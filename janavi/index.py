print("======================================")
print("      SMART TRAFFIC CONTROL SYSTEM    ")
print("======================================")

road1 = int(input("Enter Vehicle Count On Road 1 : "))
road2 = int(input("Enter Vehicle Count On Road 2 : "))
road3 = int(input("Enter Vehicle Count On Road 3 : "))

print("\nEmergency Vehicle Present?")
print("Type YES or NO")

ambulance = input("Enter : ")

print("\n======================================")
print("            VEHICLE REPORT            ")
print("======================================")

print("Road 1 Vehicles :", road1)
print("Road 2 Vehicles :", road2)
print("Road 3 Vehicles :", road3)

print("\n======================================")
print("          TRAFFIC ANALYSIS            ")
print("======================================")

if road1 > road2 and road1 > road3:
    print("Road 1 Has Highest Traffic")
    print("Green Signal Given To Road 1")

elif road2 > road1 and road2 > road3:
    print("Road 2 Has Highest Traffic")
    print("Green Signal Given To Road 2")

elif road3 > road1 and road3 > road2:
    print("Road 3 Has Highest Traffic")
    print("Green Signal Given To Road 3")

else:
    print("Traffic Is Equal On All Roads")

print("\n======================================")
print("       EMERGENCY VEHICLE CHECK        ")
print("======================================")

if ambulance == "YES":
    print("Ambulance Detected")
    print("Emergency Green Signal Activated")

else:
    print("No Emergency Vehicle")

print("\n======================================")
print("         TRAFFIC STATUS REPORT        ")
print("======================================")

total = road1 + road2 + road3

print("Total Vehicles :", total)

if total >= 150:
    print("Traffic Level : HIGH")

elif total >= 80:
    print("Traffic Level : MEDIUM")

else:
    print("Traffic Level : LOW")

print("\n======================================")
print("         SIGNAL TIMER DISPLAY         ")
print("======================================")

for i in range(10, 0, -1):
    print("Green Signal Closing In", i, "Seconds")

print("\n======================================")
print("       AI TRAFFIC MANAGEMENT DONE     ")
print("======================================")