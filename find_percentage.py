def calculate_percentage(ar):
    return sum(ar) / len(ar)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        tem = input().split()
        name = tem[0]
        scores = [float(i) for i in tem[1:]]
        student_marks[name] = scores
    query_name = input()
    print("%.2f" % calculate_percentage(student_marks[query_name]))