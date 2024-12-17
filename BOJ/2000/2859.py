HOUR = 60
DAY = HOUR * 24
WEEK = DAY * 7

days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def to_min(hhmm):
    hh, mm = map(int, hhmm.split(':'))
    return hh * HOUR + mm

def to_hour(mm):
    return f"{mm // HOUR % 24:02d}:{mm % HOUR:02d}"

def solve():
    startF, startS, priodF, priodS = [to_min(input()) for _ in range(4)]
    for x in range(1440):
        if startF == startS:
            print(days[(startS // DAY) % 7])
            print(to_hour(startS))
            return
        else:
            if startS < startF:
                startS += priodS
            else:
                startF += priodF
    
    print("Never")

solve()