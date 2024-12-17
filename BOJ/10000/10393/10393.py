DAYSECOND = 12 * 3600

def calc_degree(hour, minute, second):
    hdegree = hour * 30 + minute * 0.5 + second / 120
    mdegree = minute * 6 + second / 10
    return hdegree, mdegree

def solve():
    n = int(input())
    for x in range(1, n + 1):
        angle, arrow, hour = input().split()
        angle, hour = int(angle), int(hour)
        
        second = 0
        curangle = 360 - hour * 30
        
        if arrow == 'after':
            second = ((angle - curangle) + (0 if curangle < angle else 360)) * 120 / 11
        else:
            second = ((angle - curangle) - (360 if curangle <= angle else 0)) * 120 / 11
            second += 720 * 60
        
        hour = (hour + int(second // 3600)) % 12
        hour += 12 if hour == 0 else 0
        
        minute = int(second % 3600) // 60
        second = int(second % 60 + 0.5)
        
        print(f'Case {x}: {hour}:{minute:02}:{second:02}')
    
solve()