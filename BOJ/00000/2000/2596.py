words = {
    "000000" : "A",
    "001111" : "B",
    "010011" : "C",
    "011100" : "D",
    "100110" : "E",
    "101001" : "F",
    "110101" : "G",
    "111010" : "H"
}

def solve():
    n = int(input())
    string = list(input())

    result = ""
    for x in range(0, len(string), 6):
        canlist = []
        target = string[x : x + 6]
        for key, value in words.items():
            count = 0
            for index in range(6):
                if target[index] != key[index]:
                    count += 1
            
            if count <= 1:
                canlist.append(value)
        
        if len(canlist):
            result += canlist[0]
        else:
            print(x // 6 + 1)
            return
    
    print(result)
    
solve()