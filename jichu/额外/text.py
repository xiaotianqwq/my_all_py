def swep(a, b):
    a,b=b,a
    print('swep  a=' + str(id(a)) + '   b=' + str(id(b)))


def main():
    a = 1
    b = 2
    print('main  a='+str(id(a))+'   b='+str(id(b)))
    print(f"a={a}   b={b}")
    swep(a,b)
    print(f"a={a}   b={b}")


if __name__ == '__main__':
    main()