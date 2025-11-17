from circuit_builder import quantum_random_number_generator
number = int(input("Input the upper limit of the range of numbers: "))
# unknown_number
x = quantum_random_number_generator(number)
iteration = 0
while True:
    iteration += 1
    y = int(input("Enter your guess: "))

    if y > x:
        print("Your guess is greater than the unknown number")
    elif y < x:
        print("Your guess is lesser than the unknown number")
    else:
        print("Congrats! Your guess is correct!")
        break
print(f"You took {iteration} guesses!")