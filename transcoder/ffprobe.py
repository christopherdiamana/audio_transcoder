import json
import subprocess


def get_audio_info(filename):
    command = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'a',
        '-show_entries', 'stream=bit_rate,codec_name,sample_rate',
        '-print_format', 'json',
        filename
    ]
    value = -1
    try:
        result = subprocess.run(
            command,
            capture_output=True,       # Capture stdout and stderr
            text=True,                 # Get strings, not bytes
            check=True,                # Raise error if command fails
            timeout=10                 # Prevent hanging forever
        )
        value = json.loads(result.stdout)['streams'][0]
        value['bit_rate'] = int(value['bit_rate'])         # Specify the bitrate in bits/s.
        value['sample_rate'] = int(value['sample_rate'])   # Specify the sample rate in Hz.

    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e.stderr}")

    except subprocess.TimeoutExpired:
        print("The command took too long!")

    return value