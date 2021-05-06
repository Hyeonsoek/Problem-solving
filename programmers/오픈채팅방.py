def solution(record):
    
    logs = []
    user_list = {}
    for x in record:
        command = x.split()
        logs.append(command)
        if command[0][0] == 'E' or command[0][0] == 'C':
            user_list[command[1]] = command[2]
    
    results = []
    for log in logs:
        if log[0][0] == 'E':
            results.append(user_list[log[1]]+"님이 들어왔습니다.")
        if log[0][0] == 'L':
            results.append(user_list[log[1]]+"님이 나갔습니다.")
    return results