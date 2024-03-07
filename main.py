import random
reps = 100
ammount = 100
count = 0
Im_Bereich = 0
ausserhalb = 0

for j in range(reps):
    count = 0
    for i in range(ammount):
        x = random.randint(1,6)
        if x == 6:
            count = count + 1
    if (8 < count) and (count < 25):
        Im_Bereich = Im_Bereich + 1
    else:
        ausserhalb = ausserhalb + 1

print(f"Anzahl im Bereich: {Im_Bereich}")
print(f"Anzahl Außerhalb: {ausserhalb}")