def solve():
    n = int(input()) - 1
    *arr, answer = [*map(int, input().split())]
    cache = [[-1] * 21 for _ in range(n)]

    def dp(index, value):
        if index == n:
            if value == answer:
                return 1
            return 0
        
        if cache[index][value] != -1:
            return cache[index][value]
        
        result = 0

        if 0 <= value + arr[index] <= 20:
            result += dp(index + 1, value + arr[index])
        
        if 0 <= value - arr[index] <= 20:
            result += dp(index + 1, value - arr[index])
            
        cache[index][value] = result
        return result

    print(dp(1, arr[0]))
    
solve()