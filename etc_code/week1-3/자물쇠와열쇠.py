#!/usr/bin/python3

def solution(key, lock):
    answer = False

    lock_size = len(lock)
    key_size = len(key)

    if check_lock(key, lock):# 0
        return True
    
    key = rotate90(key)
    if check_lock(key, lock):# 90
        return True
    
    key = rotate90(key)
    if check_lock(key, lock):# 180
        return True
    
    key = rotate90(key)
    if check_lock(key, lock):# 270
        return True
    
    return False

def rotate90(m):
    m_size = len(m)
    new_m = [[0]*m_size for _ in range(m_size)]
    for i in range(m_size):
        for j in range(m_size):
            new_m[j][m_size-i-1] = m[i][j]
    
    return new_m


def get_new_key(key, lock, d_row, d_col):
    # d: shift size
    lock_size = len(lock)
    key_size = len(key)
    new_key = [[0]*lock_size for _ in range(lock_size)]
    for i in range(key_size):
        for j in range(key_size):
            new_row = i + d_row
            new_col = j + d_col
            if new_row >= 0 and new_row < lock_size and new_col >= 0 and new_col < lock_size:
                new_key[new_row][new_col] = key[i][j]

    return new_key

def check_lock(key,lock):
    lock_size = len(lock)
    key_size = len(key)
    good_key = False
    for i in range(-(key_size-1),lock_size):
        for j in range(-(key_size-1),lock_size):
            new_key = get_new_key(key, lock, i, j)
            good_key = True
            for k in range(lock_size):
                for l in range(lock_size):
                    if new_key[k][l] + lock[k][l] != 1:
                        good_key = False
                        break
                if not good_key:
                    break
            if good_key:
                break
        if good_key:
            break

    return good_key
    

if __name__ == "__main__":
    rotate90([[1,2,3],[4,5,6],[7,8,9]])

    lock = [[1,1,1],[0,0,0],[1,1,1]]
    key = [[1,1,1,1],[0,0,0,0],[1,0,0,1],[1,1,1,1]]
    print(get_new_key(key, lock, 0, 2))

    print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))