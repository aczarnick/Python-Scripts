# Worker function that prompts user for inputs and stores answers
def calculateGPA():
    numberOfClasses = int(input("How many classes are you taking this semester? "))

    classList = []
    for i in range(1, numberOfClasses + 1):
        #Get the grade Ex: A, b, c+
        rawGrade = input(f"What grade did you get in class {i}? ")

        # Get the number of credits Ex: 1, 3, 5
        rawCredits = int(input(f"How many credits is class {i}? "))

        # Use a dictionary to get the numeric value of the letter
        numericGrade = CheckInput(rawGrade.lower())

        # Using a list we ara appending a tuple with three values.
        # they are in order ("A", 4.0, 3)
        classList.append((rawGrade.upper(), numericGrade, rawCredits))

    return classList

# returns the value of a dictionary based on the 
# passed key into it. A quicker way of doing if/else
def CheckInput(input):
    return {
        "a+" : 4.0,
        "a"  : 4.0,
        "a-" : 3.7,
        "b+" : 3.3,
        "b"  : 3.0,
        "b-" : 2.7,
        "c+" : 2.3,
        "c"  : 2.0,
        "c-" : 1.7,
        "d+" : 1.3,
        "d"  : 1.0,
        "d-" : 0.7,
        "f"  : 0.0,
    }[input]


def printResult(classList):
    # Printing your header
    print("\nThe courses you entered are:")
    print("Grades\t\tHours")
    
    # creating your inits
    totalCredits = 0
    gpaSum = 0
    for item in classList:
        ## adding the third item of the tuple (second index) 
        totalCredits += item[2]

        # Calculating your GPA by multiplying your credits and numeric grade
        gpaSum += (item[1] * item[2])

        # Print for the user to see
        print(f"{item[0]}\t\t{item[2]}")

    # final calculation of all GPA sums divided by your total credits
    semesterGpa = round(gpaSum/totalCredits, 2)

    # Final semester GPA print for the user
    print(f"Your GPA is {semesterGpa}.")

# Entry point into the program
def main():
    classList = calculateGPA()
    printResult(classList)


# this is a best practice when writing scripts
# BUT NOT NECESSARY
if __name__ == "__main__":
  main()