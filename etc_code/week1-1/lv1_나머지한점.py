def solution(v):
    x, y = [], []
    
    for p in v:
        if p[0] in x:
            x.pop(x.index(p[0]))
        else:
            x.append(p[0])
        if p[1] in y:
            y.pop(y.index(p[1]))
        else:
            y.append(p[1])

    return [x.pop(), y.pop()]

if __name__ == "__main__":
    print(solution([[1, 4], [3, 4], [3, 10]]))
    print(solution([[1, 1], [2, 2], [1, 2]]))