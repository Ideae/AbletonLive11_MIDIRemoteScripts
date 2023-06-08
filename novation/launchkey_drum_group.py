<<<<<<< HEAD
=======
# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.9 (default, Mar 30 2022, 13:51:17) 
# [Clang 13.1.6 (clang-1316.0.21.2.3)]
# Embedded file name: output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/novation/launchkey_drum_group.py
# Compiled at: 2021-06-29 09:33:48
# Size of source mod 2**32: 2118 bytes
>>>>>>> d4a7b269eef325b60d6e8b8cc6298fd52c04fa34
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import listens, liveobj_valid
from ableton.v2.control_surface.components import PlayableComponent
from .drum_group import DrumGroupComponent as DrumGroupComponentBase
from .util import get_midi_color_value_for_track

class DrumGroupComponent(DrumGroupComponentBase):

    def __init__(self, *a, **k):
        (super(DrumGroupComponent, self).__init__)(*a, **k)
        self._track = None
        self._track_color = 0

    def set_parent_track(self, track):
        self._track = track
        self._DrumGroupComponent__on_track_color_changed.subject = track if liveobj_valid(track) else None
        self._DrumGroupComponent__on_track_color_changed()

    def set_drum_group_device(self, drum_group_device):
        super(DrumGroupComponent, self).set_drum_group_device(drum_group_device)
        if not liveobj_valid(self._drum_group_device):
            self._update_assigned_drum_pads()
            self._update_led_feedback()

    def can_scroll_page_up(self):
        if not liveobj_valid(self._drum_group_device):
            return False
        return super(DrumGroupComponent, self).can_scroll_page_up()

    def _update_led_feedback(self):
        PlayableComponent._update_led_feedback(self)

    def _update_button_color(self, button):
        pad = self._pad_for_button(button)
        color = self._color_for_pad(pad) if pad else self._track_color
        if color in ('DrumGroup.PadFilled', 'DrumGroup.PadEmpty'):
            if liveobj_valid(self._track):
                color = self._track_color
        button.color = color

    @listens('color')
    def __on_track_color_changed(self):
        self._track_color = get_midi_color_value_for_track(self._track)
        self._update_led_feedback()