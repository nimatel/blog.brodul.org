Running fabric on localhost
===========================

:date: 2012-08-21 11:23
:tags: fabric, python
:category: GNU-linux

Intro
+++++

I the modern world when all people live in "the clouds". The old type of sysadmins is obsolete.
The modern sysadmin must be flexible, he needs a bunch of tools to assist him.
So that he can deploy a SaaS_ application in less than 10 minutes. 
Also testing, staging servers are a must nowadays to ensure QoS_.

.. _SaaS: http://en.wikipedia.org/wiki/Software_as_a_service
.. _QoS: http://en.wikipedia.org/wiki/Quality_of_service

When I started (in 2008), I quite fast discovered the potential of Bash on linux servers.
Don't get me wrong the basic skills in bash are needed to manage sysadmin tasks.
But bash scripts are hard to maintain, usually developers can't read them.
And you are limited to bash, which means if yo want to do something "crazy" you need a CLI program for it.
I like to use Fabric which is a command line tool and a python lib for common sysadmin task, especially working with ssh and scp.

If you don't like python, try to find a similar tool for you language, like Capistrano_ for Ruby.

.. _Capistrano: http://en.wikipedia.org/wiki/Capistrano

Problem
+++++++

As mentioned before Fabric is a great tool to work with ssh. So there are functions like sudo(), run(), put().
So I wrote a bunch of functions that rely on those. Note there is also a function that runs a command locally local().
So I basically run: fab deploy_this_application -H webserver.example.com 
Then I decided to move the deploy to the server. So every time there is a git merge to branch "deploy" the application deploys itself into production (it's this blog BTW).
But `a wild problem appeared`__. I want to run deploy_this_application on localhost which is full of run(), put() calls.

.. _meme: http://knowyourmeme.com/memes/a-wild-x-appears-wild-x-appeared

__ meme_

Solution
++++++++

iElectric_ proposed to use "fab deploy_this_application -H localhost" and ssh keys to avoid password prompt. So I did it. With a few optimizations. 

.. _iElectric: http://www.domenkozar.com

First of all I created a custom key pair (local_rsa) for this propose
and added the pub key to authorized_keys:
::

    ssh-keygen 
    cd .ssh/
    cat local_rsa.pub >> authorized_keys

Then I edited the authorized_keys, so the sshd allows this key only from localhost:
::

    from="127.0.0.1,::1" ssh-rsa T94PNuDnXAoGyqInja ... nhiEZeLDx/SrsMOnJlUZsfHU4jdLrk1htpeQ== githook@webi

But then I needed to specify the key to fabric:
::
    
    fab deploy_this_application -H localhost -i ~/.ssh/local_rsa

I don't want to do that ever time. (Well it wouldn't matter, because the command is run by a script.)

So you can set an attribute to the env object to True and fabric will use ssh .config file:
::
    
    env.use_ssh_config = True

Then create/edit the ~/.ssh/config file:
::

    Host localhost
        IdentityFile ~/.ssh/local_rsa


So now you can use "fab deploy_this_application -H localhost" without any problems.
