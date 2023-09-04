import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)

ALLOWED_HOSTS = ["*"]
API_PREFIX = "/api"
PROJECT_NAME = "Hash Game"
PROJECT_DESCRIPTION = "Server for Hash Game"
PROJECT_VERSION = "0.1.0"
DOCS_URL = "/docs"
OPENAPI_URL = "/openapi.json"
