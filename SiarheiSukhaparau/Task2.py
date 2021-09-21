def check_palindrom(str_):

    new_str_ = str_[::-1]
    if new_str_ == str_:
        print("palindrom")
    else:
        print("not palindrom")


check_palindrom("aalllllla")
