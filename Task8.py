def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num3:
        return num2
    else:
        return num3

print(max_num(6, 5, 2)) # 3