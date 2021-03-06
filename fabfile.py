#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import run, local, task, env
from fabric.colors import blue, red, green
from fabric.operations import put


env.building_dir = "/tmp/building_blog"
env.production_dir = ""
env.branch = "deploy"
env.repository = "git://github.com/brodul/blog.brodul.org.git"
env.use_ssh_config = True


@task
def local_server_deploy():
    """docstring for local_server_deploy"""

    print blue("Bootstraping buildout ...")
    local('python bootstrap.py -d')
    print blue("Running buildout ...")
    local('bin/buildout')
    local('rm -rf output')
    local('mkdir output')
    update_blog()
    print green("Local deploy done.")


@task
def build_blog():
    """docstring for build_blog"""
    local("bin/pelican -d -s pelican.conf.py")


def copy_to_server():
    """docstring for copy_to_server"""
    print blue("Copying blog to server ...")
    run("mkdir /srv/blog.brodul.org")
    return put("output/*", "/srv/blog.brodul.org").succeeded


def make_backup():
    """docstring for make_backup"""
    run(" cp -r /srv/blog.brodul.org /srv/backup.blog.brodul.org")


def revert_backup():
    """docstring for revert_backup"""
    print blue("Reverting backup ...")
    run(" cp -r /srv/backup.blog.brodul.org  /srv/blog.brodul.org")
    print green("Revert succeeded. Please try again.")


def clean_server():
    """docstring for clean_server"""
    print blue("Cleaning server ...")
    run("rm -r /srv/blog.brodul.org")


def remove_backup():
    """docstring for remove_backup"""
    print blue("Removing backup ...")
    run("rm -r /srv/backup.blog.brodul.org")
    print green("Backup removed.")


@task
def update_blog():

    build_blog()
    make_backup()
    clean_server()
    try:
        copy_to_server()
        remove_backup()
    except:
        print red("Copy failed. :(")
        revert_backup()
    else:
        print green("Copy succeeded. :D")
