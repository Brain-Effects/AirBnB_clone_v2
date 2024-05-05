#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static
"""
from fabric.api import local, put, run, env
from datetime import datetime
import os

env.hosts = ['18.214.87.164', '54.83.129.5']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Uncompress the archive to the folder
        # /data/web_static/releases/<archive filename without extension>
        # on the web server
        archive_name = os.path.basename(archive_path)
        archive_name_no_ext = os.path.splitext(archive_name)[0]
        run("mkdir -p /data/web_static/releases/{}".format(
            archive_name_no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
            archive_name, archive_name_no_ext))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_name))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a new the symbolic link /data/web_static/current on the web
        # server, linked to the new version of your code
        # (/data/web_static/releases/<archive filename without extension>)
        run("ln -s /data/web_static/releases/{\
                } /data/web_static/current".format(archive_name_no_ext))

        return True
    except Exception:
        return False
