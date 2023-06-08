<<<<<<< HEAD
=======
# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.9 (default, Mar 30 2022, 13:51:17) 
# [Clang 13.1.6 (clang-1316.0.21.2.3)]
# Embedded file name: output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/novation/util.py
# Compiled at: 2021-06-29 09:33:48
# Size of source mod 2**32: 1106 bytes
>>>>>>> d4a7b269eef325b60d6e8b8cc6298fd52c04fa34
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import liveobj_valid
from ableton.v2.control_surface.components import find_nearest_color
from .colors import CLIP_COLOR_TABLE, RGB_COLOR_TABLE, Rgb

def skin_scroll_buttons(scoll_component, color, pressed_color):
    scoll_component.scroll_up_button.color = color
    scoll_component.scroll_down_button.color = color
    scoll_component.scroll_up_button.pressed_color = pressed_color
    scoll_component.scroll_down_button.pressed_color = pressed_color


def is_song_recording(song):
    return song.session_record or song.record_mode


def get_midi_color_value_for_track(track):
    if liveobj_valid(track):
        color = CLIP_COLOR_TABLE.get(track.color, None)
        if color is None:
            color = find_nearest_color(RGB_COLOR_TABLE, track.color)
        return color
    return Rgb.BLACK.midi_value