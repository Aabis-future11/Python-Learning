def classifying_lead(budget, interest_level):
    if budget <= 0:
        return "INVALID budget"

    if interest_level == "high":
        if budget >= 50000:
            return " Hot lead with high budget"
        elif 20000 <= budget < 50000:
            return " Hot lead with a medium budget"
        else:
            return " Hot lead with a low budget"
            
    
    elif interest_level == "medium":
        if budget >= 20000:
            return " Warm lead with good budget"
        else:
            return " Warm lead with low budget"
        
    else:
        return "Cold lead"

n = int(input("Number of leads:"))

for i in range(n):
    print(f"\n--- Entering Data for Lead #{i+1} ---")
    name = input("Enter your name: ")
    budget1 = int(input("Enter your budget: "))
    interest1 = input("Enter your interest (high/medium/low): ").lower()
    
    # Seedha string pass kar rahe hain function mein
    status = classifying_lead(budget1, interest1)
    
    print(f"#------- LEAD SUMMARY -------#")
    print(f"Name: {name}")
    print(f"Details: Budget {budget1}, Interest: {interest1}")
    print(f"Classification: {status}")
    print()

print("Processing Complete!")