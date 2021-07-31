import re

def solution(files):
    answer = []

    number = re.compile(r'\d+')
    input_files = []

    for idx, x in enumerate(files):
        
        original = x

        x = x.lower()

        NUMBER = number.search(x)
        HEAD = x[:NUMBER.span()[0]]
        TAIL = x[NUMBER.span()[1]:]

        input_files.append((HEAD, NUMBER.group(), idx, original))

    input_files = sorted(input_files, key=lambda x: (x[0], int(x[1]), x[2]))

    for x in input_files:
        answer.append(x[3])

    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))