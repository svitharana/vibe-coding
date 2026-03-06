def main():
    while True:
        # Input student details
        name = input("\nEnter Student's name (or type 'Exit' to quit): ")
        
        if name.lower() == 'exit':
            break
        
        try:
            # Input marks for 3 subjects
            maths = float(input("Enter marks for Maths: "))
            science = float(input("Enter marks for Science: "))
            english = float(input("Enter marks for English: "))
            
            # Calculate average
            average = (maths + science + english) / 3
            
            # Determine grade/result
            if average >= 75:
                result = "A"
            elif average >= 60:
                result = "B"
            elif average >= 40:
                result = "C"
            else:
                result = "Fail"

            # Display results
            print("-" * 24)
            print(f"Name: {name}")
            print(f"Average: {average:.1f}")
            print(f"Grade: {result}")
            print("-" * 24)
                
        except ValueError:
            print("Error: Please enter valid numerical marks.")

if __name__ == "__main__":
    main()
