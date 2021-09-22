# pypy pass

n, k = map(int, input().split())
conveyor = list(map(int, input().split()))

robot = [0] * (2 * n)
robot_idx = []

next_con = {i: i + 1 for i in range(n * 2)}
next_con[2 * n - 1] = 0


def check():
    cnt = 0
    for c in conveyor:
        cnt += (c == 0)
    return cnt >= k


answer = 0
while True:
    conveyor.insert(0, conveyor.pop())
    robot.insert(0, robot.pop())
    robot_idx = list(map(lambda x: next_con[x], robot_idx))

    temp = []
    for idx in robot_idx:
        if idx != n-1:
            temp.append(idx)
        else:
            robot[n-1] = 0
    robot_idx = temp.copy()

    # print("--------fist-------")
    # print(conveyor)
    # print(robot)
    # print(robot_idx)

    delete = -1

    for idx in range(len(robot_idx)):
        next_idx = next_con[robot_idx[idx]]
        if robot[next_idx] == 0 and conveyor[next_idx] > 0:
            conveyor[next_idx] -= 1
            robot[robot_idx[idx]] = 0
            if next_idx != n-1:
                robot[next_idx] = 1
                robot_idx[idx] = next_idx
            else:
                delete = idx

    if delete != -1:
        del robot_idx[delete]

    # print("-------second--------")
    # print(conveyor)
    # print(robot)
    # print(robot_idx)

    if conveyor[0] > 0:
        conveyor[0] -= 1
        robot[0] = 1
        robot_idx.append(0)

    # print("-------third--------")
    # print(conveyor)
    # print(robot)
    # print(robot_idx)

    if check():
        print(answer+1)
        break

    answer += 1
