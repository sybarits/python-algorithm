def first_solve():
    N = int(input())

    s = "moo"

    def moo(s, step):
        global N
        if len(s) >= N:
            return s
        
        s = s + "m"+ "o"*(step+2) + s
        return moo(s, step+1)

    s = moo(s,1)
    print(s[N-1])

def second_solve():
    N = int(input())

    if N==1:
        print("m")
        exit(0)
    elif N==2 or N == 3:
        print("o")
        exit(0)

    step = 0
    s_len = 3
    arr = [s_len]
    mid_len = 4
    while N > s_len:
        s_len = s_len*2 + mid_len
        mid_len += 1
        step += 1
        arr.append(s_len)
    # print("s_len", s_len, "step", step)
    # print(arr)

    n = N
    find_char(step, n, arr)

def find_char(step, n, arr):
    if n==1:
        print("m")
        exit(0)
    elif n==2 or n == 3:
        print("o")
        exit(0)

    if n <= arr[step-1]:
        find_char(step-1, n, arr)
    elif n == arr[step-1] + 1:
        print("m")
        exit(0)
    elif n > (arr[step-1]+step+3):
        find_char(step-1, n - (arr[step-1]+step+3), arr)
    else:
        print("o")
        exit(0)

if __name__ == "__main__":
    second_solve()
