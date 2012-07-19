Socat hack for web developers
=============================

:date: 2012-07-19 12:27
:tags: web, dev, cli
:category: GNU-linux

Sometimes you want do develop/deploy a "huge" project like RTD_ . So you create a virtual mashine, then you start the development enviroment. But the development server only listens to request on 127.0.0.1:8080. And because I am lazy and don't want to read the docs, how to change the ip and the port of the development server. I use the 'socat hack'.

First you connect to the development mashine (with ssh). Then I run:
::

    # socat TCP-LISTEN:80,fork TCP:localhost:8080 &

And now you can access the dev website just by writting the ip or hostname of the dev server.

But be careful other people can do that as well!


.. _RTD: https://github.com/rtfd/readthedocs.org
