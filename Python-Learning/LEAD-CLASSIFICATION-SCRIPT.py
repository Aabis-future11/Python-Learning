def classifying_lead(budget, interest):
    if budget > 0:

        if interest == True: 
            if budget >= 50000:
                return " HOT lead with high budget"
            elif 20000 <= budget < 50000:
                return " HOT lead with a medium budget"
            else:
                return " HOT lead with a low budget"
            
        else:
            if 20000 <= budget <= 50000:
                return " WARM lead with medium budget"
            elif budget > 50000: 
                return " WARM lead with high budget"
            else:
                return "COLD lead"
    else:
        return "INVALID budget"

n = int(input("Number of leads: "))

for i in range(n):
    print(f"\n--- Entering Data for Lead #{i+1} ---")
    name = input("Enter your name: ")
    budget1 = int(input("Enter your budget: "))
    interest1 = input("Enter your interest (high/low/medium): ").lower()


    is_interested = (interest1 == "high")
    
    status = classifying_lead(budget1, is_interested)
    
    print(f"\n#------- LEAD SUMMARY -------#")
    print(f"Name: {name}")
    print(f"Details: {budget1}, Interest: {interest1}")
    print(f"Classification: {status}")
    print()

print("Processing Complete!")