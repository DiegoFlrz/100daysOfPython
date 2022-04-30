year = int(input("Which year do you want to check?"))

#if year % 4 == 0:
    #if year % 100 == 0:
        #print("Not a Leap year.")
    #elif year % 400 == 0: * This is where i messed up, by not nesting it i messed up the loop somehow so if the year WAS a leap year, it would crash.
        #print("leap year")
#else:
    #print("Not a leap year.")

#How the instructor solved the problem:

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not a leap year.")
