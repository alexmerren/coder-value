from app import init_app
from os import environ

app = init_app()

HOST = environ.get("CV_HOST")
PORT = environ.get("CV_PORT")

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
