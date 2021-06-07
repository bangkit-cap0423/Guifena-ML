import gc
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import youtube_dl
import os
import scaper

# Generate Image Dataset (1) Due too Memory Usage, Split into 2

def extract_spectrogram(fname, iname):
    audio, sr = librosa.load(fname, res_type='kaiser_fast')
    S = librosa.feature.melspectrogram(audio, sr=sr, n_mels=128)
    log_S = librosa.power_to_db(S, ref=np.max)
    fig = plt.figure(figsize=[1, 1])
    ax = fig.add_subplot(111)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.axis("off")
    ax.axis("tight")
    plt.margins(0)
    librosa.display.specshow(log_S, sr=sr)
    fig.savefig(iname, dpi=100, pad_inches=0)
    plt.close(fig)
    plt.close('all')
    del audio, S, log_S, ax, fig


samples_folder = "soundscapes/"
images_folder = "images/"
already = os.listdir(images_folder)
d = os.listdir(samples_folder)
for i, f in enumerate(d):
    if(f.split('.')[1] == 'wav'):
      extract_spectrogram(
          samples_folder+f, f"{images_folder}/{f.replace('.wav', '.png')}")


# Generate Image Dataset 2 Due too Memory Usage, Split into 2

samples_folder = "soundscapes/"
images_folder = "images/"
already = os.listdir(images_folder)
d = os.listdir(samples_folder)
for i, f in enumerate(d):
  name = f.split('.')[0]
  tipe, nomor = name.split('_')
  print(name)
  if(f.split('.')[1] == 'wav'):
    if(tipe == 'soundscape' and int(nomor) > 300):
      extract_spectrogram(
          samples_folder+f, f"{images_folder}/{f.replace('.wav', '.png')}")
