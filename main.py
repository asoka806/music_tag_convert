import wave
import flac
import mp3
import mp4
import os
import mutagen
import dff
import sys

def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname

def main(argv):
    if len(argv) <= 1:
        print('Please input your music path')
        return
    music_path = os.path.abspath(argv[1])
    # path1 = '.\music'
    # music_path = os.path.abspath(path1)

    print('music path = ' + music_path)
    for fileName in findAllFile(music_path):
        if fileName.endswith('.lrc'):
            continue
        type = mutagen.File(fileName)
        if type is None:
            continue
        if 'audio/flac' in type.mime:
            flac.handle(fileName)
        elif 'audio/wav' in type.mime:
            wave.handle(fileName)
        elif 'audio/mp3' in type.mime:
            mp3.handle(fileName)
        elif 'audio/mp4' in type.mime:
            mp4.handle(fileName)
        elif 'audio/m4a' in type.mime:
            mp4.handle(fileName)
        elif 'audio/x-dff' in type.mime:
            dff.handle(fileName)
        else:
            print('Unsupport file mime: ' + ' '.join(type.mime) + ' file: ' + fileName)

if __name__=="__main__":
    main(sys.argv)

