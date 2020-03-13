def main():
    flag = 0
    print("Enter target value.")
    target_val = int(input())
    print("Enter number of input.")
    size = int(input())
    list = []
    print("Enter sequence of numbers.")
    for index in range(0, size):
        val = int(input())
        list.append(val)
    for index in list:
        for index1 in list:
            if index-index1 == target_val:
                flag = 1
                break
    if flag == 1:
        print("Target achieved.")
    else:
        print("Target not achieved.")


if __name__ == "__main__":
    main()
