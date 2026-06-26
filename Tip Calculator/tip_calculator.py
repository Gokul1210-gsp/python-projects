def calculate_trip():
    print("Welcome to the Tip Calculator!")

    try:
       bill = float(input("What was the total bill? $ ").strip())
       people = int(input("How many people to split the bill? ").strip())

       if bill <= 0 or people <= 0:
           print("Please enter valid positive numbers.")
           return

       while True:
           tip_percent = float(input("Tip percentage (10, 12, 15)? ").strip())

           if tip_percent  in [10, 12, 15]:
               break
           else:
               print("Invalid choice. Please enter 10, 12, or 15.")

       tip_amount = bill * (tip_percent / 100)
       total_bill = bill + tip_amount
       per_person = total_bill / people

       print(f"Each person should pay: ${per_person:.2f}")

       if tip_percent not in [10, 12, 15]:
           print("Please choose 10, 12, or 15 only.")
           return

    except ValueError:
        print("Invalid input! Please enter numbers only.")


calculate_trip()
