<<<<<<< HEAD
=======
# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.9 (default, Mar 30 2022, 13:51:17) 
# [Clang 13.1.6 (clang-1316.0.21.2.3)]
# Embedded file name: output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/control/sysex.py
# Compiled at: 2021-06-29 09:33:48
# Size of source mod 2**32: 1044 bytes
>>>>>>> d4a7b269eef325b60d6e8b8cc6298fd52c04fa34
from __future__ import absolute_import, print_function, unicode_literals
from .control import Control, control_color

class ColorSysexControl(Control):

    class State(Control.State):
        color = control_color('DefaultButton.Disabled')

        def __init__(self, color=None, *a, **k):
            (super(ColorSysexControl.State, self).__init__)(*a, **k)
            if color is not None:
                self.color = color

        def set_control_element(self, control_element):
            super(ColorSysexControl.State, self).set_control_element(control_element)
            self._send_current_color()

        def update(self):
            super(ColorSysexControl.State, self).update()
            self._send_current_color()

        def _send_current_color(self):
            if self._control_element:
                self._control_element.set_light(self.color)

    def __init__(self, *a, **k):
        super(ColorSysexControl, self).__init__(extra_args=a, extra_kws=k)