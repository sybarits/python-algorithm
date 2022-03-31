def solution(letters):
    answer = []
    s = set()
    len_l = len(letters)
    l = ""
    step = 0
    DFS(letters, l, s, step, len_l)
    answer = list(s)
    answer.sort()
    print(answer)
    return answer

def DFS(letters, l, s, step, len_l):
    # print(letters, step, l)
    if step == len_l:
        if len(l) == len_l:
            return s.add(l)
        else:
            return
    for i in range(len(letters)):
        if len(l) == 0 or l[-1] != letters[i]:
            DFS(letters[0:i] + letters[i+1:], l+letters[i], s, step + 1, len_l)
    


if __name__ == "__main__":
    solution("abca")
    solution("abcbc")
    solution("wxyz")

    # l = "ab"
    # print(l[0:1] + l[2:])