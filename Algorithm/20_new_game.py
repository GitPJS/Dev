k = 4  # 말의 개수

chess_map = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
start_horse_location_and_directions = [[0, 0, 0], [0, 1, 0], [0, 2, 0], [2, 2, 2]]

# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(game_map)
    turn_count = 1
    current_stacked_horse_map = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(horse_count):
        r, c, d = horse_location_and_directions[i]
        current_stacked_horse_map[r][c].append(i)

    while turn_count <= 1000:
        for horse_index in range(horse_count):
            n = len(game_map)
            r, c, d = horse_location_and_directions[horse_index]
            new_r = r + dr[d]
            new_c = c + dc[d]

        turn_count += 1
    return -1


print(
    get_game_over_turn_count(k, chess_map, start_horse_location_and_directions)
)  # 2가 반환 되어야합니다
