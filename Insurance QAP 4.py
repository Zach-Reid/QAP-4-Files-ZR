#QAP Project 4
#By Zachary Reid
#Program function: To calculate insurance information based on inputs.

from datetime import date, timedelta

#Default Values

NEXTPOLICY = 1944

BASICPREMIUM = 869.00

CARDISCOUNT = 0.25

LIABILITYCOVERAGE = 130.00

GLASSCOVERAGE = 86.00

LOANERCOVERAGE = 58.00

HSTRATE = 0.15

PROCESSINGFEE = 39.99

downpayment = 0

claimvariable = 0
#Lists

provlist = ['ALBERTA', 'AB', 'BRITISH COLUMBIA', 'BC', 'MANITOBA', 'MB', 'NEW BRUNSWICK', 'NB', 'NEWFOUNDLAND & LABRADOR', 'NL', 'NOVA SCOTIA', 'NS', 'ONTARIO', 'ON', 'PRINCE EDWARD ISLAND', 'PE', 'QUEBEC', 'QC', 'SASKATCHEWAN', 'SK']

paytypes = ['Down Pay', 'Full', 'Monthly']

claimlist = []

#Functions

def listprovince():
    print(" ")
    print("List of accepted provinces:")
    print("Alberta - AB")
    print("British Columbia - BC")
    print("Manitoba - MB")
    print("New Brunswick - NB")
    print("Newfoundland & Labrador - NL")
    print("Nova Scotia - NS")
    print("Ontario - ON")
    print("Prince Edward Island - PE")
    print("Quebec - QC")
    print("Saskatchewan - SK")

def downpay():
    global downpayment
    while True:
        downpayment = int(input("Enter the down payment: "))
        if (downpayment) <= 0:
            print ("Down payment cannot be negative or zero.")
        else:
            break
    
    paytypes.remove ("Down Pay")
    while True:
        pay = input("Enter the customer's payment type for the remainder (Monthly or Full): ").title()
        if pay not in paytypes:
            print("Input is not a listed form of payment.")
        else:
            break

def claimloop():
    global claimvariable
    global claimnum
    global claimdate
    global claimsum
    while True:
        claimnum = input("Enter the claim number: ")
        if claimnum.isdigit() == False:
            print("Claim number cannot use letters, symbols, or spaces.")
        else:
            break

    while True:
        claimdate = input("Enter the date of the claim: ")
        if claimdate.isspace() == True:
            print("Claim date is invalid.")
        else:
            break

    while True:
        claimsum = input("Enter the claim amount: ")
        if claimsum.isdigit() == False:
            print("Claim amount cannot use letters, symbols, or spaces.")
        else:
            break
    
    claimlist.append(claimnum)
    claimlist.append(claimdate)
    claimlist.append(claimsum)

    claimvariable = claimvariable + 1










#User input
#Name

while True:
    namefirst = input("Enter the customer's first name: ").title()
    if namefirst.isalpha() == False:
        print("Name cannot be blank or use symbols/numbers.")
    else:
        break

while True:
    namelast = input("Enter the customer's last name: ").title()
    if namelast.isalpha() == False:
        print("Name cannot be blank or use symbols/numbers.")
    else:
        break

#Number

while True:
    phone = input("Enter the customer's phone number (10 digits): ")
    if phone.isdigit() == False:
        print("Number cannot use letters, symbols, or spaces.")
    elif len(phone) !=10:
        print("Number must use 10 digits.")
    else:
        break

#Address

while True:
    city = input("Enter the customer's city: ").title()
    if city.isspace() == True:
        print("Invalid input.")
    else:
        break

while True:
    address = input("Enter the customer's address: ").title()
    if address.isspace() == True:
        print("Invalid input.")
    else:
        break

while True:
    postal = input("Enter the customer's postal code: ").upper()
    if postal.isspace() == True:
        print("Invalid input.")
    else:
        break   

#Province

while True:
    province = input("Enter the customer's province (or help for a list of provinces): ").upper()
    if province == "HELP":
        listprovince()
    if province not in provlist:
        if province == "HELP":
            print("")
        else:
            print("Entered province is not a listed province.")
    else:
        break

#Car Options

while True:
        carcount = int(input("Enter the number of cars being ensured: "))
        if (carcount) <= 0:
            print ("You cannot ensure less than 1 car.")
        else:
            break

while True:
        liability= input("Do you want extra liability? (Y/N):").upper()
        if liability != "Y" and liability != "N":
            print("Invalid input.")
        else:
            break

while True:
        glass= input("Do you want glass coverage? (Y/N):").upper()
        if glass != "Y" and glass != "N":
            print("Invalid input.")
        else:
            break

while True:
        loan= input("Is the car a loaner car? (Y/N):").upper()
        if loan != "Y" and loan != "N":
            print("Invalid input.")
        else:
            break

#Select Payment Type
        
while True:
    pay = input("Enter the customer's payment type (Monthly, Full, Down Pay): ").title()
    if pay not in paytypes:
        print("Input is not a listed form of payment.")
    else:
        break

if pay == "Down Pay":
    downpay()

while True:
    loop = input("If the customer has one or more previous claims, type Y. If each previous claim has been documented, type N. ").upper()
    if loop == "Y":
        claimloop()
    elif loop != "N" and loop != "Y":
        print("Invalid input.")
    else:
        break


#Math
        
if carcount == 1:
    premium = BASICPREMIUM
else:
    carelse = carcount - 1
    premium = BASICPREMIUM * carelse * CARDISCOUNT + BASICPREMIUM

if liability == "Y":
    liabilitycost = LIABILITYCOVERAGE * carcount
else:
    liabilitycost = 0

if glass == "Y":
    glasscost = GLASSCOVERAGE * carcount
else:
    glasscost = 0

if loan == "Y":
    loancost = LOANERCOVERAGE * carcount
else:
    loancost = 0

totalextra = loancost + glasscost + liabilitycost

totalpremium = premium + totalextra

totaltax = totalpremium * HSTRATE

finalcost = totalpremium + totaltax

#Also the time is here

currentdate = date.today()
#And this one is for day one of next month

inputdt = date.today() 

inputdt = inputdt.replace(day=1)

inputdt = inputdt + timedelta(days=32)

inputdt = inputdt.replace(day=1)

if pay == "Monthly":
    monthpay = finalcost - downpayment + PROCESSINGFEE / 8

#Receipt time..
    
print("                                                                     ") #
print("---------+---------+---------+---------+---------+---------+---------") #
print("One Stop Insurance                           Invoice Date:", currentdate) #
print("Policy Information Program                        Policy Number:", NEXTPOLICY) #
print("---------+---------+---------+---------+---------+---------+---------") #
print("Customer Information:",        namefirst.rjust(46 - len(namelast)), namelast) #
print("Phone Number:",                str(phone).rjust(55)                )#
print("Customer's Address:",        address.rjust(48 - len(city)), city        ) #, maybe
print("Postal Code:",                (postal).rjust(56)                )#
print("Customer's Province:",                (province).rjust(48)                )#
print("Amount of Cars Being Ensured:",                str(carcount).rjust(39)                )#
print("---------+---------+---------+---------+---------+---------+---------") #
print("Extra Liability:    ", liability, "    Glass Coverage:    ", glass, "    Loaner car:   ", loan) #
print("Payment type:", pay.rjust(55))
print("Down Payment Amount:", str(downpayment).rjust(48))
print("---------+---------+---------+---------+---------+---------+---------") #
print("Cars ensured:", str(carcount).rjust(55)        ) #
print("Premium Cost:", str(premium).rjust(55)        ) #
print("---------+---------+---------+---------+---------+---------+---------") #
print("Liability Cost:", str(liabilitycost).rjust(53)        ) #
print("Glass Cost:", str(glasscost).rjust(57)        ) #
print("Loaner Cost:", str(loancost).rjust(56))
print("Total Extra Cost:", str(totalextra).rjust(51)        ) #
print("Extras & Premium:", str(premium).rjust(51)        ) #
print("Total with 15% HST:", str(totaltax).rjust(49)        ) #
print("Glass Cost:", str(glasscost).rjust(57)        ) #
print("                                                                     ") #
print("Total Cost:", str(finalcost).rjust(57)        ) #
print("---------+---------+---------+---------+---------+---------+---------") #
if pay == "Monthly":
    print("Monthly Payment:", str(monthpay).rjust(52) ) #
    print("Payment duration:                                            8 Months")
    print("First Payment:                                            ", inputdt)

#The Final Stretch: The claimlist
if claimvariable >=0:    
    print("Claim #  Claim Date   Amount")
    print("----------------------------")
    for x in range(claimvariable):
        print(claimlist[0:3])
        claimlist.pop(0)
        claimlist.pop(0)
        claimlist.pop(0)
