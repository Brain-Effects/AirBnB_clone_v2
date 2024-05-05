#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the web_static
"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static
    """
    # create a directory if not exists
    local("mkdir -p versions")
    # create a tgz archive of the web_static directory
    file_name = 'versions/web_static_{}.tgz'.format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    try:
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
