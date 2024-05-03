n = int(input())
array = list(map(int, input().split()))
correct = [x+1 for x in range(n)]

def reverse(arr, check):
    fp, ep = 0, 0
    answer = []

    while len(answer) < 2 and fp < n and ep < n:
        if arr[fp] == check[fp]:
            fp += 1
            ep += 1
        else:
            if arr[ep] == check[fp]:
                arr = arr[:fp] + arr[fp:ep+1][::-1] + arr[ep+1:]
                answer.append([fp+1, ep+1])
                fp, ep = 0, 0
            else:
                ep += 1

    if arr == check and len(answer) <= 2:
        for _ in range(2-len(answer)):
            answer.append([1, 1])
        return answer
    else:
        return False


ans = reverse(array, correct)
if not ans:
    ans = reverse(array[::-1], correct[::-1])
    for i in range(2):
        ans[i] = [n-ans[i][1]+1, n-ans[i][0]+1]

for x in ans:
    print(*x)