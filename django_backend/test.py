for i in range(1, 10):
    for j in range(1, i):
        if i % j == 0:
            continue

        def myfunc(n):
            """Return lamda function."""
            return lambda a: a + n
        mydoubler = myfunc(i)
        print(mydoubler(j))
