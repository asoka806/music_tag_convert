from mutagen.mp4 import MP4
import file
import tag

def handle(fileName):
    audio = MP4(fileName)
    (tracknumber, artist, title, discnumber, totaldiscs) = tag.handle__vorbis_tags(audio, fileName)
    file.rename(fileName, tracknumber, artist, title, discnumber, totaldiscs)
