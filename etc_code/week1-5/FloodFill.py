def solution(n, m, image):
    answer = 0
    max_r = n
    max_c = m

    for start_r in range(max_r):
        for start_c in range(max_c):
            color = image[start_r][start_c]
            if color == 0:
                continue
            start = [[start_r,start_c]]
            # print("start",start)
            end = []
            while len(start) != 0:
                end = []
                for r,c in start:
                    if r+1 < max_r and image[r+1][c] == color:
                        end.append([r+1,c])
                        image[r+1][c] = 0
                    if c+1 < max_c and image[r][c+1] == color:
                        end.append([r,c+1])
                        image[r][c+1] = 0
                    if r-1 >= 0 and image[r-1][c] == color:
                        end.append([r-1,c])
                        image[r-1][c] = 0
                    if c-1 >= 0 and image[r][c-1] == color:
                        end.append([r,c-1])
                        image[r][c-1] = 0
                
                start = end
    
            answer += 1
    
    return answer

        


if __name__ == "__main__":
    print(solution(2,3,[[1, 2, 3], [3, 2, 1]]))