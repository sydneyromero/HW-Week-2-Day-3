def circum():
    while True:
        #Prompt the User
        cir_question = input("\n\nHow would you like to find the circumference of a circle?\n\nTo use the diamater measurement, enter 'D'\n\nTo use the radius measurement, enter 'R'\n\nTo quit, enter 'Q'\n\n")

        #Option: Quit the App
        if cir_question.strip().lower() == "q":
            
            #quit_application                
                            
            print ("If you need to restart this application again, please type the command below and hit enter\npython q2.py\n\n")
            break
            
        #Option: Calculate with radius
        elif cir_question.strip().lower() == "r":
            
               
            r_size = input("What is the radius?\n\n")
            r_float = float(r_size)
            c_float = 2 * 3.14 * r_float
            print (f"The circumfurence is {c_float}")


        #Option: Calculate with diamater
        elif cir_question.strip().lower() == "d":
            
            d_size = input("What is the diameter?\n\n")
            d_float = float(d_size)
            c2_float = 3.14 * d_float                 
            print (f"The circumfurence is {c2_float}")

        #Not Valid User Input    
        else:
            print ("That is not a valid answer. Please try again.\n")


