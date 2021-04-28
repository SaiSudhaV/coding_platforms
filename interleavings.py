def generate_interleaving(a, b, res, tem):
    if not a and not b:
        res.append(tem)
        return sorted(res)
    if a:
        res = generate_interleaving(a[1:], b, res, tem + a[0])
    if b:
        res = generate_interleaving(a, b[1:], res, tem + b[0])
    return sorted(res)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b = input().split()
        n = len(a) + len(b)
        print("Case #%d:" % (i + 1))
        print("\n".join(generate_interleaving(a, b, [], "")))