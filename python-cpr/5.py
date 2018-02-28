# Zhenghao Wu l630003054

def array_abs(input_array):
    for i in range(len(input_array)):
       input_array[i] = abs(input_array[i])


if __name__ == '__main__':
    input_array = []
    for i in range(5):
        input_array.append(float(input("Enter a floating point number: ")))
    array_abs(input_array)

    for i in input_array:
        print("%f" % i, end=" ")
    print("\n")
