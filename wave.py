from mutagen.wave import WAVE
from mutagen.id3 import TIT2, TPE1, TRCK, TALB, TPOS, TDRC, TCON, TMED, TPE2, TDOR, TPUB, TSO2, TSOP, TXXX, APIC
import copy
import os
import convert

fields = {
    'TIT2': TIT2,
    'TPE1': TPE1,
    'TRCK': TRCK,
    'TALB': TALB,
    'TPOS': TPOS,
    'TDRC': TDRC,
    'TCON': TCON,
    'TMED': TMED,
    'TPE2': TPE2,
    'TDOR': TDOR,
    'TPUB': TPUB,
    'TXXX:ARTISTS': TXXX,
    'TSO2': TSO2,
    'TSOP': TSOP,
    'APIC': APIC
}
def handleWave(fileName):
    audio = WAVE(fileName)

    all_tags = copy.deepcopy(audio.tags)
    for tag in all_tags:
        if fields.keys().__contains__(tag):
            # print(tag)
            tc_array = audio.get(tag).text
            encoding = audio.get(tag).encoding
            sc_array = []
            if isinstance(tc_array, list):
                for t in tc_array:
                    if isinstance(t, str):
                        nt = convert.sc(t)
                        sc_array.append(nt)
            if tag == 'TXXX:ARTISTS':
                desc = audio.get(tag).desc
                audio.tags.add(fields[tag](encoding=encoding, text=sc_array, desc=desc))
            else:
                audio.tags.add(fields[tag](encoding=encoding, text=sc_array))
    audio.save()
    # print(audio)
    # 转换成简体文件名， 重命名文件
    (path, oldName) = os.path.split(fileName)
    newname = os.path.join(path, convert.sc(oldName))
    os.rename(fileName, newname)
    print(newname + ' done')


    #
    #
    # # ID3v2.4 TITLE
    # print(audio.get('TIT2').text)
    #
    # # ID3v2.4 ARTIST
    # print(audio.get('TPE1').text)
    #
    # # ID3v2.4 TRACK
    # print(audio.get('TRCK').text)
    #
    # # ID3v2.4 ALBUM
    # print(audio.get('TALB').text)
    #
    # # ID3v2.4 DISCNUMBER
    # print(audio.get('TPOS').text)
    #
    # # ID3v2.4 YEAR
    # print(audio.get('TDRC').text)
    #
    # # ID3v2.4 GENRE
    # print(audio.get('TCON').text)
    #
    # # ID3v2.4 MEDIATYPE
    # print(audio.get('TMED').text)
    #
    # # ID3v2.4 ALBUMARTIST
    # print(audio.get('TPE2').text)
    #
    # # ID3v2.4 ORIGYEAR
    # print(audio.get('TDOR').text)
    #
    # # ID3v2.4 PUBLISHER
    # print(audio.get('TPUB').text)
    #
    # # ID3v2.4 Other fields TXXX:fieldname
    # print(audio.get('TXXX:ARTISTS').text)
    #
    # # ID3v2.4 ALBUMARTISTSORT
    # print(audio.get('TSO2').text)
    #
    # # ID3v2.4 ARTISTSORT
    # print(audio.get('TSOP').text)

# {'TIT2': TIT2(encoding=<Encoding.UTF8: 3>, text=['沉默 (feat. Kristal)']),
# 'TPE1': TPE1(encoding=<Encoding.UTF8: 3>, text=['陳小春']),
# 'TRCK': TRCK(encoding=<Encoding.LATIN1: 0>, text=['4/12']),
# 'TALB': TALB(encoding=<Encoding.UTF8: 3>, text=['算你狠']),
# 'TPOS': TPOS(encoding=<Encoding.LATIN1: 0>, text=['1/1']),
# 'TDRC': TDRC(encoding=<Encoding.UTF8: 3>, text=['2003-08-29']),
# 'TCON': TCON(encoding=<Encoding.UTF8: 3>, text=['POP']),
# 'TMED': TMED(encoding=<Encoding.UTF8: 3>, text=['CD']),
# 'TPE2': TPE2(encoding=<Encoding.UTF8: 3>, text=['陳小春']),
# 'TDOR': TDOR(encoding=<Encoding.UTF8: 3>, text=['2003-08-29']),
# 'TPUB': TPUB(encoding=<Encoding.UTF8: 3>, text=['BMG Taiwan']),
# 'TXXX:SCRIPT': TXXX(encoding=<Encoding.UTF8: 3>, desc='SCRIPT', text=['Hant']),
# 'TSO2': TSO2(encoding=<Encoding.UTF8: 3>, text=['Chan, Jordan']),
# 'TSOP': TSOP(encoding=<Encoding.UTF8: 3>, text=['Chan, Jordan']),
# 'TXXX:DISCID': TXXX(encoding=<Encoding.UTF8: 3>, desc='DISCID', text=['D10EE90F']),
# 'TXXX:ARTISTS': TXXX(encoding=<Encoding.UTF8: 3>, desc='ARTISTS', text=['陳小春']),
# 'TXXX:originalyear': TXXX(encoding=<Encoding.UTF8: 3>, desc='originalyear', text=['2003']),


# 'TXXX:BARCODE': TXXX(encoding=<Encoding.UTF8: 3>, desc='BARCODE', text=['828765622226']),
# 'TXXX:CATALOGNUMBER': TXXX(encoding=<Encoding.UTF8: 3>, desc='CATALOGNUMBER', text=['82876562222']),
# 'COMM::eng': COMM(encoding=<Encoding.UTF8: 3>, lang='eng', desc='', text=['ExactAudioCopy v0.99pb5']),
# 'TXXX:MusicBrainz Album Type': TXXX(encoding=<Encoding.UTF8: 3>, desc='MusicBrainz Album Type', text=['album']),
# 'TXXX:MusicBrainz Album Status': TXXX(encoding=<Encoding.UTF8: 3>, desc='MusicBrainz Album Status', text=['official']),
# 'TXXX:MusicBrainz Album Release Country': TXXX(encoding=<Encoding.UTF8: 3>, desc='MusicBrainz Album Release Country', text=['TW']),
# 'TXXX:Acoustid Id': TXXX(encoding=<Encoding.UTF8: 3>, desc='Acoustid Id', text=['b5c43d1e-bd04-4b32-a890-6b775f83804d']),
# 'TXXX:MusicBrainz Album Id': TXXX(encoding=<Encoding.UTF8: 3>, desc='MusicBrainz Album Id', text=['f0cf73d7-28d2-4341-9840-28a2601c82fc']),
# 'UFID:http://musicbrainz.org': UFID(owner='http://musicbrainz.org', data=b'95755d13-c364-4eaa-a243-60b46f17d0d2'),
# 'TXXX:MusicBrainz Artist Id': TXXX(encoding=<Encoding.UTF8: 3>, desc='MusicBrainz Artist Id', text=['808760ff-bac0-4397-9aa8-d4596a09f938']),
# 'TXXX:MusicBrainz Album Artist Id': TXXX(encoding=<Encoding.UTF8: 3>, desc='MusicBrainz Album Artist Id', text=['808760ff-bac0-4397-9aa8-d4596a09f938']),
# 'TXXX:MusicBrainz Release Group Id': TXXX(encoding=<Encoding.UTF8: 3>, desc='MusicBrainz Release Group Id', text=['6c5f150d-40b2-3b87-bc5d-83e0f3be134a']),
