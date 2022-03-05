def solution(dirs):
    answer = 0
    D = {"U": 0, "D": 1, "R": 2, "L": 3}
    M = [[] for _ in range(11 * 11)]
    AM = [[0]*121 for _ in range(121)]

    for y in range(10,-1,-1):
        for x in range(11):
            num = getNum(x, y)
            u, d, r, l = -1, -1, -1, -1
            if y != 10:
                u = getNum(x, y + 1)
            if y != 0:
                d = getNum(x, y - 1)
            if x != 10:
                r = getNum(x + 1, y)
            if x != 0:
                l = getNum(x - 1, y)
            M[num] = [u, d, r, l]

    start = getNum(5,5)
    end = -1
    for direction in dirs:
        end = M[start][D[direction]]
        if end == -1:
            continue
        if AM[start][end] != 1:
            AM[start][end] = 1
            AM[end][start] = 1
            answer += 1
        start = end

    return answer


def getNum(x, y):
    return y * 11 + x


if __name__ == "__main__":
    print("answer is",solution("ULURRDLLU"))
    print("answer is", solution("LULLLLLLU"))
