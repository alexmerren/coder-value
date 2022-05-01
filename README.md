# coder-value
A depressingly simple way to show that you're way too overvalued

## Python venv

To start the python venv (for development):

```bash
. ./venv/bin/activate
```

To stop the python venv:

```bash
deactive
```

## Usage

To run the application, do the following:
```bash
export FLASK_APP=app
Flask run
```

## Testing/Profiling

To profile the application (for testing purposes):
```bash
env/bin/python -m cProfile app/github/test.py > testOutput.txt
```
