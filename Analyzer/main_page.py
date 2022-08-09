from imports import *
from figlet import banner
from start_options import *
from info import about
from exits import exit

def start_screen():
    os.system('cls')
    banner()
    print("\n\t\t***** MENU *****\n")
    print("1. Start")
    print("2. About")
    print("3. Exit")
    try:
        menu_input=int(input("Enter your choice (1/2/3): "))    
        if(menu_input==1):
            os.system('cls')
            print("Let's start with Network Analysis:\n\n")
            try:
                # Complete file path of CSV file required. Error(L268) if missing file path provided.
                file_path = input("Enter complete csv file path with readings: ")
                # CSV file read and imported as pandas dataframes and stored in data_file variable.
                data_file = pd.read_csv(file_path) 
                os.system('cls')
                print("Data loaded successfully!\n\n")
                menu2(data_file)
            
            except FileNotFoundError:
                os.system('cls')
                banner()
                print("\n\nERROR: FILE NOT FOUND. Enter valid file path.")
                os.system('pause')
                os.system('cls')
                start_screen()

            except OSError:
                os.system('cls')
                banner()
                print("\n\nERROR: Invalid argument. Please enter without quote marks.")
                os.system('pause')
                os.system('cls')
                start_screen()
        
        elif(menu_input==2):
            about()
        
        elif(menu_input==3):
            exit()
        
        else:
            os.system('cls')
            banner()
            print("\n\nInvalid Input.")
            os.system('pause')
            os.system('cls')
            start_screen()
    
    # ValueError exception prevents program from crashing when no required inputs are passed
    except ValueError:
        os.system('cls')
        banner()
        print("\n\nPlease enter an input.")
        os.system('pause')
        os.system('cls')
        start_screen()

#Calls the start_screen() and effectively the application
start_screen()
