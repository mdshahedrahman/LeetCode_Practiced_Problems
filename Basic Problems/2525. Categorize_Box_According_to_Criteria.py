length = 2909
width = 3968
height = 3272
mass = 727

if (length >= 10 ** 4 or width >= 10 ** 4 or
        height >= 10 ** 4 or mass >= 10 ** 4 or
        (length * width * height) >= 10 ** 9) and mass < 100:
    print("Bulky")

elif ((length >= 10 ** 4 or width >= 10 ** 4 or
        height >= 10 ** 4 or mass >= 10 ** 4 or
        (length * width * height) >= 10 ** 9)) and mass >= 100:
    print("Both")

elif ((length < 10 ** 4 or width < 10 ** 4 or
        height < 10 ** 4 or mass < 10 ** 4 or
        (length * width * height) < 10 ** 9)) and mass < 100:
    print("Neither")

elif ((length < 10 ** 4 or width < 10 ** 4 or
        height < 10 ** 4 or mass < 10 ** 4 or
        (length * width * height) < 10 ** 9)) and mass >= 100:
    print("Heavy")