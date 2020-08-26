try:
    a,b = map(int,input().split())
    print(a/b)
except ValueError:
    print('Введите число')