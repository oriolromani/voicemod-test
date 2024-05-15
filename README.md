# Plot spectrum to decode the message

This Python3 script deciphers a visual message encoded in an audio file using a provided noise file. It performs the following steps:

1. Subtract the noise from the challenge audio file.
2. Invert the resulting audio.
3. Plot the spectrum of the inverted audio.

## Usage

1. Install Python 3 if you haven't already. You can download it from the [official Python website](https://www.python.org/downloads/).

2. Install the required dependencies using pip, it is recommended to use a [virtual environment](https://docs.python.org/3/library/venv.html) for this. Run the following with the env activated:

```pip install -r requirements.txt```

3. Run the script like:

```python plot_spectrum_with_message.py```

The script takes the files `Challenge.wav` and `WhiteNoise.wav` provided in this repository as defaults, but those can be provided as params too like:

```python plot_spectrum_with_message.py /path/to/challenge/file /path/to/whitnoise/file```


4. Decipher the message plotted in the spectrum.

A result image `result.png` is provided in this repository
