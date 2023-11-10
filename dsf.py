import file
from mutagen.dsf import DSF
import tag


def handle(fileName):
    audio = DSF(fileName)
    (tracknumber, artist, title, discnumber, totaldiscs) = tag.handle_id3_tags(audio, fileName)
    file.rename(fileName, tracknumber, artist, title, discnumber, totaldiscs)


