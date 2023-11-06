import copy
import convert
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

def handle(fileName):
    audio = MP3(fileName, ID3=EasyID3)
    all_tags = copy.deepcopy(audio.tags)
    for key, value in all_tags.items():
        tc_array = value
        sc_array = []
        if isinstance(tc_array, list):
            for t in tc_array:
                if isinstance(t, str):
                    nt = convert.sc(t)
                    sc_array.append(nt)
        audio[key] = sc_array
    audio.save()
    # 转换成简体文件名， 重命名文件
    (path, oldName) = os.path.split(fileName)
    newname = os.path.join(path, convert.sc(oldName))
    os.rename(fileName, newname)
    print(newname + ' done')
