<<<<<<< HEAD
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import TransportComponent as TransportComponentBase
=======
# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.9 (default, Mar 30 2022, 13:51:17) 
# [Clang 13.1.6 (clang-1316.0.21.2.3)]
# Embedded file name: output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Roland_FA/transport.py
# Compiled at: 2022-01-27 16:28:16
# Size of source mod 2**32: 512 bytes
from __future__ import absolute_import, print_function, unicode_literals
import ableton.v2.control_surface.components as TransportComponentBase
>>>>>>> d4a7b269eef325b60d6e8b8cc6298fd52c04fa34
from ableton.v2.control_surface.control import ButtonControl

class TransportComponent(TransportComponentBase):
    jump_to_start_button = ButtonControl()

    @jump_to_start_button.pressed
    def jump_to_start_button(self, _):
        self.song.current_song_time = 0.0