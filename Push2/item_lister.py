<<<<<<< HEAD
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import ItemListerComponent as ItemListerComponentBase
=======
# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.9 (default, Mar 30 2022, 13:51:17) 
# [Clang 13.1.6 (clang-1316.0.21.2.3)]
# Embedded file name: output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Push2/item_lister.py
# Compiled at: 2022-01-27 16:28:16
# Size of source mod 2**32: 1259 bytes
from __future__ import absolute_import, print_function, unicode_literals
import ableton.v2.control_surface.components as ItemListerComponentBase
>>>>>>> d4a7b269eef325b60d6e8b8cc6298fd52c04fa34
from ableton.v2.control_surface.components import ItemSlot, SimpleItemSlot

class IconItemSlot(SimpleItemSlot):

    def __init__(self, icon='', *a, **k):
        (super(IconItemSlot, self).__init__)(*a, **k)
        self._icon = icon

    @property
    def icon(self):
        return self._icon


class ItemListerComponent(ItemListerComponentBase):

    def _create_slot(self, index, item, nesting_level):
        items = self._item_provider.items[self.item_offset:]
        num_slots = min(self._num_visible_items, len(items))
        slot = None
        if index == 0 and self.can_scroll_left():
            slot = IconItemSlot(icon='page_left.svg')
<<<<<<< HEAD
            slot.is_scrolling_indicator = True
        else:
            if index == num_slots - 1 and self.can_scroll_right():
                slot = IconItemSlot(icon='page_right.svg')
                slot.is_scrolling_indicator = True
            else:
                slot = ItemSlot(item=item, nesting_level=nesting_level)
                slot.is_scrolling_indicator = False
=======
            slot.is_scrolling_indicator = True
        elif index == num_slots - 1 and self.can_scroll_right():
            slot = IconItemSlot(icon='page_right.svg')
            slot.is_scrolling_indicator = True
        else:
            slot = ItemSlot(item=item, nesting_level=nesting_level)
            slot.is_scrolling_indicator = False
>>>>>>> d4a7b269eef325b60d6e8b8cc6298fd52c04fa34
        return slot