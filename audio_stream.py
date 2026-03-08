import sounddevice as sd
import numpy as np
import queue


audio_queue = queue.Queue()

sample_rate = 16000
chunk_duration = 0.02 
chunk_size = int(sample_rate * chunk_duration)


def audio_callback(indata, frames, time, status):

    if status:
        print(status)

    audio_queue.put(indata.copy())


def start_stream():

    stream = sd.InputStream(
        samplerate=sample_rate,
        channels=1,
        blocksize=chunk_size,
        callback=audio_callback
    )

    stream.start()

    print("Audio streaming started")

    return stream


def get_audio_chunk():


    return audio_queue.get()
