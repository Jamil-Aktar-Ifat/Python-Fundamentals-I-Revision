marks = int(input("Enter you marks: "))

def show_result(grade):
    print(f"You got {grade}! ")

if marks >= 80:
    show_result("A*")
elif marks < 80 and marks >= 70:
    show_result("A")
elif marks < 70 and marks >= 60:
    show_result("A-")
elif marks > 40:
    show_result('Passed')
else:
    show_result("Failed")



# boolean conditions
this_is_a_good_number = marks >=80
print(this_is_a_good_number)

if(this_is_a_good_number):
    print("Inside if")
else:
    print("Inside else")