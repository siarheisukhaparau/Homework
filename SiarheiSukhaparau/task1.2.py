def count_frequence(string):
    a_dict = {}
    for i in string:
        i = i.lower()
        if i not in a_dict:
            a_dict[i] = 1
        elif i in a_dict:
            a_dict[i] += 1
    return  a_dict
print(count_frequence("Oh, it is python"))


