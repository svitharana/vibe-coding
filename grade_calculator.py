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
            
            # Display results
            print(f"Average Marks: {average:.2f}")
            
            if average >= 75:
                print("Grade: A")
            elif average >= 60:
                print("Grade: B")
            elif average >= 40:
                print("Grade: C")
            else:
                print("Result: Fail")
                
        except ValueError:
            print("Error: Please enter valid numerical marks.")

if __name__ == "__main__":
    main()
