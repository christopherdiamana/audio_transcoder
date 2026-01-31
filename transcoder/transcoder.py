from transcoder.ffprobe import get_audio_info
from transcoder.ffmpeg import get_output_profiles, generate_map_variants
from transcoder.settings import MASTER_FILENAME, OUTPUT_FILETYPE, OUTPUT_DIRECTORY, SEGMENT_FILENAME, OUTPUT_FILENAME, \
    DEFAULT_CODEC, DEFAULT_SAMPLE_RATE, DEFAULT_CHANNELS


def run(filename):

    metadata = get_audio_info(filename)
    profiles = get_output_profiles(metadata['bit_rate'])

    master_filename = f'{MASTER_FILENAME}.{OUTPUT_FILETYPE}'
    segment_filename = f'{OUTPUT_DIRECTORY}/%v/{SEGMENT_FILENAME}.ts'
    output_filename = f'{OUTPUT_DIRECTORY}/%v/{OUTPUT_FILENAME}.{OUTPUT_FILETYPE}'

    bit_rates = [
        bitrate
        for i, value in enumerate(list(profiles.values()))
        for bitrate in (f'-b:a:{i}', f'{value}k')
    ]

    result = generate_map_variants(
        filename=filename,
        codec=DEFAULT_CODEC,
        sample_rate=DEFAULT_SAMPLE_RATE,
        channels=DEFAULT_CHANNELS,
        bitrates=bit_rates,
        stream_map_names=list(profiles.keys()),
        master_name=master_filename,
        segment_filename=segment_filename,
        output=output_filename
    )

    return result