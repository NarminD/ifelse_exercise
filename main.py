exercise = int(input('How many minutes do you exercise a day? '))

if exercise in range(5,19):
    print("A little exercise goes a long way.")
elif exercise in range(20,29):
    print("You’re doing great, keep it up.")
elif exercise in range(30,59):
    print("You are investing in your health.")
elif exercise >=60:
    print("You’re a legend, building the habit to a long and healthy life.")
else:
    print("You need to start exercising, asap!")



 #if_else statements 