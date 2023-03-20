import requests
from scipy.io.wavfile import write
import sounddevice as sd
import os

auth_key = '69c90bab080141a1af241f87a7961e4a'
headers = {"authorization": auth_key, "content-type": "application/json"}


class File:
    # Used to read the file
    def read_file(filename):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(5242880)
                if not data:
                    break
                yield data

    # Used to request the file
    def request_file(self):
        upload_response = requests.post('https://api.assemblyai.com/v2/upload', headers=headers,
                                        data=read_file('output.mp3'))
        audio_url = upload_response.json()["upload_url"]
        transcript_request = {'audio_url': audio_url}
        transcript_response = requests.post("https://api.assemblyai.com/v2/transcript", json=transcript_request,
                                            headers=headers)
        _id = transcript_response.json()["id"]

        filename = "output.txt"  # saves the output to a file

        polling_response = requests.get("https://api.assemblyai.com/v2/transcript/" + _id, headers=headers)

        # shows that the file is processing
        while polling_response.json()['status'] != 'completed':
            sd.sleep(30)
            polling_response = requests.get("https://api.assemblyai.com/v2/transcript/" + _id, headers=headers)
            print("File is", polling_response.json()['status'])

        # Shows where file is saved
        with open(filename, 'w') as f:
            f.write(polling_response.json()['text'])
        print('Transcript saved to', filename)


class VoiceInput:
    # Records voice from sound device
    def record_voice(self):
        fs = 44100  # Sample rate of the recording
        seconds = 5  # Duration of the recording

        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)  # Used to record
        sd.wait()  # Wait until recording is finished
        write('output.mp3', fs, recording)  # Save as MP3 file
