def get_shortest_word(s):

    get_dict(s)
    res = str()
    c = 0
    for i in get_dict(s).keys():
        if len(i) > c:
            res = i
        c = len(res)
    return res


def get_dict(s):

    dict_ = dict()
    ind_sep = s.find(" ")
    if ind_sep > -1:
        key_dict = s[:ind_sep]
        value_dict_ = len(key_dict)
        dict_ = {key_dict: value_dict_}
        dict_.update(get_dict(s[ind_sep + 1:len(s)]).items())
    else:
        dict_[s] = len(s)
    return dict_


print(get_shortest_word('jop poop yu popa'))
