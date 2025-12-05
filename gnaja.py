
import sys
sys.path.append(r"c:\Users\Saptadeep\Desktop\100 days of python")
import os
import time

import decoder



# Get the absolute path of the current script file
path = os.path.abspath(__file__)

# Get the directory name (folder) of the script
directory = os.path.dirname(path)

print("path= ",directory)

time.sleep(3)

decoder.clr_screen()

print("Hello world!")



# sys.path.append(f"r"{directory}"")
                
# import poem

# poem.poem()
