inp_string = input("enter a string:")
first_char = inp_string[0]
modified_string = first_char + inp_string[1:].replace(first_char,'$')
print("modified string:",modified_string)
