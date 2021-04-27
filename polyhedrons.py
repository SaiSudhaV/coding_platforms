def polyhedrons(lst):
    total = 0
    for i in lst:
        if i == "Tetrahedron":
            total += 4
        elif i == "Cube":
            total += 6
        elif i == "Octahedron":
            total += 8
        elif i == "Dodecahedron":
            total += 12
            
        elif i == "Icosahedron":
            total += 20
    return total

if __name__ == "__main__":
    n = int(input())
    lst = []      
    for i in range(n):
        lst.append(str(input()))
        res = polyhedrons(lst)
        print(res)
