def split_by_index(s: str, indexes):
    sub_str_ = str()
    sub_list = []
    j = 0
    indexes.sort()
    for i in indexes:
        if 0 <= i < len(s):
            sub_str_ = s[j:i]
            j = i
            sub_list.append(sub_str_)
    sub_list.append(s[j:])
    return sub_list
print(split_by_index("pythoniscool,isn'tit?", [-1, 2, 12, 15, 17,56, 25]))
print(split_by_index("pythoniscool,isn'tit?", [0]))