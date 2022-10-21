''' Task
Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
Enter_num_of_string=int(input())
for i in range(0,Enter_num_of_string):
    str1=input()
    even_string=""
    odd_string=""
    for i in range(0,len(str1)):
        if i % 2 == 0:
            even_string+=str1[i]
        else:
            odd_string+=str1[i]
    print(even_string,odd_string)