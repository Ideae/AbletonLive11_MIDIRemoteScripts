<<<<<<< HEAD
=======
# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.9 (default, Mar 30 2022, 13:51:17) 
# [Clang 13.1.6 (clang-1316.0.21.2.3)]
# Embedded file name: output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/AIRA_MX_1/Colors.py
# Compiled at: 2022-01-28 05:06:40
# Size of source mod 2**32: 589 bytes
>>>>>>> d4a7b269eef325b60d6e8b8cc6298fd52c04fa34
from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ButtonElement import Color
BLINK_LED_CHANNEL = 14

class Blink(Color):

    def draw(self, interface):
        interface.send_value(self.midi_value)
        interface.send_value(0, channel=BLINK_LED_CHANNEL)


class Rgb:
    BLACK = Color(0)
    RED = Color(5)
    RED_BLINK = Blink(5)
    GREEN_HALF = Color(20)
    GREEN = Color(21)
    GREEN_BLINK = Blink(21)
    BLUE_HALF = Color(44)
    BLUE = Color(45)
    BLUE_BLINK = Blink(45)