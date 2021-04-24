def circularArrayRotation(a, k, queries):
    a = a[-k:] + a[:-k]
    return "\n".join(str(a[i]) for i in queries)

if _name_ == '_main_':
    n, k, q = map(int, input().split())
    a = list(map(int, input().rstrip().split()))
    queries = []
    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k % len(a), queries)
    print(result)
