import math

n = int(input("Enter n: "))

if not (
    math.sqrt(5 * n**2 + 4).is_integer()
    or math.sqrt(5 * n**2 - 4).is_integer()
):
    print(-1)
else:
    a = 0
    b = 1
    pos = 3

    if n == a:
        print(1)
    elif n == b:
        print(2)
    else:
        while True:
            temp = a
            a = b
            b = a + temp
            if n == b:
                print(pos)
                break
            else:
                pos += 1
