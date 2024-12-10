def raise_to_power(base, exponent):
    result = 1
    print(type(range(exponent)))
    for i in range(exponent):
        result *= base
    return result

print(raise_to_power(2, 3))  # 8

