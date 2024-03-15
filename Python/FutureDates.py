# Prompt the user for today's day
current_day = eval(input("Enter today's day, Sunday is 0, Monday is 1, ...., and Saturday is 6: "))

c_day = ""

if current_day == 0:
    c_day = 'Sunday'
    
elif current_day == 1:
    c_day = 'Monday'

elif current_day == 2:
    c_day = 'Tuesday'

elif current_day == 3:
    c_day = 'Wednesday'

elif current_day == 4:
    c_day = 'Thursday'

elif current_day == 5:
    c_day = 'Friday'

elif current_day == 6:
    c_day = 'Saturday'

else:
    print ('Wrong input!')

# Prompt the user for a number of days after current day for the future day

days_after = eval(input('Enter the number of days elapsed since today: '))

future_day = (days_after + current_day) % 7

f_day = ""

if future_day == 0:
    f_day = 'Sunday'
    
elif future_day == 1:
    f_day = 'Monday'

elif future_day == 2:
    f_day = 'Tuesday'

elif future_day == 3:
    f_day = 'Wednesday'

elif future_day == 4:
    f_day = 'Thursday'

elif future_day == 5:
    f_day = 'Friday'

elif future_day == 6:
    f_day = 'Saturday'

else:
    print ('Wrong input!')
    

print (f"Today is {c_day} and the future is {f_day}")