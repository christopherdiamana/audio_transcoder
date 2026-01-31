import subprocess

from transcoder.settings import AUDIO_QUALITY_PROFILES


def get_output_profiles(bit_rate):
    profiles = {
        profile: bitrate
        for profile, bitrate in AUDIO_QUALITY_PROFILES.items()
        if bitrate <= bit_rate
    }
    return profiles


def generate_map_variants(filename, codec, sample_rate, channels, bitrates, stream_map_names, master_name,
                          segment_filename, output):
    command = (
            [
                'ffmpeg',
                '-i', filename,
                '-ar', sample_rate,
                '-ac:a', channels,
                '-codec:a', codec,
            ]
            + bitrates
            + ['-map', '0:a'] * len(bitrates)
            + [
                '-f', 'hls',
                '-var_stream_map', ' '.join(f'a:0,name:{name}' for name in stream_map_names),
                '-master_pl_name', master_name,
                '-hls_segment_filename', segment_filename,
                output
            ]
    )

    try:
        result = subprocess.run(
            command,
            capture_output=True,       # Capture stdout and stderr
            text=True,                 # Get strings, not bytes
            check=True,                # Raise error if command fails
            timeout=10                 # Prevent hanging forever
        )
        return result

    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e.stderr}")

    except subprocess.TimeoutExpired:
        print("The command took too long!")