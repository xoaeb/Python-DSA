def process_string(input_string):
    # Concatenate the string with itself
    concatenated = input_string + input_string
    
    # Use list comprehension to filter characters
    result = [char for char in concatenated if not (char.isupper() or char.lower() in 'aeiou')]
    
    # Return the result as a string
    return ''.join(result)

# Given string
a = 'asdLKJiiksJKKKoi'

# Call the function and print the result 
print(process_string(a))





#akash =(ajay +2), ajay+3  = abhishek , alice=   ajay +1
# asdfasdf
# a
# sortedsd
# finallysdf
# asdf
# asdf
def function():
    i = 0
    sum = 0
    while(i < 100):
        sum = sum + i
        sum = i + sum
        i += 1
    print(sum)
    
    
function()

a=100
b=2000
c=  a%b
print(c)