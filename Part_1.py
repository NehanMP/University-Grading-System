# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.    
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20220606
# Date: 20/03/2023

def Get_Histogram():
    print()
    print("---------------------------------------------------------------------------")
    print("Histogram")
                                            
    print("Progress  ", progress_c, ":", asterisk_p)
    print("Treailer  ", trailer_c, ":", asterisk_t)
    print("Retriever ", retriever_c, ":", asterisk_r)
    print("Excluded  ", excluded_c, ":", asterisk_e)                       
    print()
                    
    print(total_c, "outcomes in total.")
    print("---------------------------------------------------------------------------")

# Assigning variables
pass_m = 0
defer_m = 0
fail_m = 0

progress_c = 0
trailer_c = 0
retriever_c = 0
excluded_c = 0

asterisk_p = ""
asterisk_t = ""
asterisk_e = ""
asterisk_r = ""

total_c = 0
total_m = 0
val_marks = [0, 20, 40, 60, 80, 100, 120]

end_program = False
valid_int = False
new_mark = False


while True:
    while end_program == False:
        
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
        total_m = pass_m + defer_m + fail_m
        if total_m != 120:
            print("Total incorrect")
        else:
            break

    # Printing the progression outcomes
    if pass_m == 120:
        print()
        print("Progress")
        
        progress_c = progress_c + 1  # Getting the count of each progress student    
        asterisk_p += "*"
        
    elif pass_m == 100:
        print()
        print("Progress (module trailer)")
        
        trailer_c = trailer_c + 1  # Getting the count of each Trailer student
        asterisk_t += "*"

    elif (pass_m + defer_m) < fail_m:  
        print()
        print("Exclude")
        
        excluded_c = excluded_c + 1  # Getting the count of each Excluded student
        asterisk_e += "*"

    else:
        print()
        print("Do not progress - module retriever")
        
        retriever_c = retriever_c + 1  # Getting the count of each Retriever student
        asterisk_r += "*"

    total_c = retriever_c + excluded_c + trailer_c + progress_c     
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
        Get_Histogram()
        exit()


































    
