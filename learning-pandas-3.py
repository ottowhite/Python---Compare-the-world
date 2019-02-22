#learning-pandas-3
#more challenging spreadsheet

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def section(text):
    lines = "-------------------------------------------------------------------------------"
    thing = int(len(lines)/2-len(text)/2)-2

    print("\n\n")
    print(lines[0:thing] + "[ " + text + " ]" + lines[0:thing] + "\n")

sheet = pd.read_csv("country_data.csv")






def compare_the_world():
    section("COMPARE THE WORLD")
    print()
    for x in range(0, len(sheet.columns)):
        print(str(x) + " " + sheet.columns[x])
        
    independant = int(input("\nPlease enter the index of the independant variable: "))
    dependant = int(input("Please enter the index of the dependant variable: "))

    xvalue = sheet.columns[independant]
    yvalue = sheet.columns[dependant]

    current_country = sheet["country"][0]
    for i in range(0, len(sheet)):

        if (current_country != sheet["country"][i]):
            
            x = sheet[sheet["country"].isin([current_country])][xvalue]
            y = sheet[sheet["country"].isin([current_country])][yvalue]

            
            plt.plot(x, y, label=current_country)

            current_country = sheet["country"][i]
           
    #plt.legend()
    plt.title(yvalue + " against "+ xvalue + " (global)")
    plt.xlabel(xvalue)
    plt.ylabel(yvalue)
    plt.show()



compare_the_world()



'''
        

#for x in range(0, len(countries)):
    



def make_graph():
    
    x = uk["year"]
    y = uk["Confidence in national government"]
    
    plt.plot(x, y, label="UK")
    plt.xlabel("Year")
    plt.ylabel("Confidence in national government")

    plt.legend()
    plt.show()

    
'''

'''
uk = sheet[sheet["country"].isin(["United Kingdom"])]

x = sheet[sheet["country"].isin(["United Kingdom"])]["year"]
y = sheet[sheet["country"].isin(["United Kingdom"])]["Democratic Quality"]

print(x.values)
print(y.values)
plt.plot(x.values, y.values, label="United Kingdom")
plt.show()

'''

#print(sheet.columns)

#make_graph()

#collect_countries()
