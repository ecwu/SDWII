# Zhenghao Wu l630003054


def abs(original):  # custom function return absolute value
    if original >= 0:
        return original
    else:
        return -original


if __name__ == '__main__':
    user_input = float(input("Enter a floating-point number:"))
    print("The absolute value of %f is %f" % (user_input, abs(user_input)))
