from mutagen.flac import FLAC
import file
import tag


def handle(fileName):
    audio = FLAC(fileName)
    (tracknumber, artist, title, discnumber, totaldiscs) = tag.handle__vorbis_tags(audio, fileName)
    file.rename(fileName, tracknumber, artist, title, discnumber, totaldiscs)


