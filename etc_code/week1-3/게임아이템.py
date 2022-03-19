def solution(healths, items):
    answer = []
    healths.sort()

    for i in range(len(items)):
        items[i].append(i)
        
    items.sort(key = lambda x : -x[0])
    item_dic = {i : items[i] for i in range(len(items))}

    for i in range(len(healths)):
        for j, item in item_dic.items():
            if healths[i] - item[1] >= 100:
                answer.append(item[2]+1)
                del item_dic[j]
                break

    answer.sort()
    print("answer",answer)
    return answer


if __name__ == "__main__":
    solution([200,120,150], [[30,100],[500,30],[100,400]])
    # solution([300,200,500], [[1000,600],[400, 500],[300,100]])