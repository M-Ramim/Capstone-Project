"""
Lists
Student Project
Project Title:
"""

print("Sign In For ClubFinder".center(115))
###-- Names and student id's of the loged in student
    ##--Storing the student's first and last name
student_name = ["mohammad ramim", "bailey wu", "chance powell", "angela anthony", "eileen knapp"] 

    ##--Storing the student ID  
student_id = [10033355, 11048355, 10048895, 18903355, 14438895]

logged_in = False

while not logged_in:
    student = input("Would you like to Login or Signup? ").lower()
    ##-- Checking if the user is loging in or signing up 
    if student == "login":
        while True:
            names = input("Enter your first and last name: ").lower()
            collect_id = int(input("Enter your ID numbers: "))
            
            ##--This is checking wheather the name and the id matches or not.
            if names in student_name and collect_id in student_id:
                index = student_name.index(names)
                if student_id[index] == collect_id:
                    print("Login successful!")
                    logged_in = True
                    break
            ##--this will print out if the ID or name does not match                              
            else:
                print("Incorrect name or ID. Please try again.")
            
    
                             
                             
                             
    ##--This is when the user wants to signup    
    elif student == "signup":
        ##--new variable input to collect the new name and ID
        new_name = input("Enter your first and last name: ").lower()
        new_id = int(input("Enter your ID number: "))
        
        ##--this is to check if the user id and name are in the list
        if new_name in student_name or new_id in student_id:
            print("The ID or the Student name already exist")
        else:
            print("Signup successful!")
            student_name.append(new_name)
            student_id.append(new_id)
            continue
        
        
        
    else:
        print("Please enter 'login' or 'signup'")
        
            







