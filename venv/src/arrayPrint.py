def array_print(array):
    out = [str(elem) for elem in array]
    out = ' '.join(out)
    print(out)

if __name__ == '__main__':
    array = [int(elem) for elem in input().strip().split()]
    res = array[::-1]
    array_print(res)