def count_boolean(b1, b2, b3) :
    a = [b1, b2, b3]
    count = 0
    i = 0
    for i in a :
        if i == "True" :
            count += 1
        i += 1
    if count >= 2:
        return True
    else :
        return False
