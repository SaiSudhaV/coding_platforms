def second_last(students):
    scores = set([i[1] for i in students])
    tem, res = sorted(scores)[1], []
    for key, value in students:
        if value == tem:
            res.append(key)
    return "\n".join(i for i in sorted(res))

if __name__ == '__main__':
    students = []
    t = int(input())
    for _ in range(t):
        name = input()
        score = float(input())
        students.append([name, score])
    print(second_last(students))
