<<<<<<< HEAD
=======
# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.9 (default, Mar 30 2022, 13:51:17) 
# [Clang 13.1.6 (clang-1316.0.21.2.3)]
# Embedded file name: output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/RemoteSL/__init__.py
# Compiled at: 2021-06-29 09:33:48
# Size of source mod 2**32: 1163 bytes
>>>>>>> d4a7b269eef325b60d6e8b8cc6298fd52c04fa34
from __future__ import absolute_import, print_function, unicode_literals
from .RemoteSL import RemoteSL

def create_instance(c_instance):
    return RemoteSL(c_instance)


from _Framework.Capabilities import *

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=4661,
                          product_ids=[11],
                          model_name='SL MkII'), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC, REMOTE]),
                 inport(props=[NOTES_CC, REMOTE, SCRIPT]),
                 outport(props=[NOTES_CC, SYNC]),
                 outport(props=[SCRIPT])]}