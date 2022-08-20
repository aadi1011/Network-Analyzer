from imports import *
from figlet import banner
from main_page import start_screen
from start_options import *

#show_data function includes all the text-based diplayable options provided by the program. 
def show_data(data_file):
    banner()
    print("0. Go Back")  
    print("1. Show first 10 readings")
    print("2. Show source and counts")
    print("3. Show destination and counts")
    print("4. Show protocols and counts")
    print("5. Show all traffic of a protocol")

    sub_option2 = int(input("Choose option: "))
    if(sub_option2==1):
        try:
            print(data_file.head(10))   #pandas head() prints the first 10 results of csv 
            os.system('pause')
            os.system('cls')
            show_data(data_file)
        except KeyError:
            os.system('cls')
            banner()
            print("Invalid CSV Format provided. Please upload a valid CSV file of Wireshark export format.")
            os.system('pause')
            os.system('cls')
            start_screen()
    elif(sub_option2==2):
        try:
            sources=data_file.groupby("Source").Source.count()  #groups the csv data by the 'Source' filter and sorts them by their count
            print(sources.sort_values())
            os.system('pause')
            os.system('cls')
            show_data(data_file)
        except KeyError:
            os.system('cls')
            banner()
            print("Invalid CSV Format provided. Please upload a valid CSV file of Wireshark export format.")
            os.system('pause')
            os.system('cls')
            start_screen()
    elif(sub_option2==3):
        try:
            dest=data_file.groupby("Destination").Destination.count() #groups the csv data by the 'Destination' filter and sorts them by their count
            print(dest.sort_values())
            os.system('pause')
            os.system('cls')
            show_data(data_file)
        except KeyError:
            os.system('cls')
            banner()
            print("Invalid CSV Format provided. Please upload a valid CSV file of Wireshark export format.")
            os.system('pause')
            os.system('cls')
            start_screen()
    elif(sub_option2==4):
        try:
            protocol=data_file.groupby("Protocol").Protocol.count() #groups the csv data by the 'Protocol' filter and sorts them by their count
            print(protocol.sort_values())
            os.system('pause')
            os.system('cls')
            show_data(data_file)
        except KeyError:
            os.system('cls')
            banner()
            print("Invalid CSV Format provided. Please upload a valid CSV file of Wireshark export format.")
            os.system('pause')
            os.system('cls')
            start_screen()
    elif(sub_option2==5):
        try:
            ProtoSearch = input("Enter the protocol you want to search (case sensitive): ")  #User input to search all connections for a protocol.
            #Allowing more than default '10' values to be printed
            pd.set_option('display.max_rows', 500)                          
            print(data_file.loc[data_file['Protocol']==ProtoSearch, ["Time","Source","Destination","Protocol","Length"]])
            os.system('pause')
            os.system('cls')
            #Setting values back to 10 (default)
            pd.set_option('display.max_rows', 10)
            show_data(data_file)
        except KeyError:
            os.system('cls')
            banner()
            print("Invalid CSV Format provided. Please upload a valid CSV file of Wireshark export format.")
            os.system('pause')
            os.system('cls')
            start_screen()
    elif(sub_option2==0):   #Goes back to main menu
        os.system('cls')
        menu2(data_file)
    else:
        os.system('cls')
        print("Invalid input given. Please try again.")
        os.system('pause')
        os.system('cls')
        show_data(data_file)
