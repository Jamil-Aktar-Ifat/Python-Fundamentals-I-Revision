grocery_list = ['rice', 'potato', 'beef']

print(f"Before: {grocery_list}")

grocery_list.append('water')
print(f"After: {grocery_list}")



list_2 = list()
print(list_2)
list_2.append(4)
print(list_2)
list_2.append('computer')
print(list_2)


# indexing 
print(grocery_list[3])
print(grocery_list[-2])

# sorting
names = ['jamil', 'khan', 'aktar', 'ifat', 'rehan', 'tazbir']
print(f"Before sorting: {names}")
names.sort() # a way to sort 
print(f"After sorting: {names}")


numbers = [1, 10, 4, 6,2, 55, 28, 53, 11]
print(numbers)
sorted_numbers =  sorted(numbers) # another way to sort 
print(sorted_numbers)
