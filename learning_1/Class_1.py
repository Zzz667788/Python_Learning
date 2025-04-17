# ask user for their name
name = input("what's your name ?")

#remove whitespace from str and capitalize user's name
name = name.strip().title()

#
first_name,last_name = name.split(" ")

#say hello to user
print(f"hello,{name}")

