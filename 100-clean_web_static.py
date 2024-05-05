#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the
contents of the web_static, distributes it to web servers,
and deletes out-of-date archives
"""
from fabric.api import local, put, run, env
from datetime import datetime
import os

env.hosts = ['18.214.87.164', '54.83.129.5']


def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    number = int(number)

    # keep at least one version
    if number == 0:
        number = 1

    count = 0
    for file in reversed(sorted(os.listdir("versions"))):
        count += 1
        if count > number:
            local("rm versions/{}".format(file))
            run("rm -rf /data/web_static/releases/{}".format(file))

    return True
