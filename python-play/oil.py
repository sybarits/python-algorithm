def get_oil_size(land, start_point, check, depth, width, oil_num):
    # land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [
    #     1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
    if check[start_point[0]][start_point[1]] != 0:
        return check[start_point[0]][start_point[1]]
    size = 1
    start = [start_point]
    end = []
    check[start_point[0]][start_point[1]] = 1
    while len(start) != 0:
        # print('start')
        # print(start)
        for s in start:
            if (s[1] - 1) >= 0 and land[s[0]][s[1] -1] == 1 and check[s[0]][s[1] - 1] == 0:
                size += 1
                end.append([s[0], s[1] - 1])
                check[s[0]][s[1] - 1] = oil_num
            if (s[1] + 1) < width and land[s[0]][s[1] + 1] == 1 and check[s[0]][s[1] + 1] == 0:
                size += 1
                end.append([s[0], s[1] + 1])
                check[s[0]][s[1] + 1] = oil_num
            if (s[0] - 1) >= 0 and land[s[0] - 1][s[1]] == 1 and check[s[0] - 1][s[1]] == 0:
                size += 1
                end.append([s[0] - 1, s[1]])
                check[s[0] - 1][s[1]] = oil_num
            if (s[0] + 1) < depth and land[s[0] + 1][s[1]] == 1 and check[s[0] + 1][s[1]] == 0:
                size += 1
                end.append([s[0] + 1, s[1]])
                check[s[0] + 1][s[1]] = oil_num

        start = end
        end = []

    return size

def solution(land):
    answer = 0
    depth = len(land)
    width = len(land[0])
    oil_num = 1
    for i in range(len(land[0])):
        max_oil = 0
        check = [[0 for _ in range(width)] for _ in range(depth) ]
        for deep in range(len(land)):
            if land[deep][i] == 0:
                continue
            if deep != 0 and land[deep-1][i] == 1 and land[deep][i] == 1:
                continue
            oil_size = get_oil_size(land,[deep,i], check, depth, width, oil_num)
            if oil_size != 0:
                oil_num += 1
            max_oil += oil_size
        if max_oil > answer:
            answer = max_oil
        
    return answer


if __name__ == "__main__":
    result = solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [
                      1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]])
    print("result", result)
    result = solution([[1, 1, 1, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 0, 0]])
    print("result", result)
