import sys

# global min_cal

def solution(diet):
    answer = 0
    cal_sum = [[0,0,0] for _ in range(len(diet))]
    global min_cal
    min_cal  = sys.maxsize#maxint
    cal_sum[0][0] = diet[0][0]
    cal_sum[0][1] = diet[0][1]
    cal_sum[0][2] = diet[0][2]

    # DFS(diet, cal_sum, 0, 0)
    # DFS(diet, cal_sum, 0, 1)
    # DFS(diet, cal_sum, 0, 2)
    BFS(diet, cal_sum)
    print(cal_sum)
    print(min_cal)
    return answer


def BFS(diet, cal_sum):
    start = [[0,0], [0,1], [0,2]]
    end = []

    while start:

        for r,c in start:
            cur_sum = cal_sum[r][c]
            global min_cal
            if min_cal < cur_sum:
                continue
            if r == len(diet)-1:
                min_cal = min(cur_sum, min_cal)
                continue 
            
            for i in range(1,4):
                next_r = r
                next_c = c
                if c + i > 2:
                    next_r += 1
                    next_c = (c+i)%3
                else:
                    next_c += i
                print(r,c ,next_r, next_c)
                if next_r == len(diet):
                    continue
                temp_sum = cur_sum + diet[next_r][next_c]
                if 0 == cal_sum[next_r][next_c]:
                    cal_sum[next_r][next_c] = temp_sum
                    end.append([next_r, next_c])
                elif 0 != cal_sum[next_r][next_c] and temp_sum < cal_sum[next_r][next_c]:
                    cal_sum[next_r][next_c] = temp_sum
                    end.append([next_r, next_c])
        
        start = end
        end = []

def DFS(diet, cal_sum, r, c):
    cur_sum = cal_sum[r][c]
    global min_cal

    if min_cal < cur_sum:
        return
    if r == len(diet)-1:
        min_cal = min(cur_sum, min_cal)
        return 

    for i in range(1,4):
        next_r = r
        next_c = c
        if c + i > 2:
            next_r += 1
            next_c = (c+i)%3
        else:
            next_c += i
        # print(r,c ,next_r, next_c)
        if next_r == len(diet):
            continue
        temp_sum = cur_sum + diet[next_r][next_c]
        if 0 == cal_sum[next_r][next_c]:
            cal_sum[next_r][next_c] = temp_sum
            DFS(diet, cal_sum, next_r, next_c)
        elif 0 != cal_sum[next_r][next_c] and temp_sum < cal_sum[next_r][next_c]:
            cal_sum[next_r][next_c] = temp_sum
            DFS(diet, cal_sum, next_r, next_c)
        elif 0 != cal_sum[next_r][next_c] and temp_sum > cal_sum[next_r][next_c]:
            continue


if __name__ =="__main__":
    solution([ [360, 138, 338], [230, 102, 311], [320, 474, 214], [131, 498, 484], [366, 176, 249], [323, 407, 116], [265, 433, 317] ])
    