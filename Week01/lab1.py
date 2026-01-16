# Sample Coding Question 01 Week 01 
# Mehmet Emin Onem 

#Question 2 defining an array (list)

magic_array = [1 , 3 , 4 , 9 ]

#Question 3: Order of Operations 

a = 1 
b = 2
c = 3
d = 4 

# fully bracketed version of the expression 

e = (a - ((b ** c) // d)) + (a % c)

# The final value of e is 0

print(f"the value of e is {e}")

# Question 4: String formatting
# Create a variable called “temperature” with the value 32.6. Then, print the following
#sentence by using the variable and the format function, with 1 line of code.“The temperature
#today is: 32.600 degrees Celsius

temperature = 32.6
print(f"The temperature today is : {temperature:.3f} degrees celcius")

#Question 5: User Input

userAge = int(input("Enter your age: "))
userAge = userAge + 22

print (f"Now showing the shop items filtred by age {userAge}")
