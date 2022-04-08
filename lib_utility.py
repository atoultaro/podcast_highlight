import numpy as np
from math import floor
import librosa


def cos_sim(a, b):
    """
    Dot product between vector a and vector b
    :param a: vector a
    :param b: vector b
    :return: dot product
    """
    return np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))


def load_wav_16k_mono(filename, sr=16000):
    """
    Load a WAV file.
    :param filename: filename of the target sound file
    :param sr: sampling rate
    :return: sound samples in array
    """
    samples, sr = librosa.load(filename, sr=sr)
    if samples.ndim == 2:
        samples = samples[:, 1]

    return samples


def load_wav_16k_mono_segment(filename, begin_sec, end_sec):
    """
    Load a WAV file with specified begin time and end time.
    :param filename:
    :param begin_sec:
    :param end_sec:
    :return:
    """
    samples, sr = librosa.load(filename, sr=16000)  # AudioSet needs input audio of sampling rate 16k
    if samples.ndim == 2:
        samples = samples[:, 1]
    samples = samples[floor(begin_sec * sr):floor(end_sec * sr)]

    return samples
