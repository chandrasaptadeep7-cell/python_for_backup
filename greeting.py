 
    

import time
timestamp = time.strftime('%H:%M:%S')
print(" ")
print("The time is ",timestamp)


hour = int(time.strftime('%H'))

if hour<12:
    print("Good Morning!")

elif hour==12 or hour==13 or hour==14 or hour==15:
    print("Good Noon")
elif hour==16 or hour==17:
    print("Good Afternoon")  
  
elif hour==18 or hour==19 or hour==20 or hour==21:
    print("Good Evening!")  
  
elif hour==23 or hour==24:
    print("Good Night!")  
print(" ")
  
