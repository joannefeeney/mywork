# test program

def collatz(n):
    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(1, end='')

if __name__ == '__main__':
    n = int(input("Enter a positive integer: "))
    collatz(n)
    