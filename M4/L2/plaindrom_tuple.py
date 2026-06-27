tuple_original = (1,2,3,3,2,1)
print(tuple_original)
list_original = list(tuple_original)
reverse_list = list_original[::-1]
reverse_tuple = tuple(reverse_list)
print(reverse_tuple)
if list_original == reverse_list:
    print('This Tuple is a pallindrom ')

else:
    print('This Tuple is not a pallindrom')    

