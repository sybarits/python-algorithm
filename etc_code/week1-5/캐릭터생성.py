from collections import deque

def solution(n, record):
    answer = []
    characters = [deque() for _ in range(n+1)]
    # print(characters)
    for re in record:
        a = re.split()
        i = int(a[0])
        character = a[1]
        if character in characters[i]:
            continue
        if len(characters[i]) == 5:
            characters[i].popleft()
        characters[i].append(character)
    # print(characters)
    for c in characters:
        answer += list(c)
    # print(answer)
    return answer


if __name__ == "__main__":
    solution(1, ["1 fracta", "1 sina","1 hana","1 robel","1 abc", "1 sina", "1 lynn"])
    solution(4, ["1 a","1 b","1 abc","3 b","3 a","1 abcd","1 abc","1 aaa","1 a","1 z","1 q", "3 k", "3 q", "3 z", "3 m", "3 b"])