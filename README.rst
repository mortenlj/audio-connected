===============
Audio Connected
===============

Watches PulseAudio events for new sinks connected, and if the name matches the configured name, make that sink the default sink.

Installation
============

Probably works best when installed with pipx_: `pipx install audio-connected`

To make it run on startup, you can add a XDG Autostart entry in `$XDG_CONFIG_HOME/autostart` (`~/.config/autostart` by default).

Example:

.. include:: audio-connected.desktop
    :code: ini


.. _pipx: https://pypa.github.io/pipx/
