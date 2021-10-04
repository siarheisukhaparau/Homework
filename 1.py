### Task 4.1
# Open file `data/unsorted_names.txt` in data folder. Sort
# the names and write them to a new file called `sorted_names.txt`.
# Each name should start with a new line as in the following example:


def sort_names():

    with open("/data/unsorted_names.txt", "r") as g:
        unsorted_names = g.readlines()
        unsorted_names.sort()
    with open("/data/sorted_names.txt", "w") as x:
        for name in unsorted_names:
            x.write(name)
sort_names()
