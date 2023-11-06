import wave
import flac
import mp3
import os
import mutagen

def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname

def main():
    music_path = './music/'
    for fileName in findAllFile(music_path):
        type = mutagen.File(fileName)
        if type is None:
            continue
        if 'audio/flac' in type.mime:
            flac.handle(fileName)
        elif 'audio/wav' in type.mime:
            wave.handle(fileName)
        elif 'audio/mp3' in type.mime:
            mp3.handle(fileName)
        else:
            print('Unsupport file mime: ' + ' '.join(type.mime) + ' file: ' + fileName)

if __name__=="__main__":
    main()

