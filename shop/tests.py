
# 1 Take a list from the user and reverse it without user defined function.
#user=input("enter a list")
#for i in user:
   # print(i)



import time


    # Get the current time
num=int(input("enter time"))
current_time = datetime.datetime.now().time()

    # Extract the hour from the current time
current_hour = current_time.hour

    # Greet the user based on the current hour
if 5 <= current_hour < 12:
    print("Good morning!")
elif 12 <= current_hour < 18:
    print("Good afternoon!")
else:
    print("Good evening!")

# Call the greeting function
#greeting()

