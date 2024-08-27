from invoke import Collection

from . import docker

# from . import keys

ns = Collection()
ns.add_collection(docker)
