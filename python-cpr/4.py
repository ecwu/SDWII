# Zhenghao Wu l630003054

if __name__ == '__main__':
    number_amount = int(input("How many floating point numbers do you want to multiply together:"))
    sum = 1.0
    for i in range(number_amount):  # Ask for every float, and
        temp = float(input("Enter a floating point number:"))
        sum *= temp
    print("The product is: %f" % sum)
