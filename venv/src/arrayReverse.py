def array_print(array):
    out = [str(elem) for elem in array]
    print(out)

if __name__ == '__main__':
    array = [int(elem) for elem in input().strip().split()]
    array = array[::-1]
    array_print(array)