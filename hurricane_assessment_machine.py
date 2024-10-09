# Josue Guzman
# Hurricane Assessment Machine

import time

# A simple "boot up" sequence for immersing the user.
print("Welcome to the Hurricane Assessment Machine!")
print("Powering on . . .")
time.sleep(1)
print("Booting . . .")
time.sleep(1)

# Gathers number of hurricanes.
while True:
    count=int(input("How many hurricanes will be assessed today?\n"))

    if (count>5):
        print("We are sorry. The limit is 5 hurricanes. Please try again.")
    else:
        break

print(f"Preparing to assess {count} hurricane(s)...")
print(". . .")
time.sleep(1)

# Creates a list storing name, speed, and category.
hurricane_info=[]

for j in range(count):
    name=input(f"What is the name of Hurricane {j+1}?\n")
    wind_speed=int(input(f"What is the sustained wind speed of {name}?\n"))
    if (wind_speed>=157):
        category=5
    elif (wind_speed<157 and wind_speed>130):
        category=4
    elif (wind_speed<130 and wind_speed>111):
        category=3
    elif (wind_speed<111 and wind_speed>96):
        category=2
    elif (wind_speed<96 and wind_speed>74):
        category=1
    else:
        category=0
    
    hurricane_info.append((name, wind_speed, category))

# Prints the parameters of each hurricane along with a descriptive message.
for i, (name, wind_speed, category) in enumerate(hurricane_info, 1):
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(f"{i}. {name} - Wind Speed: {wind_speed} mph - Category: {category}\n")
    if (category==1):
        print(f"Hurricane {name} has dangerous winds that can cause some damage.\nFlying debris may occur, and power outages are likely due to snapped power lines and downed trees.\n\n")
    elif (category==0):
        print(f"Hurricane {name} is not at hurricane strength, but caution should still be taken.")
    elif (category==2):
        print(f"Hurricane {name} has extremely dangerous winds that will cause significant damage.\nRoofs, trees, and power lines are at risk, and extended power outages may occur.\n\n")
    elif (category==3):
        print(f"Hurricane {name} is a major storm with devastating wind damage. \nWell-built homes may lose roof structure, and electricity and water may be unavailable for several days to weeks.\n\n")
    elif (category==4):
        print(f"Hurricane {name} will bring catastrophic damage. \nMany homes will suffer major damage, with roofs and walls blown off. \nFlooding and power outages may last for weeks.\n\n")
    elif (category==5):
        print(f"Hurricane {name} is life-threatening and catastrophic. \nBuildings may be completely destroyed, and entire areas can be uninhabitable for weeks or months due to flooding and infrastructure damage.\n\n")
    
