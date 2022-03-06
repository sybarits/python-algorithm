#!/usr/bin/python3
def solution(seat):
    seat_set = set([str(r)+str(c) for r,c in seat])
    return len(seat_set)


if __name__ == "__main__":
    # print("result",solution([[1,1],[2,2],[3,3]]))
    print("result",solution([[1,1],[2,1],[1,2],[3,4],[2,1],[2,1]]))