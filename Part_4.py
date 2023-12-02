# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.    
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20220606
# Date: 20/03/2023


# Assigning variables
pass_m = 0
defer_m = 0
fail_m = 0

val_marks = [0, 20, 40, 60, 80, 100, 120]

end_program = False
valid_int = False
new_mark = False

marks = []
outcome_dict = {}
inputs_dict = {}


while True:
    while end_program == False:
        
    # Getting user Id
        while valid_int == False:
            try:
                Id = str(input("Please enter your ID: "))
                print()
                if Id == "":
                    pass
                else:
                    break
            except IndexError:
                print("Please enter a valid Id number.")
            
        
    # Getting value for the the pass mark while looping until all credits are entered       
        while valid_int == False:
            try:                
                pass_m = int(input("Please enter your credits of pass: ")) # Get pass credits
                if pass_m not in val_marks:
                    print("Out of range")
                else:
                    break
            except ValueError:    # If non int value is given
                print("Integer required")
                

       # Getting value for the the defer mark while looping until all credits are entered        
        while valid_int == False:
            try:
                defer_m = int(input("Please enter your credits of defer: ")) # Get defer credits           
                if defer_m not in val_marks:
                    print("Out of range")
                else:
                    break
            except ValueError:    # If non int value is given
                print("Integer required")


       # Getting value for the the fail mark while looping until all credits are entered 
        while valid_int == False:
            try:
                fail_m = int(input("Please enter your credits of fail: ")) # Get fail credits           
                if fail_m not in val_marks:
                    print("Out of range")
                else:
                    break
            except ValueError:    # If non int value is given
                print("Integer required")

       # Checking the validation of the total credit marks
        marks = [pass_m, defer_m, fail_m]
        if sum(marks) != 120:
            print()
            print("Total incorrect")
        else:
            break
        
        
    # Printing the progression outcomes
    if pass_m == 120:
        output = "Progress"
        
    elif pass_m == 100:
        output = "Progress (module trailer)"

    elif (pass_m + defer_m) < fail_m:  
        output = "Exclude"

    else:
        output = "Do not progress (module retriever)"


    # Storing the progression outcome to a dictionary
    outcome_dict[Id] = {
        'output': output,
        'marks': [pass_m, defer_m, fail_m]
    }

    inputs_dict[Id] = [pass_m, defer_m, fail_m]

    print()
    print("Would you like to enter another set of data?")
    
        
    while True:
        flow = input("Enter 'y' for yes or 'q' to quit and view results: ") # 'y' to continue the program and 'q' to ext the program and view the histogram
        try:
            if flow not in ['y', 'q']:                
                raise ValueError("Please enter 'y' or 'q' in order to proceed.")
            break  
        except ValueError as error:  # Looping the process until 'y' or 'q' is entered 
            print(error)

    if flow == "y":
        new_mark = True
        print()
        
    elif flow == "q":
        print()
        for Id, marks in inputs_dict.items():            
            print(f"{Id} : {output} - {marks[0]}, {marks[1]}, {marks[2]}")
        exit()
        
        


            
           
