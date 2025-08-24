def cel_to_faren(temp_cel):
    fern = (temp_cel*9/5)+32
    return fern
def faren_to_cel(temp_fern):
    cel = (temp_fern-32)*5/9
    return cel
def cel_to_kel(temp_cel):
    kel = temp_cel+273
    return kel   
while True:
    print("______🌡️Main Menu🌡️_______")
    print("1.Convert Celcius -> Farenhite")
    print("2.Convert Farenhite -> Celcius")
    print("3.Convert Celcius -> Kelvin")
    print("4.Exit👋")
    choice = int(input("Choose Between (1-4)"))
    if choice == 4:
        print("Exiting program....👋")
        break
    elif choice == 1:
        celcius = int(input("Enter Celcius Temperature = "))
        Farenhite = cel_to_faren(celcius)
        print(f"{celcius} in Farenhite is = {Farenhite}")
    elif choice == 2:
        farenhite = int(input("Enter Farenhite Temperature = "))
        Celcius = faren_to_cel(farenhite)
        print(f"{farenhite} in Celcius is = {Celcius}")
    elif choice == 3:
        celcius = int(input("Enter Celcius Temperature = "))
        Kelvin = cel_to_kel(celcius)
        print(f"{celcius} is Kelvin is = {Kelvin}")    
    else:
        print("Invalid Choice, try again.")    