def foo(n):
    if n > 0:
        return n
    else:
        return foo(n + 1)

if __name__ == '__main__':
    foo(-5)