import file
from mutagen.dsdiff import DSDIFF
import tag


def handle(fileName):
    audio = DSDIFF(fileName)
    (tracknumber, artist, title, discnumber, totaldiscs) = tag.handle_id3_tags(audio)
    file.rename(fileName, tracknumber, artist, title, discnumber, totaldiscs)


