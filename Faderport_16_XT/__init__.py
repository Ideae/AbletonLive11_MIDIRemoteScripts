<<<<<<< HEAD
=======
# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.9 (default, Mar 30 2022, 13:51:17) 
# [Clang 13.1.6 (clang-1316.0.21.2.3)]
# Embedded file name: output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Faderport_16_XT/__init__.py
# Compiled at: 2022-01-27 16:28:16
# Size of source mod 2**32: 777 bytes
>>>>>>> d4a7b269eef325b60d6e8b8cc6298fd52c04fa34
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.capabilities import CONTROLLER_ID_KEY, PORTS_KEY, REMOTE, SCRIPT, controller_id, inport, outport
from MackieControlXT import MackieControlXT

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=6479,
                          product_ids=[516],
                          model_name=['PreSonus FP16']), 
     
     PORTS_KEY: [
                 inport(props=[]),
                 inport(props=[SCRIPT, REMOTE]),
                 outport(props=[]),
                 outport(props=[SCRIPT, REMOTE])]}


def create_instance(c_instance):
    return MackieControlXT(c_instance)