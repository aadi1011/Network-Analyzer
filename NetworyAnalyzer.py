# AADI'S NETWORK ANALYZER.
# This python program analyzes captured network packets in CSV and allows the user to classify them according to source traffic, destination traffic
# protocols and also map the network traffic with its connections in a visual format.
# Suspected network addresses can also be marked and mapped. 
# An additional GeoLocator feature is also provided.

#MIT License
#Copyright (c) 2022 Aadith Sukumar
# Created by AADITH SUKUMAR
# GitHub: https://github.com/aadi1011
# LinkedIn: https://linkedin.com/in/aadith-sukumar/

# Importing required libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import geoip2.database
import pyfiglet
 
# banner() function for ASCII Word Art in the terminal. banner() is called at start of every function after 
# clearing screen to stay on top of program
def banner():
    result = pyfiglet.figlet_format("Aadi's Network Analyzer", font = "slant" ) #pyfiglet module helps create the art
    print(result)

# Main menu function. Actual program starts with the start_screen() function
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
        show_data(data_file)
    elif(option_menu2==2):  #Proceeds to graph_data()
        os.system('cls')
        graph_data(data_file)
    elif(option_menu2==3):  #Proceeds to suspect()
        os.system('cls')
        suspect(data_file)  
    elif(option_menu2==4):  #Proceeds to GeoLoc()
        os.system('cls')
        GeoLoc(data_file)
    elif(option_menu2==0):  #Goes back
        os.system('cls')
        start_screen()
    else:                   #If invalid option given by user
        os.system('cls')
        print("Invalid input given. Please try again.")
        os.system('pause')
        os.system('cls')
        menu2(data_file)        
 
#show_data function includes all the text-based diplayable options provided by the program. 
def show_data(data_file):
    banner()
    print("0. Go Back")  
    print("1. Show first 10 readings")
    print("2. Show source and counts")
    print("3. Show destination and counts")
    print("4. Show protocols and counts")
    
    sub_option2 = int(input("Choose option: "))
    if(sub_option2==1):
        print(data_file.head(10))   #pandas head() prints the first 10 results of csv 
        os.system('pause')
        os.system('cls')
        show_data(data_file)
    elif(sub_option2==2):
        sources=data_file.groupby("Source").Source.count()  #groups the csv data by the 'Source' filter and sorts them by their count
        print(sources.sort_values())
        os.system('pause')
        os.system('cls')
        show_data(data_file)
    elif(sub_option2==3):
        dest=data_file.groupby("Destination").Destination.count() #groups the csv data by the 'Destination' filter and sorts them by their count
        print(dest.sort_values())
        os.system('pause')
        os.system('cls')
        show_data(data_file)
    elif(sub_option2==4):
        protocol=data_file.groupby("Protocol").Protocol.count() #groups the csv data by the 'Protocol' filter and sorts them by their count
        print(protocol.sort_values())
        os.system('pause')
        os.system('cls')
        show_data(data_file)
    elif(sub_option2==0):   #Goes back to main menu
        os.system('cls')
        menu2(data_file)
    else:
        os.system('cls')
        print("Invalid input given. Please try again.")
        os.system('pause')
        os.system('cls')
        show_data(data_file)

#graph_data() provides options for graphical display of data
def graph_data(data_file):
    banner()
    print("0. Go Back")
    print("1. Display NodeView of traffic")
    print("2. Display EdgeView of traffic")
    print("3. Display network map based on traffic")
    
    sub2_option2=int(input("Choose an option:"))
    if(sub2_option2==1):
        #the map of the network with its start points and end points are first gathered before mapping.  
        network = nx.from_pandas_edgelist(data_file, source="Source", target="Destination", edge_attr=True) #file and other attributes mentioned and stored in network variable.
        print(network.nodes()) # Prints the nodal view of the network map
        os.system('pause')
        os.system('cls')
        graph_data(data_file)
    
    elif(sub2_option2==2):
        network = nx.from_pandas_edgelist(data_file, source="Source", target="Destination", edge_attr=True)
        print(network.edges())  #Prints the edge view of the network map with its source and destination
        os.system('pause')
        os.system('cls')
        graph_data(data_file)
    
    elif(sub2_option2==3):
        network = nx.from_pandas_edgelist(data_file, source="Source", target="Destination", edge_attr=True)
        nx.draw_circular(network, with_labels=True) #network map is drawn with the connections made from the network variable.
        #Network map is plotted (on a new window if running from terminal)
        plt.show()  
        os.system('pause') 
        os.system('cls')
        graph_data(data_file)
    
    elif(sub2_option2==0):
        os.system('cls')
        menu2(data_file)
    
    else:
        os.system('cls')
        print("Invalid input given. Please try again.")
        os.system('pause')
        os.system('cls')
        graph_data(data_file)

# If any suspected address found in network, suspect() marks it separately and displays information about its connections. 
def suspect(data_file):
    banner()
    
    #taking input of suspect
    suspect_ad=input("Enter suspected address: ")
    print("Suspect loaded\n")
    
    #loading network map data (as started in L116)
    network = nx.from_pandas_edgelist(data_file, source="Source", target="Destination", edge_attr=True)
    
    #Suspect source and destination connection information is grapped and stored in two different variable and printed.
    suspect_source_info=data_file.loc[data_file["Source"]==suspect_ad]    #takes the data from the captured file and cross-checks the suspect's connections as source
    suspect_dest_info=data_file.loc[data_file["Destination"]==suspect_ad] #takes the data from the captured file and cross-checks the suspect's connections as destination
    print("Captured source network information of suspect: \n",suspect_source_info)
    print("\n\nCaptured destination network information of suspect: \n",suspect_dest_info)
    
    #prompt to show graphical network map with suspected isolated with its connections.
    suspect_graph_option=input("\nPress Y to show suspect network graph (any other key to go back): ")
    if(suspect_graph_option=='y' or suspect_graph_option=='Y'):
        pos=nx.spring_layout(network)   #the spring_layour positions nodes using Fruchterman-Reingold force-directed algorithm
        
        #Safe networks marked isolated and with green colour and other parameters
        nx.draw(network, pos, node_color="green", node_size=300, with_labels=True)
        #Suspect marked in red by program and larger size to show prominence
        options = {"node_size":1000, "node_color":"r"}
        nx.draw_networkx_nodes(network, pos, nodelist=[suspect_ad],**options)
        plt.show()  #Network map is plotted (on a new window if running from terminal)
        os.system('\npause')
        os.system('cls')
        menu2(data_file)
    
    else:
        os.system('cls')
        menu2(data_file)

#GeoLoc() uses geoip2 and geolite2 tools to locate and return the origin country of a public IP Address
def GeoLoc(data_file):
    banner()
    
    print("\n GEOLOCATION TOOL: \nFinds country location of provided public address using GeoIP2 module.")
    print("NOTE: Requires GeoLite2-Country.mmdb file installed in path. Only works on PUBLIC IP addreses.\n")
    geo_option=input("Print 1 to continue, 0 to go back: ")
    if(geo_option=='1'):

        #loads the GeoLite2-Country.mmdb file into the geoip2 database
        reader = geoip2.database.Reader("C:\\Users\\Aadith Sukumar\\Desktop\\CyberSec Project\\Network Analyzer\\GeoLite2-Country.mmdb")
        geoloc_input=input("Enter Public IP Address to locate: ")
        try:
            #Checks in the database for the input public IP address
            response = reader.country(geoloc_input) 
            print(response.country.name)
            os.system('pause')
            os.system('cls')
            menu2()
            
        #Private IP Address/Reserved IP Address are not located by geoip2 tool and error thrown
        except geoip2.errors.AddressNotFoundError: 
            print("Address not in database")
            os.system('pause')
            os.system('cls')        
            GeoLoc()

        except ValueError:
            print("Invalid Input")
            os.system('pause')
            os.system('cls')
            GeoLoc()
    
    elif(geo_option=='0'):
        os.system('cls')
        menu2(data_file)

#About page of this application
def about():
    os.system('cls')
    banner()
    print("**Network Analyzer Program**")
    print("Network Analyzer analyzes the network information available in CSV format, captured using Wireshark or any other network/packet sniffing/capturing tool.")
    print("This is developed solely for use in Windows OS and developmen is underway for Linux distros as well.\n")
    print("Created By: AADITH SUKUMAR")
    print("GitHub: https://github.com/aadi1011")
    print("LinkedIn: https://www.linkedin.com/in/aadith-sukumar/")
    os.system('pause')
    os.system('cls')
    start_screen()

#Prompted exit menu of application
def exit():
    os.system('cls')
    banner()
    
    exit_option=input("Are You Sure?(Y/N): ")
    if(exit_option=='Y' or exit_option=='y'):
        os.system('cls')
        print("Thank you for using Network Analyzer!")
    elif(exit_option=='N' or exit_option=='n'):
        os.system('cls')
        start_screen()
    else:
        exit()

#APPLICATION STARTS WITH THIS FUNCTION
# Start screen with the basic menu options and that leads to other functions of the application. 
def start_screen():
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
