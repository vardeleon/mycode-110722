 #!/usr/bin/env python3

# ifc and lese challenge """

def main():

    message = 'Detemining Earthquake Effects base on Magnitude:   '

# wrap connection in a float() to accept decimals as numbers
#    magnetude = float(input("Please enter the Magnetude: "))
    magnetude = input("Please enter the Magnetude: ")
    if not magnetude.isdigit():
         print("Please enter numeric  ie 1 - 8 ")
         return

# if input value was higher or equal to 8
    magnetude = float(magnetude)

    if magnetude >= 8:
         message = message + 'Great earthquake. Can totally destroy communities near the epicenter.'
    elif magnetude >= 7:
         message = message + 'Major earthquake. Serious damage'
    elif magnetude >= 6.1:
         message = message + 'May cause a lot of damage in very populated areas.'
    elif magnetude >= 5.5:
         message = message + 'Slight damage to buildings and other structures.'
    elif magnetude >= 2.6:
          message = message + 'Often felt, but only causes minor damage.'
    elif magnetude >= 2.5:
         message = message + 'Usually not felt, but can be recorded by seismograph.'
    else:  
         message = message + 'Butterfly wings.'
    print(message)

if  __name__ == "__main__":
    main()

