def get_digits(num):

    list_ = list()
    for i in str(num):
        list_.append(int(i))
    tup_num = tuple(list_)
    print(tup_num)


get_digits(87178291199)
