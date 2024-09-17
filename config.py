import os

SOME_SERVICE_PORT = os.getenv("SOME_SERVICE8PORT")
if not SOME_SERVICE_PORT:
    raise Exception