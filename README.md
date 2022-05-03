# coder-value
A depressingly simple way to show that you're way too overvalued

## Python venv

To start the python venv (for development):

```bash
. env/bin/activate
```

To stop the python venv:

```bash
deactive
```

## Usage

To configure and run the application, do the following:

1. Add GitHub Username and Access Token into `github_config`
2. To set environment variables for config, execute:

```bash
source github_config
```

3. Then to run the application, execute:

```bash
env/bin/python main.py
```

## Profiling Performance

To profile the application (for testing purposes):

```bash
env/bin/python -m cProfile app/profile_api.py > testOutput.txt
```
