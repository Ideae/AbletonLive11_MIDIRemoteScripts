from __future__ import absolute_import, print_function, unicode_literals
SYSEX_IDENTITY_REQUEST = (240, 126, 127, 6, 1, 247)
DEVICE_CODE = (81, 0)
MANUFACTURER_ID = (0, 32, 41)
LIVE_MODE_SYSEX_BYTE = (0, )
STANDALONE_MODE_SYSEX_BYTE = (1, )
SESSION_LAYOUT_SYSEX_BYTE = (0, )
NOTE_LAYOUT_SYSEX_BYTE = (2, )
DRUM_LAYOUT_SYSEX_BYTE = (1, )
AUDIO_LAYOUT_SYSEX_BYTE = (4, )
USER_LAYOUT_SYSEX_BYTE = (3, )
FADER_LAYOUT_SYSEX_BYTE = (5, )
TURN_OFF_LEDS = (240, 0, 32, 41, 2, 16, 14, 0, 247)
QUIT_MESSAGE = (240, 0, 32, 41, 2, 16, 64, 247)
SYSEX_STANDARD_PREFIX = (240, 0, 32, 41, 2, 16)
SYSEX_STANDARD_SUFFIX = (247, )
CHALLENGE_PREFIX = (240, 0, 32, 41, 2, 16, 64)
SYSEX_PARAM_BYTE_MODE = (33, )
SYSEX_PARAM_BYTE_LAYOUT = (34, )
SYSEX_PARAM_BYTE_FADER_SETUP = (43, )
SYSEX_STATUS_BYTE_MODE = 45
SYSEX_STATUS_BYTE_LAYOUT = 46
LIVE_MODE_SWITCH_REQUEST = SYSEX_STANDARD_PREFIX + SYSEX_PARAM_BYTE_MODE + LIVE_MODE_SYSEX_BYTE + SYSEX_STANDARD_SUFFIX
SYSEX_CHALLENGE_RESPONSE_BYTE = (64, )
BLINK_LED_CHANNEL = 1
PULSE_LED_CHANNEL = 2
FADER_TYPE_STANDARD = 0
FADER_TYPE_BIPOLAR = 1
ACTION_BUTTON_COLORS = dict(color='DefaultButton.Off',
  pressed_color='DefaultButton.On',
  disabled_color='DefaultButton.Disabled')
USER_MODE_CHANNELS = (5, 6, 7, 13, 14, 15)
USER_MATRIX_IDENTIFIERS = [
 [
  64,65,66,67,96,97,98,99],
 [
  60,61,62,63,92,93,94,95],
 [
  56,57,58,59,88,89,90,91],
 [
  52,53,54,55,84,85,86,87],
 [
  48,49,50,51,80,81,82,83],
 [
  44,45,46,47,76,77,78,79],
 [
  40,41,42,43,72,73,74,75],
 [
  36,37,38,39,68,69,70,71]]
CHROM_MAP_CHANNEL = 3
DEVICE_MAP_CHANNEL = 4
VOLUME_MAP_CHANNEL = 8
PAN_MAP_CHANNEL = 9
SENDS_MAP_CHANNEL = 0
DR_MAP_CHANNEL = 9
FEEDBACK_CHANNELS = [CHROM_MAP_CHANNEL, DR_MAP_CHANNEL]