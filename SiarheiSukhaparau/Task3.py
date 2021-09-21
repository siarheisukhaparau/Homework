def sep_str_(str_, sep_char):

    new_str_ = str()
    ind_sep_char = str_.find(sep_char)
    list_from_str = []
    if ind_sep_char >= 0:
        if ind_sep_char > 0:
            new_str_ = str_[0:ind_sep_char]
        list_from_str.append(new_str_)
        list_from_str.extend(sep_str_(str_[ind_sep_char+len(sep_char):len(str_)], sep_char))
    else:
        list_from_str.append(str_)
    return list_from_str


print(sep_str_(", masha, kasha, ", ", "))
