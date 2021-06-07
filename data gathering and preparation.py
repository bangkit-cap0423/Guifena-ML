import gc
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import youtube_dl
import os
import scaper
# !apt install ffmpeg
# pip install scaper
# pip install youtube_dl

os.chdir('drive/MyDrive/audio_alt_path')

# download data from youtube (the forest sound manually downloaded)
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
}
linkchainsaw = ['https://www.youtube.com/watch?v=0DzsPL-xElE', 'https://www.youtube.com/watch?v=1MgcrYdYas0',
                'https://www.youtube.com/watch?v=9HcahqYUVoc', 'https://www.youtube.com/watch?v=AhcY8QVSLtM',
                'https://www.youtube.com/watch?v=BBukw6JpCeg', 'https://www.youtube.com/watch?v=BsYFCAuPjwE',
                'https://www.youtube.com/watch?v=C46X66FU_Dw', 'https://www.youtube.com/watch?v=LH08k5Kf4AI',
                'https://www.youtube.com/watch?v=NJUl3gPX07o', 'https://www.youtube.com/watch?v=_6uZ1HyHSQY',
                'https://www.youtube.com/watch?v=kHNWRR0hJ08', 'https://www.youtube.com/watch?v=yaaHJV5VOXQ']

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
  for link in linkchainsaw:
    ydl.download([link])



# Generate Dataset Chainsaw sound + Forest Sound, we combine forest sound and chainsaw sound
import scaper
soundscape_duration = 30.0
outfolder = 'soundscapes/'
foreground = os.path.expanduser("foreground")
background = os.path.expanduser("background")
sc = scaper.Scaper(soundscape_duration, foreground, background)
sc.add_background(label=("const", "forest"),
                  source_file=("choose", []),
                  source_time=("uniform", 0, 300-soundscape_duration))

for i in range(1000):
    audiofile = outfolder+f'/normal_{i}.wav'
    jamsfile = outfolder+f'/normal_{i}.jams'
    txtfile = outfolder+f'/normal_{i}.txt'
    sc.generate(audiofile, jamsfile,
                allow_repeated_label=True,
                allow_repeated_source=True,
                disable_sox_warnings=True,
                no_audio=False)

sc.add_event(label=("const", "chainsaw"),
             source_file=("choose", []),
             source_time=("uniform", 10, 30),
             event_time=("const", 0),
             event_duration=("const", 30),
             snr=("uniform", -5, 0),
             pitch_shift=("uniform", -15, 15),
             time_stretch=None)

for i in range(1000):
    audiofile = outfolder+f'/soundscape_{i}.wav'
    jamsfile = outfolder+f'/soundscape_{i}.jams'
    sc.generate(audiofile, jamsfile,
                allow_repeated_label=True,
                allow_repeated_source=True,
                disable_sox_warnings=True,
                no_audio=False)
