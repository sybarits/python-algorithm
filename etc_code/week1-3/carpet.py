def solution(brown, yellow):
    total = brown + yellow
    x, y = (brown // 2 - 1), 3

    while x * y != total:
        y += 1
        x -= 1

    return [x, y]


if __name__ == "__main__":
    print("answer is", solution(10, 2))
    print("answer is", solution(8, 1))
    print("answer is", solution(24, 24))
