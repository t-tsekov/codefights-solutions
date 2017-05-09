def lrc2subRip(lrcLyrics, songLength):

    def readTime(lyric):
        parts = lyric[1:lyric.index(']')].split(':')
        print(parts)
        ss = parts.pop()
        if '.' in ss:
            ss, ms = ss.split('.')
        else:
            ms = 0
        ss = int(ss)
        ms = int(ms)
        mm = int(parts.pop())
        if len(parts):
            hh = int(parts.pop())
        else:
            hh = 0
        hh += mm / 60
        mm %= 60

        return '{:02d}:{:02d}:{:02d},{:03d}'.format(hh, mm, ss, ms * 10)

    output = []
    for i, line in enumerate(lrcLyrics, 1):
        output.append(str(i))
        start_time = readTime(line)
        if i == len(lrcLyrics):
            end_time = readTime('[' + songLength + ']')
        else:
            end_time = readTime(lrcLyrics[i])
        output.append("{} --> {}".format(start_time, end_time))
        output.append(line[line.index(']') + 2:])
        if i < len(lrcLyrics):
            output.append("")
    return output