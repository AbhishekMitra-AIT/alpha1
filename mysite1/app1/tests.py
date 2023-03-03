# from django.test import TestCase
from django.shortcuts import render, redirect
import random, wave, sys, pyaudio, time
import numpy as np
from .models import *

# Create your tests here.


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1 
RATE = 44100
RECORD_SECONDS = 5

def record_audio(request,msg3):
        # messages.info(request, 'Recording Started..')
        prefix = 'MICO-'
        rand_num = random.randint(100000, 999999)
        audio_files = ((prefix+str(rand_num))+str('.wav'))
        audio_file_path = 'Audio_media'

        # context = {}
        with wave.open(audio_files, 'wb') as wf:
                p = pyaudio.PyAudio()
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(p.get_sample_size(FORMAT))
                wf.setframerate(RATE)

                stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

                print(f'Recording Started for {RECORD_SECONDS}sec..')
                # context['msg2'] = 'Recording Started..'
                start_time = time.time()

                for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
                        wf.writeframes(stream.read(CHUNK))
                        
                        # progress = wf.tell() / wf.getnframes()
                # messages.info(request, 'Recording Complete.')
                        elapsed_time = time.time() - start_time
                        print(f"In progress {int(elapsed_time)}sec..", end='\r')

                print('Recording Complete.')
                stream.close()
                
        p.terminate()
        wf.close()

        # Create an instance of audio_db1 model and save the .wav file and user details
        audio = audio_db1()
        audio.email = msg3

        audio.audio_file.save(audio_files, open(audio_files, 'rb'))
        audio.save()

        # request.session['msg5'] = 'Recording Complete.' # publishing value1
        return redirect('dashboard')


def play_audio(request,id):
        recd_data = audio_db1.objects.get(pk = id)
        wav_file = wave.open(recd_data.audio_file, 'rb')

        # instantiate PyAudio
        audio = pyaudio.PyAudio()

        # open the stream
        stream = audio.open(format=audio.get_format_from_width(wav_file.getsampwidth()),
                        channels=wav_file.getnchannels(),
                        rate=wav_file.getframerate(),
                        output=True)

        # read data and play stream
        data = wav_file.readframes(1024)

        # messages.info(request, 'Playback Started..')
        print('Playback Started..')      
        max_amplitude = 25000  # initialize maximum amplitude value
        while data:
                stream.write(data)
                chunk = np.frombuffer(data, dtype=np.int16)  # convert data to numpy array
                chunk_max_amplitude = np.max(np.abs(chunk))  # find maximum amplitude value in chunk
                # enable below to check if audio amplitude crosses a given threshold
                # if chunk_max_amplitude > max_amplitude:
                #         print('your voice amplitude crossed > 25000')
                data = wav_file.readframes(1024)
        
        print('Playback Finished.')
        # messages.info(request, 'Playback Finished.')

        # stop stream and close
        stream.stop_stream()
        stream.close()
        audio.terminate() # terminate PyAudio

        return redirect('dashboard')
