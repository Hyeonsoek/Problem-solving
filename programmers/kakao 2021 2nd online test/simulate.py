import api

from collections import defaultdict

def make_board(loc_response):
    N = 5
    board = [[0] * N for _ in range(N)]
    redirect = defaultdict((int, int))

    for j in range(N):
        for i in range(N):
            redirect[i * N + j] = (i, j)

    for loc in loc_response['locations']:
        i, j = redirect[loc['id']]
        board[i][j] = loc['located_bikes_count']

    del redirect

    return board

def make_trucks(trucks_response):
    trucks = [(0, 0)] * 5

    for truck in trucks_response:
        trucks[truck['id']] = (trucks['location_id'], trucks['loaded_bikes_count'])

    return trucks

def make_commandline(board, trucks):
    command_line = []



    return command_line

def init():
    url, auth = "", ""
    start_response = api.start_api(url, auth)
    auth = start_response["auth_key"]

    return url, auth

def simulate():
    url, auth = init()

    locations_response = api.locations_api(url, auth)
    board = make_board(locations_response)

    trucks_response = api.trucks_api(url, auth)
    trucks = make_trucks(trucks_response)

    commandline = make_commandline(board, trucks)