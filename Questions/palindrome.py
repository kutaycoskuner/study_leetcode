def Main():
    # ==== test
    x = 1991

    # ==== logic
    mapping = list(str(x))
    for ii in range(0, len(mapping)):
        if mapping[ii] != mapping[len(mapping)-ii-1]:
            break
        if ii+2 >= len(mapping)-ii-1:
            print('true')
            return True
    print('false')
    return False

    # print(len(mapping))
    # for ii in range(0, len(nums)):


# ==== Main
if __name__ == "__main__":
    Main()