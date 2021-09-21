def replace_quotes(str_):

    list_from_str = []
    for i in str_:
        if i == "\"":
            list_from_str.append('\'')
        elif i == "\'":
            list_from_str.append('\"')
        else:
            list_from_str.append(i)
    new_str_ = ''.join(list_from_str)
    print(new_str_)
    print(list_from_str)


replace_quotes("hello\'\"")
