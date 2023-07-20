def has_noble_integers(nums_array: list) -> int:
    nums_array.sort(reverse=True)
    for index in range(len(nums_array)):
        if index == nums_array[index]:
            return 1
    return -1


try:
    num_array = list(map(int, input("Enter integers separated by space : ").split()))
    print("The output array is : ", has_noble_integers(num_array))
except ValueError:
    print("Invalid Input, Please enter only integer")
