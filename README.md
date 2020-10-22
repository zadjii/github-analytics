# Duplicate graph

A tool for building a visual graph of all the duplicate issues for a repo

Create a personal access token on github, and slam it in a file named `secrets.json`, like so:

```json
{
    "GITHUB_API_TOKEN" : "your_token_here",

    "REPO" : "microsoft/terminal"
}
```


Run these scripts to build the graph

```sh
# outdated steps
# python main.py > duplicate-issues.json
# python filter_issues.py duplicate-issues.json > short-dupe-issues.json

# Gather all the "Resolution-Duplicate" issues, and all their comments
python main.py > long-duplicate-issues.json
# Build a graph.json that includes all the issues referenced by the duplicate issues
python build_graph.py long-duplicate-issues.json > graph.json
```
Then,

run a local python webserver to be able to deliver the `graph.json` to the wepbage.

In python 3:
```sh
python -m http.server
```

then navigate to localhost:8000/graphs.html






## Contributing

After cloning the repo, run `pip install -r requirements.txt`

### Code formatting

This project uses [`black`](https://github.com/psf/black) for code formatting.
To format the code, run `black .`. You might need to add your python scripts
directory to your path. For me, this was done with:

```
set PATH=%PATH%;%localappdata%\Packages\PythonSoftwareFoundation.Python.3.7_qbz5n2kfra8p0\LocalCache\local-packages\Python37\Scripts
```
