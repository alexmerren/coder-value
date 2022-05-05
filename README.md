# Coder Value 

## Contents

- **[Development](#development)**
- **[Usage](#usage)**
- **[Testing](#testing)**

## Development

To start developing, you need [Python 3.8+](https://www.python.org/downloads/)

For a more seamless development environment, you can use [Python venv](https://docs.python.org/3/library/venv.html)

Once you start a venv, you can develop immediately!

## Usage

To configure and run the application, do the following:

1. Add GitHub Username and Access Token into `github_config`
2. You can either:
    1. Set environment variables for config, and run the application:
    ```bash
    source github_config
    env/bin/python main.py
    ```
    2. Or, run the make command:
    ```bash
    make run
    ```

## Testing 

To profile the application (for testing purposes):

```bash
env/bin/python -m cProfile tests/profile_api.py > testOutput.txt
```
