#!/usr/bin/python3
from datetime import datetime
from fabric.api import local


def do_pack():
    """Generates a .tgz
    """

    d = datetime.now()
    now = d.strftime('%Y%m%d%H%M%S')

    local("mkdir -p versions")
    local("tar -czvf versions/web_static_{}.tgz web_static".format(now))
