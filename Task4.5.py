def remember_result(func):
    #remember previous result and retrieve it
    with open("previous_result.txt", 'r') as g:
        try:
            previous_result = g.readlines()
        except:
            previous_result = []

    def wrapper(*args):
        if len(previous_result) == 0:
            print("Last result = ", None)
        else:
            print("Last result = ", previous_result[0])

        with open("previous_result.txt", "w") as g:
            g.write(func(*args))


        return func

    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        if isinstance(item, str):
            result += item
        else:
            result = 0
            for item in args:
                result += item
    result = str(result)
    print(f"Current result = '{result}'")
    return result
sum_list("a", "b")