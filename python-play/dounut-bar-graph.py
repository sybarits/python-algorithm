def solution(edges):
    start = [ 0 for _ in range(1000000) ]
    end = [ 0 for _ in range(1000000) ]
   
    for e in edges:
        start[e[0]] += 1
        end[e[1]] += 1
    bar = 0
    eight = 0
    solo_dot = 0
    solo_dot_cnt = 0

    for i in range(1000000):
        if start[i] == 0 and end[i] != 0:
            bar += 1
        if start[i] == 2 and end[i] != 0:
            eight += 1
        if start[i] >= 2 and end[i] == 0:
            solo_dot = i
    
    for e in edges:
        if e[0] == solo_dot:
            solo_dot_cnt += 1

    dounut = solo_dot_cnt - bar - eight

    return [solo_dot, dounut, bar, eight]


if __name__ == "__main__":
    edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
    print("solution is",solution(edges))
