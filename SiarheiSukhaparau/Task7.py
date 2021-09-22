def foo(List):
    res_list = []
    x = 0
    prod = 1
    if len(List) == 1:
        res_list = [x]
    else:
        for i in List:
            List.pop(x)
            x += 1
            List.reverse()
            for j in List:
                prod = prod * j

            res_list.append(prod)
            prod = 1
            List.append(i)
            List.reverse()
    return res_list





print(foo([3, 2]))