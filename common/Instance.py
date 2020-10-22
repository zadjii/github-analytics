import os
import imp
import _thread
import signal
import configparser
import json
from migrate.versioning import api
from common.SimpleDB import SimpleDB
from common.ResultAndData import *
from models import db_base
import time

SECRETS_FILE = "secrets.json"
CONFIG_FILE = "config.json"


def get_config():
    secrets = json.load(open(SECRETS_FILE, "r", encoding="utf-8"))
    config = json.load(open(CONFIG_FILE, "r", encoding="utf-8"))
    appconfig = {}
    appconfig.update(secrets)
    appconfig.update(config)
    return appconfig


def get_github_token():
    return get_config()["GITHUB_API_TOKEN"]


def get_github_repo():
    return get_config()["REPO"]


class Instance(object):
    def __init__(self):
        """
        Creates a Instance which can track database and authentication state
        """
        ms_cli_root = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        self._working_dir = os.path.join(".localdata")
        self._db = None
        self._db_name = "github-analytics.db"
        self._db_models = db_base
        self._db_map = {}

        self._appconfig = None
        self._session = None
        self._current_user_guid = None

        self.init_dir()

    def init_dir(self):
        """
        1. creates the WD if it doesn't exist
        2. Reads data from the working dir
        3. creates the db if it doesn't exist
        """

        # 1.
        exists = os.path.exists(self._working_dir)
        if not exists:
            os.makedirs(self._working_dir)
        else:
            # 2.
            # self.load_conf()
            pass

        # 3.
        exists = os.path.exists(self._db_path())
        # print("The db does not exist" if not exists else "The db already exists")
        self._db = self.make_db_session()
        self._db.engine.echo = False
        if not exists:
            print("Creating db...")
            self._db.create_all_and_repo(self._db_migrate_repo())
            print(
                "The database ({}) should have been created here".format(
                    self._db_path()
                )
            )
            print("The migration repo should have been created here")

    def _db_uri(self):
        return "sqlite:///" + self._db_path()

    def _db_migrate_repo(self):
        return os.path.join(self._working_dir, "db_repository")

    def get_db(self):
        thread_id = _thread.get_ident()

        if not (thread_id in list(self._db_map.keys())):
            db = self.make_db_session()
            self._db_map[thread_id] = db

        return self._db_map[thread_id]

    def make_db_session(self):
        db = SimpleDB(self._db_uri(), self._db_models)
        db.engine.echo = False
        return db

    def _db_path(self):
        return os.path.join(self._working_dir, self._db_name)

    def migrate(self):
        repo = self._db_migrate_repo()
        uri = self._db_uri()
        db = self.get_db()
        migration_name = "%04d_migration.py" % (api.db_version(uri, repo) + 1)
        migration = repo + "/versions/" + migration_name
        tmp_module = imp.new_module("old_model")
        old_model = api.create_model(uri, repo)
        exec(old_model, tmp_module.__dict__)
        script = api.make_update_script_for_model(
            uri, repo, tmp_module.meta, db.Base.metadata
        )
        open(migration, "wt").write(script)
        api.upgrade(uri, repo)
        print("New migration saved as " + migration)
        print("Current database version: " + str(api.db_version(uri, repo)))
        api.upgrade(uri, repo)
        print("New database version: " + str(api.db_version(uri, repo)))
