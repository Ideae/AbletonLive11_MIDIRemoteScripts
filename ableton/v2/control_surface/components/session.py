<<<<<<< HEAD
=======
# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.9 (default, Mar 30 2022, 13:51:17) 
# [Clang 13.1.6 (clang-1316.0.21.2.3)]
# Embedded file name: output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/components/session.py
# Compiled at: 2022-01-28 05:06:24
# Size of source mod 2**32: 12507 bytes
>>>>>>> d4a7b269eef325b60d6e8b8cc6298fd52c04fa34
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
from itertools import count
import Live
from ...base import EventObject, in_range, listens, listens_group, product
from ..component import Component
from ..control import ButtonControl
from .scene import SceneComponent

class SessionComponent(Component):
    _session_component_ends_initialisation = True
    scene_component_type = SceneComponent
    managed_select_button = ButtonControl(color='Session.Select',
      pressed_color='Session.SelectPressed')
    managed_delete_button = ButtonControl(color='Session.Delete',
      pressed_color='Session.DeletePressed')
    managed_duplicate_button = ButtonControl(color='Session.Duplicate',
      pressed_color='Session.DuplicatePressed')

    def __init__(self, session_ring=None, auto_name=False, *a, **k):
        (super(SessionComponent, self).__init__)(*a, **k)
        self._session_ring = session_ring
        self._SessionComponent__on_offsets_changed.subject = self._session_ring
        self._stop_all_button = None
        self._stop_track_clip_buttons = None
        self._stop_clip_triggered_value = 'Session.StopClipTriggered'
        self._stop_clip_value = 'Session.StopClip'
        self._stop_clip_disabled_value = 'Session.StopClipDisabled'
        self._track_slots = self.register_disconnectable(EventObject())
        self._selected_scene = self._create_scene()
        self._scenes = [self._create_scene() for _ in range(self._session_ring.num_scenes)]
        if self._session_component_ends_initialisation:
            self._end_initialisation()
        if auto_name:
            self._auto_name()
        self._SessionComponent__on_track_list_changed.subject = self.song
        self._SessionComponent__on_scene_list_changed.subject = self.song
        self._SessionComponent__on_selected_scene_changed.subject = self.song.view

    def _end_initialisation(self):
        self._SessionComponent__on_selected_scene_changed()
        self._reassign_scenes_and_tracks()

    def _create_scene(self):
        return self.scene_component_type(parent=self, session_ring=(self._session_ring))

    def scene(self, index):
        return self._scenes[index]

    def selected_scene(self):
        return self._selected_scene

    def _auto_name(self):
        self.name = 'Session_Control'
        self.selected_scene().name = 'Selected_Scene'
        for track_index in range(self._session_ring.num_tracks):
            clip_slot = self.selected_scene().clip_slot(track_index)
            clip_slot.name = 'Selected_Scene_Clip_Slot_%d' % track_index

        for scene_index in range(self._session_ring.num_scenes):
            scene = self.scene(scene_index)
            scene.name = 'Scene_%d' % scene_index
            for track_index in range(self._session_ring.num_tracks):
                clip_slot = scene.clip_slot(track_index)
                clip_slot.name = '%d_Clip_Slot_%d' % (track_index, scene_index)

    def set_stop_all_clips_button(self, button):
        self._stop_all_button = button
        self._SessionComponent__on_stop_all_value.subject = button
        self._update_stop_all_clips_button()

    def set_stop_track_clip_buttons(self, buttons):
        self._stop_track_clip_buttons = buttons
        self._SessionComponent__on_stop_track_value.replace_subjects(buttons or [])
        self._update_stop_track_clip_buttons()

    def set_managed_select_button(self, button):
        self.managed_select_button.set_control_element(button)
        self.set_modifier_button(button, 'select')

    def set_managed_delete_button(self, button):
        self.managed_delete_button.set_control_element(button)
        self.set_modifier_button(button, 'delete')

    def set_managed_duplicate_button(self, button):
        self.managed_duplicate_button.set_control_element(button)
        self.set_modifier_button(button, 'duplicate')

    def set_modifier_button(self, button, name, clip_slots_only=False):
        for y in range(self._session_ring.num_scenes):
            scene = self.scene(y)
            if not clip_slots_only:
                getattr(scene, 'set_{}_button'.format(name))(button)
            else:
                for x in range(self._session_ring.num_tracks):
                    getattr(scene.clip_slot(x), 'set_{}_button'.format(name))(button)

    def set_clip_launch_buttons(self, buttons):
        if buttons:
            for button, (x, y) in buttons.iterbuttons():
                scene = self.scene(y)
                slot = scene.clip_slot(x)
                slot.set_launch_button(button)

        else:
            for x, y in product(range(self._session_ring.num_tracks), range(self._session_ring.num_scenes)):
                scene = self.scene(y)
                slot = scene.clip_slot(x)
                slot.set_launch_button(None)

    def set_scene_launch_buttons(self, buttons):
        num_scenes = self._session_ring.num_scenes
        if buttons:
            for x, button in enumerate(buttons):
                scene = self.scene(x)
                scene.set_launch_button(button)

        else:
            for index in range(self._session_ring.num_scenes):
                scene = self.scene(index)
                scene.set_launch_button(None)

    @listens('offset')
    def __on_offsets_changed(self, *a):
        if self.is_enabled():
            self._reassign_scenes_and_tracks()

    def _reassign_scenes_and_tracks(self):
        self._reassign_tracks()
        self._reassign_scenes()

    def set_rgb_mode(self, color_palette, color_table, clip_slots_only=False):
        for y in range(self._session_ring.num_scenes):
            scene = self.scene(y)
            if not clip_slots_only:
                scene.set_color_palette(color_palette)
                scene.set_color_table(color_table)
            else:
                for x in range(self._session_ring.num_tracks):
                    slot = scene.clip_slot(x)
                    slot.set_clip_palette(color_palette)
                    slot.set_clip_rgb_table(color_table)

    def update(self):
        super(SessionComponent, self).update()
        if self.is_enabled():
            self._update_stop_track_clip_buttons()
            self._update_stop_all_clips_button()
            self._reassign_scenes_and_tracks()

    def _update_stop_track_clip_buttons(self):
        if self.is_enabled():
            for index in range(self._session_ring.num_tracks):
                self._update_stop_clips_led(index)

    @listens('scenes')
    def __on_scene_list_changed(self):
        self._reassign_scenes()

    @listens('visible_tracks')
    def __on_track_list_changed(self):
        self._reassign_tracks()

    @listens('selected_scene')
    def __on_selected_scene_changed(self):
        if self._selected_scene is not None:
            self._selected_scene.set_scene(self.song.view.selected_scene)

    def _update_stop_all_clips_button(self):
        if self.is_enabled():
            button = self._stop_all_button
            if button:
                button.set_light(button.is_pressed())

    def _reassign_scenes(self):
        scenes = self.song.scenes
        for index, scene in enumerate(self._scenes):
            scene_index = self._session_ring.scene_offset + index
            scene.set_scene(scenes[scene_index] if len(scenes) > scene_index else None)
            scene.set_track_offset(self._session_ring.track_offset)

        if self._selected_scene is not None:
            self._selected_scene.set_track_offset(self._session_ring.track_offset)

    def _reassign_tracks(self):
        tracks_to_use = self._session_ring.tracks_to_use()
<<<<<<< HEAD
        tracks = list(map(lambda t: t if isinstance(t, Live.Track.Track) else None
, tracks_to_use))
=======
        tracks = list(map(lambda t: t if isinstance(t, Live.Track.Track) else None, tracks_to_use))
>>>>>>> d4a7b269eef325b60d6e8b8cc6298fd52c04fa34
        self._SessionComponent__on_fired_slot_index_changed.replace_subjects(tracks, count())
        self._SessionComponent__on_playing_slot_index_changed.replace_subjects(tracks, count())
        self._update_stop_all_clips_button()
        self._update_stop_track_clip_buttons()

    @listens('value')
    def __on_stop_all_value(self, value):
        self._stop_all_value(value)

    def _stop_all_value(self, value):
        if self.is_enabled():
<<<<<<< HEAD
            if not (value != 0 or self._stop_all_button.is_momentary()):
=======
            if not (value is not 0 or self._stop_all_button.is_momentary()):
>>>>>>> d4a7b269eef325b60d6e8b8cc6298fd52c04fa34
                self.song.stop_all_clips()
            self._update_stop_all_clips_button()

    @listens_group('value')
    def __on_stop_track_value(self, value, button):
        if self.is_enabled():
<<<<<<< HEAD
            if not (value != 0 or button.is_momentary()):
=======
            if not (value is not 0 or button.is_momentary()):
>>>>>>> d4a7b269eef325b60d6e8b8cc6298fd52c04fa34
                tracks = self._session_ring.tracks_to_use()
                track_index = list(self._stop_track_clip_buttons).index(button) + self._session_ring.track_offset
                if in_range(track_index, 0, len(tracks)):
                    if tracks[track_index] in self.song.tracks:
                        tracks[track_index].stop_all_clips()

    @listens_group('fired_slot_index')
    def __on_fired_slot_index_changed(self, track_index):
        self._on_fired_slot_index_changed(track_index)

    def _on_fired_slot_index_changed(self, track_index):
        session_ring = self._session_ring
        button_index = track_index - session_ring.track_offset
        if in_range(button_index, 0, session_ring.num_tracks):
            self._update_stop_clips_led(button_index)

    @listens_group('playing_slot_index')
    def __on_playing_slot_index_changed(self, track_index):
        self._on_playing_slot_index_changed(track_index)

    def _on_playing_slot_index_changed(self, track_index):
        session_ring = self._session_ring
        button_index = track_index - session_ring.track_offset
        if in_range(button_index, 0, session_ring.num_tracks):
            self._update_stop_clips_led(button_index)

    def _update_stop_clips_led(self, index):
        tracks_to_use = self._session_ring.tracks_to_use()
        track_index = index + self._session_ring.track_offset
        if self.is_enabled():
<<<<<<< HEAD
            if self._stop_track_clip_buttons is not None:
                if index < len(self._stop_track_clip_buttons):
                    button = self._stop_track_clip_buttons[index]
                    if button is not None:
=======
            if self._stop_track_clip_buttons != None:
                if index < len(self._stop_track_clip_buttons):
                    button = self._stop_track_clip_buttons[index]
                    if button != None:
>>>>>>> d4a7b269eef325b60d6e8b8cc6298fd52c04fa34
                        value_to_send = None
                        if track_index < len(tracks_to_use):
                            if tracks_to_use[track_index].clip_slots:
                                track = tracks_to_use[track_index]
                                if track.fired_slot_index == -2:
                                    value_to_send = self._stop_clip_triggered_value
<<<<<<< HEAD
                                else:
                                    if track.playing_slot_index >= 0:
                                        value_to_send = self._stop_clip_value
                                    else:
                                        value_to_send = self._stop_clip_disabled_value
                        if value_to_send is None:
                            button.set_light(False)
                        else:
                            if in_range(value_to_send, 0, 128):
                                button.send_value(value_to_send)
                            else:
                                button.set_light(value_to_send)
=======
                                elif track.playing_slot_index >= 0:
                                    value_to_send = self._stop_clip_value
                                else:
                                    value_to_send = self._stop_clip_disabled_value
                        if value_to_send == None:
                            button.set_light(False)
                        elif in_range(value_to_send, 0, 128):
                            button.send_value(value_to_send)
                        else:
                            button.set_light(value_to_send)
>>>>>>> d4a7b269eef325b60d6e8b8cc6298fd52c04fa34
