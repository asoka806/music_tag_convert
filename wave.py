from mutagen.wave import WAVE
import file
import tag

def handle(fileName):
    audio = WAVE(fileName)
    (tracknumber, artist, title, discnumber, totaldiscs) = tag.handle_id3_tags(audio, fileName)
    file.rename(fileName, tracknumber, artist, title, discnumber, totaldiscs)
