# -*- coding: utf-8 -*-
__author__ = 'Kirill Yakovenko'
__email__ = 'kirill.yakovenko@gmail.com'

import os
from fabric.api import task, sudo, run, cd, settings, env, prefix, put
from fabric.contrib.project import rsync_project

env.setdefault('destination', '/srv/')


@task
def install_sqlite():
    pass


@task
def install_mysql():
    pass


@task
def install_packages():
    sudo('apt-get update')
    sudo('apt-get install -y git virtualenv build-essential python-dev')


@task
def install_wiring_pi():
    with cd('/tmp'):
        with settings(warn_only=True):
            sudo('[ -d wiringPi ] && rm -R wiringPi')
        run('git clone git://git.drogon.net/wiringPi')
        with cd('wiringPi'):
            sudo('./build')


@task
def install_python_env():
    with cd(env.destination):
        sudo('virtualenv .ve')
        put('requirements.pip', '/tmp')
        with prefix('source .ve/bin/activate'):
            sudo('pip install -r /tmp/requirements.pip')


@task
def upload():
    with cd(env.destination):
        sudo('[ -d zero ] || mkdir zero/')
        sudo('chown -fR {0} zero/'.format(env.user))
    rsync_project(os.path.join(env.destination, 'zero'), local_dir='zero/*', delete=True, exclude=[".DS_Store"])


@task
def deploy():
    install_packages()
    install_python_env()
    upload()
    #install_mysql()
    #install_supervisor()
    #restart()

