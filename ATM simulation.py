username="morgan"
password="123"

#prompting user to enter password
entry=input("enter password :")

#equating enter password to the correct one
if entry == password:
 print("you are in")

#prompting the user to renter
elif entry!=password:

    k=1
    while k<3:
        k=k+1
        rentry = input("Re enter password :")

        if rentry==password:
            print("you are in")


    else:
        print("==This card is blocked==")
