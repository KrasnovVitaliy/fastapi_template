import os

import tomli

with open(os.path.join("pyproject.toml"), mode="rb") as fp:
    pyproject = tomli.load(fp)
PACKAGE_VERSION = pyproject["tool"]["poetry"]["version"]

DOCKER_IMAGE_REGISTRY = "dockeradmin.cyou:8005"
DOCKER_IMAGE_NAME = "sample_service"
DOCKER_REGISTRY_USER = "user"
DOCKER_REGISTRY_PASSWORD = "password"
