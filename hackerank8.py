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

