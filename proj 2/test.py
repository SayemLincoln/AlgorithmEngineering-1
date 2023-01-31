#
#


if __name__ == '__main__':
    fp = open(input("Please Enter File Name: "), "r")
    list_ = []

    for num in fp:
        list_.append( float(num))
    list_ = sorted(list_)
    print(" -> ".join(map(str, list_)))
    fp.close()
