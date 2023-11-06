import wave
import flac
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
            flac.handleFlac(fileName)
        elif 'audio/wav' in type.mime:
            wave.handleWave(fileName)
        else:
            print('Unsupport file mime: ' + fileName)

if __name__=="__main__":
    main()

