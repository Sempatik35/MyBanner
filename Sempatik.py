import random,time, sys
from colorama import *
 
init(autoreset=True)
fr = Fore.RED
fb = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
 
def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
 
    x = """
  (                                             
 )\ )                              )        )  
(()/(   (     )              )  ( /( (   ( /(  
 /(_)) ))\   (     `  )   ( /(  )\()))\  )\()) 
(_))  /((_)  )\  ' /(/(   )(_))(_))/((_)((_)\  
/ __|(_))  _((_)) ((_)_\ ((_)_ | |_  (_)| |(_) 
\__ \/ -_)| '  \()| '_ \)/ _` ||  _| | || / /  
|___/\___||_|_|_| | .__/ \__,_| \__| |_||_\_\  
                  |_|                      
 
       +-------- CREATED BY--------+
 
                                          """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
        time.sleep(0.06)
logo()