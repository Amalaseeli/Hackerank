''' Input Format

The first line contains an integer, , denoting the number of entries in the phone book.
Each of the  subsequent lines describes an entry in the form of  space-separated values on a single line. The first value is a friend's name, and the second value is an -digit phone number.

After the  lines of phone book entries, there are an unknown number of lines of queries. Each line (query) contains a  to look up, and you must continue reading lines until there is no more input.

Note: Names consist of lowercase English alphabetic letters and are first names only.'''
n=int(input())
phonebook={}
for i in range(n):
    book=input()
    (k,v)=book.split()
    phonebook[k]=v
# for (k,v) in phonebook.items():
#     print(k,v)

try:
    while True:
        test=str(input())
        if test in phonebook.keys():
            
            print(test+ "="+ str(phonebook[test]))
        else:
            print("Not found")
except EOFError as e:
    print(end="")

