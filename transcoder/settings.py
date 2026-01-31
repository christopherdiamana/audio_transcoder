PROFILES = {
    'very_low':  {'bitrate': 64,  'codec': 'aac', 'sample_rate': '44100', 'channels': 2},
    'low':       {'bitrate': 96,  'codec': 'aac', 'sample_rate': '44100', 'channels': 2},
    'normal':    {'bitrate': 128, 'codec': 'aac', 'sample_rate': '44100', 'channels': 2},
    'high':      {'bitrate': 192, 'codec': 'aac', 'sample_rate': '44100', 'channels': 2},
    'very_high': {'bitrate': 256, 'codec': 'aac', 'sample_rate': '44100', 'channels': 2},
}

AUDIO_QUALITY_PROFILES = {
    'very_low': 64,
    'low': 96,
    'normal': 128,
    'high': 192,
    'very_high': 256
}

DEFAULT_CODEC = 'aac'
DEFAULT_SAMPLE_RATE = '44100'
DEFAULT_CHANNELS = '2'

SEGMENT_FILENAME = 'segment_%03d'
MASTER_FILENAME = 'master'
OUTPUT_DIRECTORY = 'output'
OUTPUT_FILENAME = 'playlist'
OUTPUT_FILETYPE = 'm3u8'
