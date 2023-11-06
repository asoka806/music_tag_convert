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
    base = './music/'
    for fileName in findAllFile(base):
        type = mutagen.File(fileName)
        if type == None:
            continue
        if 'audio/flac' in type.mime:
            print(fileName + ' is a flac')
            flac.handleFlac(fileName)
        elif 'audio/wav' in type.mime:
            print('this is a wav')
            wave.handleWave(fileName)

if __name__=="__main__":
    main()

