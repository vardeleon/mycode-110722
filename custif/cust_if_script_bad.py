 #!/usr/bin/env python3


message = 'Effects base on Magnitude:  '
#message = 'Detemining Earthquake Effects base on Magnitude '

# wrap connection in a float() to accept decimals as numbers
magnetude = float(input("Please enter the Magnetude: "))

# if input value was higher or equal to 25
if magnetude > 8 and magnetude < 7.9:
   message = message + 'Great earthquake. Can totally destroy communities near the epicenter.'
if magnetude >= 7.9: magnetude < 7.9:
    message = message + 'Major earthquake. Serious damage'
elif magnetude >= 6.9:
    message = message + 'May cause a lot of damage in very populated areas.'
elif magnetude >= 6.0:
    message = message + 'Slight damage to buildings and other structures.'
elif magnetude >= 5.4:
    message = message + 'Often felt, but only causes minor damage.'
elif magnetude >= 2.5:
    message = message + 'Usually not felt, but can be recorded by seismograph.'
#else:  
#    message = message + 'Great earthquake. Can totally destroy communities near the epicenter.'
print(message)

