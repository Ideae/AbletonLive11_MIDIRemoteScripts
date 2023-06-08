<<<<<<< HEAD
=======
# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.9 (default, Mar 30 2022, 13:51:17) 
# [Clang 13.1.6 (clang-1316.0.21.2.3)]
# Embedded file name: output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/APC20/SliderModesComponent.py
# Compiled at: 2022-01-27 16:28:16
# Size of source mod 2**32: 2700 bytes
>>>>>>> d4a7b269eef325b60d6e8b8cc6298fd52c04fa34
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
import _Framework.ButtonElement as ButtonElement
import _Framework.ModeSelectorComponent as ModeSelectorComponent

class SliderModesComponent(ModeSelectorComponent):

    def __init__(self, mixer, sliders, *a, **k):
        (super(SliderModesComponent, self).__init__)(*a, **k)
        self._mixer = mixer
        self._sliders = sliders
        self._mode_index = 0

    def disconnect(self):
        super(SliderModesComponent, self).disconnect()
        self._mixer = None
        self._sliders = None

    def set_mode_buttons(self, buttons):
        for button in self._modes_buttons:
            button.remove_value_listener(self._mode_value)

        self._modes_buttons = []
        if buttons != None:
            for button in buttons:
                identify_sender = True
                button.add_value_listener(self._mode_value, identify_sender)
                self._modes_buttons.append(button)

        self.update()

    def number_of_modes(self):
        return 8

    def update(self):
        super(SliderModesComponent, self).update()
        if self.is_enabled():
            for index in range(len(self._modes_buttons)):
                if index == self._mode_index:
                    self._modes_buttons[index].turn_on()
                else:
                    self._modes_buttons[index].turn_off()

            for index in range(len(self._sliders)):
                strip = self._mixer.channel_strip(index)
                slider = self._sliders[index]
                slider.use_default_message()
                slider.set_identifier(slider.message_identifier() - self._mode_index)
                strip.set_volume_control(None)
                strip.set_pan_control(None)
                strip.set_send_controls((None, None, None))
                slider.release_parameter()
                if self._mode_index == 0:
                    strip.set_volume_control(slider)
                else:
                    if self._mode_index == 1:
                        strip.set_pan_control(slider)
                if self._mode_index < 5:
                    send_controls = [
                     None, None, None]
                    send_controls[self._mode_index - 2] = slider
                    strip.set_send_controls(tuple(send_controls))