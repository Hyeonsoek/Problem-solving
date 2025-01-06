while True:
    string = input()
    if not int(string):
        break
    mid = len(string) // 2
    
    if len(string) & 1:
        print("yes" if string[:mid]==string[mid+1:][::-1] else "no")
    else:
        print("yes" if string[:mid]==string[mid:][::-1] else "no")