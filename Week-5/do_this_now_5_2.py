"""
Given the existing dictionary:
name_to_age = {"Bill": 21, "Jane": 4, "Jack": 56}

Write code to prompt the user for a name and age, add these to the dictionary, then display all of the data nicely. Sample:

Name: Mario
Age: 34
Jack		-	 56
Bill 	-	 21
Mario 	-	 34
Jane 	-	  4


"""

name_to_age = {"Bill": 21, "Jane": 34, "Sven": 56}
user_input_name = input("Please enter a name: ")
user_input_age = int(input("Please enter an age: "))
name_to_age.update( { user_input_name: user_input_age} )
for name, age in name_to_age.items():
    print("{:12} - {:8}".format(name, age))
