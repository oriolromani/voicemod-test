import argparse

import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav


def subtract_noise(challenge_file: str, noise_file: str) -> tuple[int, np.ndarray]:
    """Subtracts noise file from challenge file sample by sample"""
    with open(challenge_file, "rb") as challenge_wav, open(
        noise_file, "rb"
    ) as noise_wav:
        challenge_rate, challenge = wav.read(challenge_wav)
        noise_rate, noise = wav.read(noise_wav)

    if challenge_rate != noise_rate:
        raise ValueError("Sampling rates of the audio files do not match.")

    result_audio = challenge - noise
    return challenge_rate, result_audio


def plot_spectrum(audio: np.ndarray, sampling_rate: int) -> None:
    """Plots audio spectrum"""
    plt.figure(figsize=(20, 5))
    plt.specgram(audio, Fs=sampling_rate)
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.savefig("result.png")
    plt.show()


def main():
    parser = argparse.ArgumentParser(
        description="Process and plot audio spectrum with noise subtraction."
    )
    parser.add_argument(
        "challenge_file",
        nargs="?",
        default="Challenge.wav",
        help="Path to the challenge WAV file (default: Challenge.wav)",
    )
    parser.add_argument(
        "noise_file",
        nargs="?",
        default="WhiteNoiseMono.wav",
        help="Path to the noise WAV file (default: WhiteNoiseMono.wav)",
    )

    args = parser.parse_args()

    sampling_rate, result_audio = subtract_noise(args.challenge_file, args.noise_file)
    inverted_audio = np.flip(result_audio)
    plot_spectrum(inverted_audio, sampling_rate)


if __name__ == "__main__":
    main()
