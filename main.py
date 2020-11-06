print("Welcome to the Tip calculator.")
cena = float(input("What was the total bill? $"))
dysko = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
lidi = int(input("How many people to split the bill? "))
dysko_prevod = float((dysko / 100) + 1.00)
vsecko = float((cena / lidi) * dysko_prevod)
vse_dohromady = round(vsecko, 2)
print(f"Each person should pay: {vse_dohromady}")

