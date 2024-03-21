print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("> > > > > > > > > > > > > > > > > > EXPENSE TRACKER < < < < < < < < < < < < < < < < < < ")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

CB  = 0
dict = {}
i_amt = 0
o_amt =0
q = 4
while True:
        
    print("\n")
    print("PRESS 1 : INITIAL AMOUUNT")
    print("PRESS 2 : ADD ADDITIONAL AMOUNT")
    print("PRESS 3 : VIEW INITIAL AND CURRENT AMOUNT")
    print("PRESS 4 : ADD EXPENSE AMOUNT AND NAME")
    print("PRESS 5 : EDIT EXPENSE AMOUNT")
    print("PRESS 6 : EDIT EXPENSE NAME")
    print("PRESS 7 : DELETE EXPENSE")
    print("PRESS 8 : EXIT")

    print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

    try:
        print("\n")
        choice = int(input("ENTER YOUR CHOICE :"))
        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    except ValueError:
        print("\nOOPS..!!! ENTER A DIGIT")
    
    if choice == 1:

        print("\n- - - - - - - - - - - - - - - - - ADD INITIAL AMOUNT - - - - - - - - - - - - - - - - - -")
        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        if i_amt == 0:

            try:
                amt = int(input("\nENTER THE AMOUNT :"))
                o_amt += amt
                CB=amt

            except:
                print("\nOOPS..!!! ENTER A DIGIT")
                print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
            else:
                i_amt += amt
                V = i_amt
                print("\nAMOUNT ADDED SUCCESSFULLY")
                print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

        else:
            if i_amt >=0:
            
                print("\nAMOUNT ALREADY ENTERED..!!!")
                print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    elif choice == 2:

        print("\n- - - - - - - - - - - - - - - - ADD ADDITIONAL AMOUNT - - - - - - - - - - - - - - - - -")
        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

        try:
            amt2 = int(input("\nENTER THE AMOUNT :"))
            o_amt += amt2
        except:
            print("\nOOPS..!!!ENTER IN DIGITS")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        else:
            i_amt +=amt2
            V = i_amt
            print("\nAMOUNT ADDED SUCCESSFULLY")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

    

    elif choice == 4:
        if i_amt<=0:
            print("\nADD INITIAL AMOUNT..!!!")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

        else:
        
            name =  input("\nENTER THE EXPENSSE NAME :")
            if name not in dict:
                try:
                    exp_amt = int(input("\nENTER THE AMOUNT :"))
                except:
                    print("\nOOPS..!!!ENTER THE DIGIT")
                    print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
                else:
                    if CB - exp_amt<=0:
                        print("\nINSUFFICIENT BALANCE..!!!")
                        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
                    else:
                        # exp_amt <= i_amt
                        dict[name] = exp_amt
                        print(f"\nAMOUNT ADDED SUCCESSFULLY")
                        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

            else:
                R = dict[name]
                del dict[name]
                value1 = int(input("\nENTER THE AMOUNT :"))
                W = R + value1
                if CB - exp_amt<=0:
                    print("\nINSUFFICIENT BALANCE..!!!")
                    print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
                else:
                    dict[name] = W                        
    
    elif choice == 3:
        
        
        
        print("\n- - - - - - - - - - - -- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        print("\n- - - - - - - - - - - -- - - - - - VIEW EXPENSES - - - - - - - - - - - - - - - - - - -")
        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        print("\n")
        print("INITIAL AMOUNT =",V)
        print("\n")
        if V <=0:
            print()
        else:
            for name,exp_amt in dict.items():
                print(name,exp_amt)

            v = 0
            for q in dict.values():
                v =v+q
            
            print()
            print("\nTOTAL EXPENSES ",v)
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
            CB = V - sum(dict.values())
            if (CB<=0):
                print("\nINSUFFICIENT BALANCE..!!!")
            else:
                print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ") 
                print("\nCURRENT BALANCE =",CB)
                print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
            

    elif choice == 5:
        
        print("\n- - - - - - - - - - - - - - - - - EDIT EXPENSE AMOUNT - - - - - - - - - - - - - - - - -")
        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        y = input("\nENTER THE EXISTING NAME :")
        if y in dict:
            try:
                new_amt = int(input("\nENTER TEH NEW AMOUNT :"))
                dict.update({y:new_amt})   
            except:
                print("\nOOPS..!!!ENTER THE DIGIT")
                print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
            else:    
                if new_amt < V:
                    print("\nINSUFFICIENT BALANCE..!!!")
                    print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
                else:
                    print("\nUPDATED SUCCESSFULLY")
                    print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        else:
            print("\nEXPENSE NAME NOT FOUND..!!!")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

    elif choice == 6:
        
        print("\n- - - - - - - - - - - - - - - - - EDIT EXPENSE NAME - - - - - - - - - - - - - - - - - -")
        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

        z = input("\nENTER THE EXISTING NAME: ")
        if z in dict:
            j = input("\nENTER THE NEW NAME: ")
            if j in dict:
                dict[j] += dict[z]
            else:
                dict[j] = dict[z]
            del dict[z]
            print("\nUPDATED SUCCESSFULLY")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
           
        else:
            print("\nEXPENSE NAME NOT FOUND..!!!")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")


    elif choice == 7:
        print("\n- - - - - - - - - - - - - - - - - - DELETE EXPENSES - - - - - - - - - - - - - - - - - - -")

        M = input("\nENTER THE EXISTING NAME :")

        if M in dict:
            dict.pop(M)
            print("\nDELETED SUCCESSFULLY")
            print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

    elif choice == 8:

        print("\n> > > > > > > > > > > > > > > > > > > > EXITED < < < < < < < < < < < < < < < < < < < < ")
        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        exit()
        
    
    elif choice >8:

        print("\nWRONG CHOICE..!!!!")
        print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")