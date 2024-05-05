#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static and distributes it to web servers
"""
from fabric.api import local, put, run, env
from datetime import datetime
import os

env.hosts = ['18.214.87.164', '54.83.129.5']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static
    """
    local("sudo mkdir -p versions")
    file_name = 'versions/web_static_{}.tgz'.format(
            datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    try:
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        archive_name = os.path.basename(archive_path)
        archive_name_no_ext = os.path.splitext(archive_name)[0]
        run("sudo mkdir -p /data/web_static/releases/{}".format(
            archive_name_no_ext))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{\
                }".format(archive_name, archive_name_no_ext))
        run("sudo rm /tmp/{}".format(archive_name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{\
                } /data/web_static/current".format(archive_name_no_ext))
        return True
    except Exception:
        return False


def deploy():
    """
    Creates and distributes an archive to web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
