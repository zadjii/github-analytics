from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from models import db_base as base
import os
import json

__author__ = "zadjii"


strong_dupe_table = Table(
    "strong_duplicates",
    base.metadata,
    Column("left_id", Integer, ForeignKey("issue.id")),
    Column("right_id", Integer, ForeignKey("issue.id")),
)

weak_dupe_table = Table(
    "weak_duplicates",
    base.metadata,
    Column("left_id", Integer, ForeignKey("issue.id")),
    Column("right_id", Integer, ForeignKey("issue.id")),
)

related_table = Table(
    "related_table",
    base.metadata,
    Column("left_id", Integer, ForeignKey("issue.id")),
    Column("right_id", Integer, ForeignKey("issue.id")),
)


class Issue(base):
    __tablename__ = "issue"
    """
    Represents a single issue
    """

    id = Column(Integer, primary_key=True)
    raw_data = Column(String)
    number = Column(Integer)

    title = Column(String)
    state = Column(String)
    body = Column(String)

    duplicates = relationship(
        "Issue",
        secondary=strong_dupe_table,
        primaryjoin=strong_dupe_table.c.left_id == id,
        secondaryjoin=strong_dupe_table.c.right_id == id,
        backref="duplicate_of",
    )

    weak_duplicates = relationship(
        "Issue",
        secondary=weak_dupe_table,
        primaryjoin=weak_dupe_table.c.left_id == id,
        secondaryjoin=weak_dupe_table.c.right_id == id,
        backref="weak_duplicate_of",
    )

    mentioned_by = relationship(
        "Issue",
        # lazy='dynamic',
        secondary=related_table,
        primaryjoin=related_table.c.left_id == id,
        secondaryjoin=related_table.c.right_id == id,
        backref="mentioned_issues",
    )
    # backref=backref("mentioned_issues", lazy="dynamic"))

    def __init__(self, api_obj):
        self.number = api_obj.number
        self.raw_data = json.dumps(api_obj._rawData)
