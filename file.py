import os


def rename(fileName, track_no, artist, title, discnumber, totaldiscs):
    # 转换成简体文件名， 重命名文件
    (path, oldName) = os.path.split(fileName)
    (file, ext) = os.path.splitext(oldName)

    if len(title) > 0:
        if len(artist) > 0:
            if len(track_no) > 0:
                newfile = track_no + ' - ' + artist + ' - ' + title
            else:
                newfile = artist + ' - ' + title
        else:
            newfile = title
    else:
        print(f'{fileName} no title skip!')
        return

    if len(totaldiscs) > 0 and int(totaldiscs) > 1:
        newfile = discnumber + ' - ' + newfile

    newpath = os.path.join(path, newfile + ext)
    try:
        os.rename(fileName, newpath)
    except OSError as e:
        print(f'rename {fileName} error: {e.errno}, Error text: {e.strerror}')
    # 寻找同级目录下的lrc歌词文件并重命名
    (tmp_path, ext) = os.path.splitext(fileName)
    lrc_file = tmp_path + '.lrc'
    if os.path.exists(lrc_file):
        new_lrc_path = os.path.join(path, newfile + '.lrc')
        try:
            os.rename(lrc_file, new_lrc_path)
        except OSError as e:
            print(f'rename {fileName} lrc error: {e.errno}, Error text: {e.strerror}')

    print(newfile + ext + ' done')
