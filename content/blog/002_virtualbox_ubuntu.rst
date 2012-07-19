Virtualbox modules setup - Ubuntu 12.04
=======================================

:date: 2012-07-15 16:54
:tags: fail, virtualbox, ubuntu_fail
:category: GNU-linux

There is allways something wrong about vbox modules. And thas is completly normal, because adding modules to the kernel is not that trivial.
What is trivial, is write documentation in the program itself or on the website.

If you update virtualbox. The modules and the module API may change.
Which means you have to compile the modules for your kernel.

If you start an virtual mashine in the gui you get a message.
That you should run::

    $ sudo /etc/init.d/vboxdrv setup

But there is no such script. But when you are starting virtualbox via CLI. You get informative message::

    WARNING: The character device /dev/vboxdrv does not exist.
             Please install the virtualbox-ose-dkms package and the appropriate
             headers, most likely linux-headers-generic.

             You will not be able to start VMs until this problem is fixed.

So you have to install the virtualbox-ose-dkms::

    $ sudo apt-get install virtualbox-ose-dkms

Then we can see if the vbox module is added::

    dkms status

Then install it::

    $ # dkms install virtualbox/<version>
    $ sudo dkms install virtualbox/4.1.12


If you dont have the kernel headers you will get this error::

    Error! Your kernel headers for kernel 3.2.0-26-generic cannot be found.
    Please install the linux-headers-3.2.0-26-generic package,
    or use the --kernelsourcedir option to tell DKMS where it's located

So you have to install them::

    $ sudo apt-get install linux-headers-3.2.0-26-generic

Then we have to 'start' the modules::

    $ sudo /etc/init.d/virtualbox start

I hope it works.
:D

