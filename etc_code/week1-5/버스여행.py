def solution(n,signs):
    answer = []
    ll = [[] for _ in range(n)]
    
    for a in range(len(signs)):
        for b in range(len(signs[a])):
            if signs[a][b] == 1:
                ll[a].append(b)
    

    # print(ll)
    for start in range(n):
        mid = [start]
        end = []
        cnt = 0
        while len(mid) != 0:

            end = []
            for m in mid:
                for e in ll[m]:
                    signs[start][e] = 1
                    if not e in end:
                        end.append(e)
                    if not e in ll[start]:
                        ll[start].append(e)

            mid = end
            print("mid", mid)
            print("signs", signs)
            print("pass", start, cnt)
            cnt += 1
            if cnt == n*2 or len(mid) > n*2:
                break
    # print(signs)
    answer = signs
    return answer


if __name__ == "__main__":
    print(solution(3, [[0,1,0],[0,0,1],[1,0,0]]))

    # print(solution(3, [[0,0,1],[0,0,1],[0,1,0]]))