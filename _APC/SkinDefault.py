<<<<<<< HEAD
=======
# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.9 (default, Mar 30 2022, 13:51:17) 
# [Clang 13.1.6 (clang-1316.0.21.2.3)]
# Embedded file name: output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/_APC/SkinDefault.py
# Compiled at: 2022-01-27 16:28:16
# Size of source mod 2**32: 2294 bytes
>>>>>>> d4a7b269eef325b60d6e8b8cc6298fd52c04fa34
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
from _Framework.ButtonElement import Color
import _Framework.Skin as Skin
from pushbase.colors import Blink, Pulse, Rgb
GREEN = Color(1)
GREEN_BLINK = Color(2)
RED = Color(3)
RED_BLINK = Color(4)
AMBER = Color(5)

class Defaults(object):

    class DefaultButton(object):
        On = Color(127)
        Off = Color(0)
        Disabled = Color(0)


class BiLedColors(object):

    class Session(object):
        ClipStopped = AMBER
        ClipStarted = GREEN
        ClipRecording = RED
        ClipTriggeredPlay = GREEN_BLINK
        ClipTriggeredRecord = RED_BLINK
        ClipEmpty = Color(0)
        Scene = Color(0)
        SceneTriggered = GREEN_BLINK
        NoScene = Color(0)
        StopClip = Color(0)
        StopClipTriggered = GREEN_BLINK
        RecordButton = Color(0)

    class Zooming(object):
        Selected = AMBER
        Stopped = RED
        Playing = GREEN
        Empty = Color(0)


class RgbColors(object):

    class Session(object):
        Scene = Rgb.GREEN
        SceneTriggered = Blink(Rgb.GREEN, Rgb.BLACK, 24)
        NoScene = Rgb.BLACK
        ClipStopped = Rgb.AMBER
        ClipStarted = Pulse(Rgb.GREEN.shade(1), Rgb.GREEN, 48)
        ClipRecording = Pulse(Rgb.BLACK, Rgb.RED, 48)
        ClipTriggeredPlay = Blink(Rgb.GREEN, Rgb.BLACK, 24)
        ClipTriggeredRecord = Blink(Rgb.RED, Rgb.BLACK, 24)
        ClipEmpty = Rgb.BLACK
        RecordButton = Rgb.BLACK

    class Zooming(object):
        Selected = Rgb.AMBER
        Stopped = Rgb.RED
        Playing = Rgb.GREEN
        Empty = Rgb.BLACK


class StopButtons(object):

    class Session(object):
        StopClip = Color(1)
        StopClipTriggered = Color(2)


class CrossfadeButtons(object):

    class Mixer(object):

        class Crossfade(object):
            Off = Color(0)
            A = Color(1)
            B = Color(2)


def make_default_skin():
    return Skin(Defaults)


def make_biled_skin():
    return Skin(BiLedColors)


def make_rgb_skin():
    return Skin(RgbColors)


def make_stop_button_skin():
    return Skin(StopButtons)


def make_crossfade_button_skin():
    return Skin(CrossfadeButtons)