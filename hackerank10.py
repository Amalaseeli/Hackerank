''' Task
Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation. When working with different bases, it is common to show the base as a subscript.

Example

The binary representation of  is . In base , there are  and  consecutive ones in two groups. Print the maximum, .

Input Format

A single integer, .

Print a single base- integer that denotes the maximum number of consecutive 's in the binary representation of .
'''
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
    
