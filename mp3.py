from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

import file
import tag


def handle(fileName):
    audio = MP3(fileName, ID3=EasyID3)
    (tracknumber, artist, title, discnumber, totaldiscs) = tag.handle__vorbis_tags(audio, fileName)
    file.rename(fileName, tracknumber, artist, title, discnumber, totaldiscs)
