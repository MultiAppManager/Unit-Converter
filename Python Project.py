print("Unit Converter")
print("===============")

# ==== to choose type of conversion ====
def UnitConverter():
    unit_change = \
        {
            1: "Length",
            2: "Temperature",
            3: "Time",
            4: "Speed",
            5: "Energy",
        }

# ==== for getting number of type ====
    for keys, values in unit_change.items():
        print("{:2}. {}".format(keys, values))

    change = int(input("\nWhich type of conversion you want to do from 1 to 5:"))

    # ==== Type 1 (length) ====
    if change == 1:
        print(">>> You chose type Length")
        print("")
        length_dict = \
            {
                1: "Centimeter to KiloMetre",
                2: "KiloMetre to Centimeter",
                3: "Centimeter to FOOT",
                4: "Centimeter to Meter",
                5: "Meter to Centimeter",
            }

        # ==== for getting number of conversion ====
        print("==========================")
        length_value = float(input("- Enter a number to convert: "))
        for keys, values in length_dict.items():
            print("{:2}. {}".format(keys, values))
        length_convert = int(input("\nWhich conversion you want to do from 1 to 5: "))

        # ==== converting ====
        if length_convert == 1:
            print("{} cm is equal to {} km.".format(length_value, length_value / 100000))
        elif length_convert == 2:
            print("{} km is equal to {} cm.".format(length_value, length_value * 100000))
        elif length_convert == 3:
            print("{} cm is equal to {} feet.".format(length_value, length_value / 30.48))
        elif length_convert == 4:
            print("{} cm is equal to {} m.".format(length_value, length_value / 100))
        elif length_convert == 5:
            print("{} m is equal to {} cm.".format(length_value, length_value * 100))
        else:
            print("Sorry, Please type correct number from 1 to 5.")

    # ==== Type 2 (Temperature) ====
    elif change == 2:
        print(">>> You chose type Temperature")
        print("")
        Temp_dict = \
            {
                1: "Celsius to Fahrenheit",
                2: "Celsius to Kelvin",
                3: "Fahrenheit to Celsius",
                4: "Fahrenheit to Kelvin",
                5: "Kelvin to Celsius",
                6: "Kelvin to Fahrenheit"
            }

        # ==== for getting number of conversion ====
        print("==========================")
        Temp_value = float(input("- Enter a number to convert: "))
        for keys, values in Temp_dict.items():
            print("{:2}. {}".format(keys, values))
        Temp_convert = int(input("\nWhich conversion you want to do from 1 to 6: "))

        # ==== converting ====
        if Temp_convert == 1:
            print("{} C is equal to {} F".format(Temp_value, (Temp_value * 9.5) + 32))
        elif Temp_convert == 2:
            print("{} C is equal to {} K".format(Temp_value, Temp_value + 273.15))
        elif Temp_convert == 3:
            print("{} F is equal to {} C".format(Temp_value, (Temp_value - 32) * 5.9))
        elif Temp_convert == 4:
            print("{} C is equal to {} K".format(Temp_value, (Temp_value - 32) * 5.9 + 273.15))
        elif Temp_convert == 5:
            print("{} K is equal to {} C".format(Temp_value, Temp_value - 273.15))
        elif Temp_convert == 6:
            print("{} K is equal to {} F".format(Temp_value, (Temp_value - 273.15) * 9.5 + 32))
        else:
            print("Sorry, Please type correct number from 1 to 6.")

    # ==== Type 3 (Time) ====
    elif change == 3:
        print(">>> You chose type Time")
        print("")
        Time_dict = \
            {
                1: "Second to Minute",
                2: "Minute to Second",
                3: "Second to Hour",
                4: "Minute to Hour",
                5: "Hour to Minute",
                6: "Day to Hour",
                7: "Hour to Day"
            }

        # ==== for getting number of conversion ====
        print("==========================")
        Time_value = float(input("- Enter a number to convert: "))
        for keys, values in Time_dict.items():
            print("{:2}. {}".format(keys, values))
        Time_convert = int(input("\nWhich conversion you want to do from 1 to 7: "))

        # ==== converting ====
        if Time_convert == 1:
            print("{} S is equal to {} M".format(Time_value, Time_value / 60))
        elif Time_convert == 2:
            print("{} M is equal to {} S".format(Time_value, Time_value * 60))
        elif Time_convert == 3:
            print("{} S is equal to {} H".format(Time_value, Time_value / 3600))
        elif Time_convert == 4:
            print("{} M is equal to {} H".format(Time_value, Time_value / 60))
        elif Time_convert == 5:
            print("{} H is equal to {} M".format(Time_value, Time_value * 60))
        elif Time_convert == 6:
            print("{} day is equal to {} H".format(Time_value, Time_value * 24))
        elif Time_convert == 7:
            print("{} H is equal to {} day".format(Time_value, Time_value / 24))
        else:
            print("Sorry, Please type correct number from 1 to 7.")

    # ==== Type 4 (Speed) ====
    elif change == 4:
        print(">>> You chose type Speed")
        print("")
        Spead_dict = \
            {
                1: "Mile per hour to kilometer per hour",
                2: "Kilometer per hour to Mile per hour",
                3: "Mile per hour to Meter per Second",
                4: "Meter per Second to Mile per hour",
                5: "Kilometer per hour to Meter per Second",
                6: "Meter per Second to Kilometer per hour"
            }

        # ==== for getting number of conversion ====
        print("==========================")
        Spead_value = float(input("- Enter a number to convert: "))
        for keys, values in Spead_dict.items():
            print("{:2}. {}".format(keys, values))
        Spead_convert = int(input("\nWhich conversion you want to do from 1 to 6: "))

        # ==== converting ====
        if Spead_convert == 1:
            print("{} Ml is equal to {} Km".format(Spead_value, Spead_value * 1.609))
        elif Spead_convert == 2:
            print("{} Km is equal to {} Ml".format(Spead_value, Spead_value / 1.609))
        elif Spead_convert == 3:
            print("{} Ml is equal to {} M".format(Spead_value, Spead_value / 2.237))
        elif Spead_convert == 4:
            print("{} M is equal to {} Ml".format(Spead_value, Spead_value * 2.237))
        elif Spead_convert == 5:
            print("{} Km is equal to {} M".format(Spead_value, Spead_value / 3.6))
        elif Spead_convert == 6:
            print("{} M is equal to {} Km ".format(Spead_value, Spead_value * 3.6))
        else:
            print("Sorry, Please type correct number from 1 to 6.")


    # ==== Type 5 (Enegry) ====
    elif change == 5:
        print(">>> You chose type Energy")
        print("")
        Energy_dict = \
            {1: "Joule to Kilojoule",
             2: "Kilojoule to Joule",
             3: "Joule to Kilocalorie",
             4: "Kilocalorie to Joule",
             5: "Kilojoule to Kilocalorie",
             6: "Kilocalorie to Kilojoule"
             }

        # ==== for getting number of conversion ====
        print("==========================")
        Energy_value = float(input("- Enter a number to convert: "))
        for keys, values in Energy_dict.items():
            print("{:2}. {}".format(keys, values))
        Energy_convert = int(input("\nWhich conversion you want to do from 1 to 6: "))
        if Energy_convert == 1:
            print("{} J is equal to {} Kj".format(Energy_value, Energy_value / 1000))
        elif Energy_convert == 2:
            print("{} Kj is equal to {} J".format(Energy_value, Energy_value * 1000))
        elif Energy_convert == 3:
            print("{} J is equal to {} Kc".format(Energy_value, Energy_value / 4184))
        elif Energy_convert == 4:
            print("{} Kc is equal to {} J".format(Energy_value, Energy_value * 4184))
        elif Energy_convert == 5:
            print("{} Kj is equal to {} Kc".format(Energy_value, Energy_value / 4.184))
        elif Energy_convert == 6:
            print("{} Kc is equal to {} Kj".format(Energy_value, Energy_value * 4.184))
        else:
            print("Sorry, Please type correct number from 1 to 6.")
UnitConverter()
def runAgain():
	runAgn = input("\nwant To Run Again Y/n: ")
	if(runAgn.lower() == 'y'):
		UnitConverter()
		runAgain()
	else:
	    print("Exit")

runAgain()