#What-day-is-today
#Run the program to find out what day is today

import datetime
a = datetime.datetime.today().weekday()
if a == 0:
    print("It's Monday. Have a nice day.")
elif a == 1:
    print("It's Tuesday. Have a nice day.")
elif a == 2:
    print("It's Wednesday. Have a nice day.")
elif a == 3:
    print("It's Thursday. Have a nice day.")
elif a == 4:
    print("It's Friday. Have a nice day.")
elif a == 5:
    print("It's Saturday. Have a nice day.")
elif a == 6:
    print("It's Sunday. Have a nice day.")
    