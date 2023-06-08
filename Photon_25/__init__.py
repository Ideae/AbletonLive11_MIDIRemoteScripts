<<<<<<< HEAD
=======
# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.9 (default, Mar 30 2022, 13:51:17) 
# [Clang 13.1.6 (clang-1316.0.21.2.3)]
# Embedded file name: output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Photon_25/__init__.py
# Compiled at: 2022-01-27 16:28:16
# Size of source mod 2**32: 1082 bytes
>>>>>>> d4a7b269eef325b60d6e8b8cc6298fd52c04fa34
from __future__ import absolute_import, print_function, unicode_literals
import Live
import _Generic.GenericScript as GenericScript
from .config import *

def create_instance(c_instance):
    return GenericScript(c_instance, Live.MidiMap.MapMode.absolute, Live.MidiMap.MapMode.absolute, DEVICE_CONTROLS, TRANSPORT_CONTROLS, VOLUME_CONTROLS, TRACKARM_CONTROLS, BANK_CONTROLS, CONTROLLER_DESCRIPTIONS)