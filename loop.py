def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


# using while loop  
# starting = 0
even_numbers = []
limit = int(input("Enter the limit: "))
# while starting <= limit:
#     if is_even(starting):
#        even_numbers.append(starting)
#     starting+=1


# for loop
for num in range(0 ,limit+1):
    if is_even(num):
        even_numbers.append(num)
    

print(f"Even numbers: {even_numbers}")


grocery_list = ['apple', 'lemon', 'lime', 'ginger', 'oat', 'soya']

for item in grocery_list:
    # if item == 'lemon': #skip the intended item from the list
    #     continue
    # print(item)

    if item == 'oat': #break before the intended item 
        break
    # print(item)


# printing the grocery items using for loop 
for i in range(0, len(grocery_list)):
    print(f"{grocery_list[i]} at index {i}")
print("Program end")