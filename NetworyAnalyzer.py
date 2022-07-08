import os
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import geoip2.database
import pyfiglet

result = pyfiglet.figlet_format("Aadi's Network Analyzer", font = "slant" )
print(result)

def menu2(data_file):
    print("0. Go Back")
    print("1. Show Data")
    print("2. Build Graphs")
    option_menu2 = int(input("Choose an option: \n"))
    if(option_menu2 == 1):
        os.system('cls')
        show_data(data_file)
    elif(option_menu2==2):
        os.system('cls')
        graph_data(data_file)
    elif(option_menu2==0):
        os.system('cls')
        start_screen()

def show_data(data_file):
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

def about():
    pass

def exit():
    pass


def start_screen():
    print("\n\t\t***** MENU *****\n")
    print("1. Start")
    print("2. About")
    print("3. Exit")
    menu_input=int(input("Enter your choice (1/2/3): "))
    if(menu_input==1):
        os.system('cls')
        print("Let's start with Network Analysis:\n\n")
        file_path = input("Enter complete csv file path with readings: ")
        data_file = pd.read_csv(file_path)
        os.system('cls')
        print("Data loaded successfully!\n\n")
        menu2(data_file)
    elif(menu_input==2):
        about()
    elif(menu_input==3):
        exit()
    else:
        print("Wrong Input.")

start_screen()
