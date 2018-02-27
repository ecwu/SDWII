# Zhenghao Wu l630003054

if __name__ == '__main__':
    a = int(input("Enter the first integer:"))
    b = int(input("Enter the second integer"))  # Read two integer
    if (a >= 0) and (b >= 0):  # If both integer are positive
        print("The integers " + str(a) + " and " + str(b) + " are both positive")
    else:
        print("The integers " + str(a) + " and " + str(b) + " are not both positive")
