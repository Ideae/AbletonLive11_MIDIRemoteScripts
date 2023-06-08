<<<<<<< HEAD
=======
# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.9 (default, Mar 30 2022, 13:51:17) 
# [Clang 13.1.6 (clang-1316.0.21.2.3)]
# Embedded file name: output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/base/collection/indexed_dict.py
# Compiled at: 2021-06-29 09:33:48
# Size of source mod 2**32: 1523 bytes
>>>>>>> d4a7b269eef325b60d6e8b8cc6298fd52c04fa34
from __future__ import absolute_import, print_function, unicode_literals
from collections import OrderedDict

class IndexedDict(OrderedDict):

    def __init__(self, *args, **kwds):
        self._IndexedDict__keys = []
        (super(IndexedDict, self).__init__)(*args, **kwds)

    def __setitem__(self, key, value, *args, **kwds):
        (super(IndexedDict, self).__setitem__)(key, value, *args, **kwds)
<<<<<<< HEAD
        if key not in self._IndexedDict__keys:
            self._IndexedDict__keys.append(key)
=======
        self._IndexedDict__keys.append(key)
>>>>>>> d4a7b269eef325b60d6e8b8cc6298fd52c04fa34

    def __delitem__(self, key, *args, **kwds):
        (super(IndexedDict, self).__delitem__)(key, *args, **kwds)
        self._IndexedDict__keys.remove(key)

    def clear(self):
        super(IndexedDict, self).clear()
        self._IndexedDict__keys = []

    def popitem(self, last=True):
        item = super(IndexedDict, self).popitem(last)
        self._IndexedDict__keys.pop(-1 if last else 0)
        return item

    def keys(self):
        return self._IndexedDict__keys

    def item_by_index(self, ix):
        key = self._IndexedDict__keys[ix]
        return (
         key, self[key])

    def key_by_index(self, ix):
        return self._IndexedDict__keys[ix]

    def value_by_index(self, ix):
        return self[self._IndexedDict__keys[ix]]

    def index_by_key(self, key):
        return self._IndexedDict__keys.index(key)