def array_increment(array, x):
    for i in range(len(array)):
        array[i] += x

def array_print(array):
    out = [str(elem) for elem in array]
    out = ' '.join(out)
    print(out)

if __name__ == '__main__':
    array = [int(elem) for elem in input().strip().split()]
    x = int(input())
    array_increment(array, x)
    array_print(array)