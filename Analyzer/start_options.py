#main menu code. need to fix circular import

from imports import *
from figlet import banner
from main_page import *  #to check circulat import
import data_disp
import graph_disp
import sus_data
import geo_loc

def menu2(data_file):
    banner()
    # menu option
    print("0. Go Back")
    print("1. Show Data")
    print("2. Build Graphs")
    print("3. Trace Suspected Address")
    print("4. Find public IP address GeoLocation")
    
    option_menu2 = int(input("Choose an option: \n")) # Take user choice for menu
    if(option_menu2 == 1):  #Proceeds to show_data() 
        os.system('cls')
        data_disp.show_data(data_file)
    elif(option_menu2==2):  #Proceeds to graph_data()
        os.system('cls')
        graph_disp.graph_data(data_file)
    elif(option_menu2==3):  #Proceeds to suspect()
        os.system('cls')
        sus_data.suspect(data_file)  
    elif(option_menu2==4):  #Proceeds to GeoLoc()
        os.system('cls')
        geo_loc.GeoLoc(data_file)
    elif(option_menu2==0):  #Goes back
        os.system('cls')
        start_screen()
    else:                   #If invalid option given by user
        os.system('cls')
        print("Invalid input given. Please try again.")
        os.system('pause')
        os.system('cls')
        menu2(data_file)        
