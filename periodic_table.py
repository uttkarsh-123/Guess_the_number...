group1 = ["Hydrogen", "Lithium", "Sodium", "Potassium", "Rubidium", "Ceasium", "Francium"]
group2 = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
group13 = ["Boron", "Alluminium", "Gallium", "Indium","Thallium"]
group14 = ["Carbon", "Silicon", "Germanium", "Tin","Lead"]
group15 = ["Nitrogen", "Phosphorus", "Astatine", "Antimony", "Bismuth"]
group16 = ["Oxygen", "Sulphur", "Selenium", "tellurium", "Polonium"]
group17 = ["Fluorine", "Chlorine", "Bromine", "Iodine","Astatine"]
group18 = ["Helium", "Neon", "Argon","Krypton", "Xenon", "Radium"]
group = int(input("Please enter the group :-\n"))
period = int(input("Please enter the period:-\n"))
period-=1
if group == 1:
    print(group1[period])
elif group == 2:
    print(group2[period])
elif group == 3:
    print(group3[period])
elif group == 13:
    print(group13[period])
elif group == 14:
    print(group14[period])
elif group == 15:
    print(group15[period])
elif group == 16:
    print(group16[period])
elif group == 17:
    print(group17[period])
elif group == 18:
    print(group18[period])

