
def find_max_ones(num):
    if not num:
        return 0
    bin_num = bin(num)[2:]
    print(bin_num)
    return len(max(bin_num.replace('0', ' ').split()))


if __name__ == '__main__':
    num = int(input('Enter integer number:'))
    max_ones = find_max_ones(num)
    print("max 1's count is", max_ones)
    
