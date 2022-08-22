# banner() function for ASCII Word Art in the terminal. banner() is called at start of every function after 
# clearing screen to stay on top of program

from imports import *
def banner():
    result = pyfiglet.figlet_format("Aadi's Network Analyzer", font = "slant" ) #pyfiglet module helps create the art
    print(result)
