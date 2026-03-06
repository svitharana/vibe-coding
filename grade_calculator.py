def main():
    # Input student details
    name = input("Enter Student's name: ")
    
    try:
        # Input marks for 3 subjects
        maths = float(input("Enter marks for Maths: "))
        science = float(input("Enter marks for Science: "))
        english = float(input("Enter marks for English: "))
        
        # Calculate average
        average = (maths + science + english) / 3
        
        # Display results
        print(f"\nStudent Name: {name}")
        print(f"Average Marks: {average:.2f}")
        
        if average >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")
            
    except ValueError:
        print("Error: Please enter valid numerical marks.")

if __name__ == "__main__":
    main()
