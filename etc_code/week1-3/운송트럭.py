def solution(max_weight, specs, names):
    answer = 1
    temp_weight = 0
    spec_dict = dict(specs)

    for p in names:
        if temp_weight + int(spec_dict[p]) > max_weight:
            temp_weight = int(spec_dict[p])
            answer += 1
        else:
            temp_weight += int(spec_dict[p])

    return answer

if __name__ == "__main__":
    solution(300, [["toy","70"], ["snack", "200"]], ["toy", "snack", "snack"])
    solution(200, [["toy","70"], ["snack", "200"]], ["toy", "snack", "toy"])