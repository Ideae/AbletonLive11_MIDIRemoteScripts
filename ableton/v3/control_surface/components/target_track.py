from __future__ import absolute_import, print_function, unicode_literals
from ...base import MultiSlot, depends, listenable_property, listens, listens_group, liveobj_changed, liveobj_valid, scene_index
from .. import Component
from ..controls import ToggleButtonControl
from ..display import Renderable

class TargetTrackComponent(Component, Renderable):
    lock_button = ToggleButtonControl(color='TargetTrack.LockOff',
      on_color='TargetTrack.LockOn')

    @depends(show_message=None)
    def __init__(self, name='Target_Track', show_message=None, is_private=False, *a, **k):
        (super().__init__)(a, name=name, is_private=is_private, **k)
        self._show_message = show_message
        self._target_track = None
        self._target_clip = None
        self._locked_to_track = False
        self.lock_button.connect_property(self, 'is_locked_to_track')
        self.register_slot(self.song.view, self._selected_track_changed, 'selected_track')
        self.register_slot(MultiSlot(subject=self,
          listener=(self._update_target_clip),
          event_name_list=('target_track', 'arrangement_clips')))
        self.register_slot(self.application.view, self._update_target_clip, 'focused_document_view')
        self.register_slot(self.song.view, self._update_target_clip, 'detail_clip')
        self.register_slot(self.song.view, self._update_target_clip, 'selected_scene')
        self._selected_track_changed()

    def disconnect(self):
        self._target_track = None
        self._target_clip = None
        super().disconnect()

    @listenable_property
    def target_track(self):
        return self._target_track

    @listenable_property
    def target_clip(self):
        return self._target_clip

    @listenable_property
    def is_locked_to_track(self):
        return self._locked_to_track

    @is_locked_to_track.setter
    def is_locked_to_track(self, is_locked):
        if is_locked != self._locked_to_track:
            self._locked_to_track = is_locked
            current_track = self._target_track
            self._set_target_track()
            self.notify_is_locked_to_track()
            if self._locked_to_track:
                self._show_message('Locked to {}'.format(self._target_track.name))
            else:
                self._show_message('Unlocked from {}'.format(current_track.name))

    def _selected_track_changed(self):
        self._set_target_track()

    def _set_target_track(self):
        if not (self._locked_to_track and liveobj_valid(self._target_track)):
            new_target = self._get_new_target_track()
            if liveobj_changed(self._target_track, new_target):
                self._target_track = new_target
                self._update_target_clip()
                self.notify_target_track()
            self.is_locked_to_track = False

    def _get_new_target_track(self):
        return self.song.view.selected_track

    def _update_target_clip(self):
        self._TargetTrackComponent__on_target_clip_slot_has_clip_changed.subject = None
        clip = None
        if self._target_track in self.song.tracks:
            if self.application.view.focused_document_view == 'Session':
                clip = self._target_clip_from_session()
            else:
                clip = self._target_clip_from_arrangement()
        if liveobj_changed(self._target_clip, clip):
            self._target_clip = clip
            self.notify_target_clip()

    def _target_clip_from_arrangement(self):
        clip = self.song.view.detail_clip
        if liveobj_valid(clip):
            if clip in self._target_track.arrangement_clips:
                return clip

    def _target_clip_from_session(self):
        clip_slot = self._target_track.clip_slots[scene_index()]
        self._TargetTrackComponent__on_target_clip_slot_has_clip_changed.subject = clip_slot
        if clip_slot.has_clip:
            return clip_slot.clip

    @listens('has_clip')
    def __on_target_clip_slot_has_clip_changed(self):
        self._update_target_clip()


class ArmedTargetTrackComponent(TargetTrackComponent):

    def __init__(self, *a, **k):
        self._armed_track_list = []
        (super().__init__)(*a, **k)
        self._ArmedTargetTrackComponent__on_tracks_changed.subject = self.song
        self._ArmedTargetTrackComponent__on_tracks_changed()

    def disconnect(self):
        self._armed_track_list = None
        super().disconnect()

    def _selected_track_changed(self):
        if not self._armed_track_list:
            self._set_target_track()

    def _get_new_target_track(self):
        if self._armed_track_list:
            return self._armed_track_list[-1]
        return super()._get_new_target_track()

    @listens('visible_tracks')
    def __on_tracks_changed(self):
        tracks = self._tracks()
        self._ArmedTargetTrackComponent__on_arm_changed.replace_subjects(tracks)
        self._ArmedTargetTrackComponent__on_frozen_state_changed.replace_subjects(tracks)
        self._refresh_armed_track_list()

    @listens_group('arm')
    def __on_arm_changed(self, _):
        self._refresh_armed_track_list()

    @listens_group('is_frozen')
    def __on_frozen_state_changed(self, _):
        self._refresh_armed_track_list()

    def _refresh_armed_track_list(self):
        tracks = self._tracks()
        for track in self._armed_track_list:
            if liveobj_valid(track):
                if track.arm:
                    if not track.is_frozen:
                        if track not in tracks:
                            pass
                    self._armed_track_list.remove(track)

        for track in tracks:
            if track.arm:
                if not track.is_frozen:
                    if track not in self._armed_track_list:
                        self._armed_track_list.append(track)

        self._set_target_track()

    def _tracks(self):
        return [t for t in self.song.tracks if liveobj_valid(t) if t.can_be_armed]