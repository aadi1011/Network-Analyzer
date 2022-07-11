import os
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import geoip2.database
import pyfiglet
 

def banner():
    result = pyfiglet.figlet_format("Aadi's Network Analyzer", font = "slant" )
    print(result)

def menu2(data_file):
    banner()
    print("0. Go Back")
    print("1. Show Data")
    print("2. Build Graphs")
    print("3. Trace Suspected Address")
    print("4. Find public IP address GeoLocation")
    option_menu2 = int(input("Choose an option: \n"))
    if(option_menu2 == 1):
        os.system('cls')
        show_data(data_file)
    elif(option_menu2==2):
        os.system('cls')
        graph_data(data_file)
    elif(option_menu2==3):
        os.system('cls')
        suspect(data_file)
    elif(option_menu2==4):
        os.system('cls')
        GeoLoc()

    elif(option_menu2==0):
        os.system('cls')
        start_screen()
    else:
        os.system('cls')
        print("Invalid input given. Please try again.")
        os.system('pause')
        os.system('cls')
        menu2(data_file)        
 
def show_data(data_file):
    banner()
    print("0. Go Back")  
    print("1. Show first 10 readings")
    print("2. Show source and counts")
    print("3. Show destination and counts")
    print("4. Show protocols and counts")
    sub_option2 = int(input("Choose option: "))
    if(sub_option2==1):
        print(data_file.head(10))
        os.system('pause')
        os.system('cls')
        show_data(data_file)
    elif(sub_option2==2):
        sources=data_file.groupby("Source").Source.count()
        print(sources.sort_values())
        os.system('pause')
        os.system('cls')
        show_data(data_file)
    elif(sub_option2==3):
        dest=data_file.groupby("Destination").Destination.count()
        print(dest.sort_values())
        os.system('pause')
        os.system('cls')
        show_data(data_file)
    elif(sub_option2==4):
        protocol=data_file.groupby("Protocol").Protocol.count()
        print(protocol.sort_values())
        os.system('pause')
        os.system('cls')
        show_data(data_file)
    elif(sub_option2==0):
        os.system('cls')
        menu2(data_file)
    else:
        os.system('cls')
        print("Invalid input given. Please try again.")
        os.system('pause')
        os.system('cls')
        show_data(data_file)

def graph_data(data_file):
    banner()
    print("0. Go Back")
    print("1. Display NodeView of traffic")
    print("2. Display EdgeView of traffic")
    print("3. Display network map based on traffic")
    sub2_option2=int(input("Choose an option:"))
    if(sub2_option2==1):
        network = nx.from_pandas_edgelist(data_file, source="Source", target="Destination", edge_attr=True)
        print(network.nodes())
        os.system('pause')
        os.system('cls')
        graph_data(data_file)
    elif(sub2_option2==2):
        network = nx.from_pandas_edgelist(data_file, source="Source", target="Destination", edge_attr=True)
        print(network.edges())
        os.system('pause')
        os.system('cls')
        graph_data(data_file)
    elif(sub2_option2==3):
        network = nx.from_pandas_edgelist(data_file, source="Source", target="Destination", edge_attr=True)
        nx.draw_circular(network, with_labels=True)
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

def suspect(data_file):
    banner()
    suspect_ad=input("Enter suspected address: ")
    print("Suspect loaded\n")
    
    network = nx.from_pandas_edgelist(data_file, source="Source", target="Destination", edge_attr=True)
    suspect_source_info=data_file.loc[data_file["Source"]==suspect_ad]
    suspect_dest_info=data_file.loc[data_file["Destination"]==suspect_ad]
    print("Captured source network information of suspect: \n",suspect_source_info)
    print("\n\nCaptured destination network information of suspect: \n",suspect_dest_info)
    
    suspect_graph_option=input("\nPress Y to show suspect network graph (any other key to go back): ")
    if(suspect_graph_option=='y' or suspect_graph_option=='Y'):
        pos=nx.spring_layout(network)
        nx.draw(network, pos, node_color="green", node_size=300, with_labels=True)
        options = {"node_size":1000, "node_color":"r"}
        nx.draw_networkx_nodes(network, pos, nodelist=[suspect_ad],**options)
        plt.show()
        os.system('\npause')
        os.system('cls')
        menu2(data_file)
    else:
        os.system('cls')
        menu2(data_file)

def GeoLoc():
    banner()
    
    print("\n GEOLOCATION TOOL: \nFinds country location of provided public address using GeoIP2 module.")
    print("NOTE: Requires GeoLite2-Country.mmdb file installed in path. Only works on PUBLIC IP addreses.\n")
    geo_option=input("Print 1 to continue, 0 to go back: ")
    if(geo_option==1):
        reader = geoip2.database.Reader("C:\\Users\\Aadith Sukumar\\Desktop\\CyberSec Project\\Network Analyzer\\GeoLite2-Country.mmdb")
        geoloc_input=input("Enter Public IP Address to locate: ")
        try:
            response = reader.country(geoloc_input)
            print(response.country.name)
            os.system('pause')
            os.system('cls')
            menu2()
            
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
    elif(geo_option==0):
        os.system('cls')
        menu2()


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
                file_path = input("Enter complete csv file path with readings: ")
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
    except ValueError:
        os.system('cls')
        banner()
        print("\n\nPlease enter an input.")
        os.system('pause')
        os.system('cls')
        start_screen()

start_screen()
