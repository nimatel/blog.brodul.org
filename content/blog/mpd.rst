How to setup MPD on ubuntu
==========================

:date: 2012-07-01 22:20
:tags: mpd, fun
:category: GNU-linux

.. NOTE ::

    this is a very basic setup

Installation
++++++++++++

Install the daemon and client::

    # apt-get update
    # apt-get install mpd mpc

Configuration
+++++++++++++

Change the folowing lines::

    bind_to_address "localhost"

to::

    bind_to_address "0.0.0.0"

Comment the ALSA audio_output::

    #
    #audio_output {
    #       type            "alsa"
    #       name            "My ALSA Device"
    #       device          "hw:0,0"        # optional
    #       format          "44100:16:2"    # optional
    #       mixer_device    "default"       # optional
    #       mixer_control   "PCM"           # optional
    #       mixer_index     "0"             # optional
    #}
    #
    # An example of an OSS output:
    #


Set the web streaming::

    # An example of a httpd output (built-in HTTP streaming server):
    #
    audio_output {
            type            "httpd"
            name            "My HTTP Stream"
            encoder         "vorbis"                # optional, vorbis or lame
            port            "8000"
            quality         "5.0"                   # do not define if bitrate is defined
    #       bitrate         "128"                   # do not define if quality is defined
            format          "44100:16:1"
    }
    #

Copy some music into::

    /var/lib/mpd/music

Run the mpc on server::

    $ mpc update # update database
    $ mpc ls   # added files should  appear
    $ mpc ls | mpc add # add all files to the playlist
    $ mpc play


How to listen
+++++++++++++

Go to the client computer and open vlc. Setup a network stream (http://<yourserver>:8000)
