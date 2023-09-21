values = [0, 2, 10, 6]


def same_by(characteristic, objects):
    values = list(map(characteristic, objects))

    for i in range(1, len(values)):
        if values[i] != values[i - 1]:
            return False
    return True


if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
