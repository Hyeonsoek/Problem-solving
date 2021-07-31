def min_time(start, end):

    start_hour, start_min = start.split(':')
    end_hour, end_min = end.split(':')

    start = int(start_hour) * 60 + int(start_min)
    end = int(end_hour) * 60 + int(end_min)

    return end - start

def make_melody(start, end, melody):

    ret = ''
    len_melody = int(len(melody))
    cnt = min_time(start, end)

    for x in range(cnt):
        x %= len_melody
        ret += melody[x:x+1]

    return ret

def change_code(melody):

    change = [('C#','H'),('D#','I'),('F#','J'),('F#','K'),('G#','L'),('A#','M')]

    for pre, post in change:
        melody = melody.replace(pre, post)

    return melody

def solution(m, musicinfos):
    answer = ''

    index = 1
    long_music = []

    m = change_code(m)

    for x in musicinfos:
        start, end, name, melody = x.split(',')

        melody = change_code(melody)
        melody = make_melody(start, end, melody)

        if len(m) <= len(melody) and m in melody:
            long_music.append((min_time(start, end), index, name))
            index += 1

    long_music = sorted(long_music, key=lambda x : (-x[0], x[0]))

    if long_music:
        return long_music[0][2]
    else:
        return "(None)"

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]  ))