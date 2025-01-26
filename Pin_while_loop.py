# Hardcoded PIN (as a string)
correct_pin = "1234"
max_attempts = 3
attempts = 1  # Start at the first attempt

# Start the loop while the number of attempts is less than or equal to max_attempts
while attempts <= max_attempts:
    # Ask user to input their pin
    supplied_pin = input(f"Attempt {attempts}/{max_attempts} - Enter Pin Here: ")

    # Compare the entered PIN (as a string) with the correct PIN
    if supplied_pin == correct_pin:
        print(f"Pin correct! Attempt {attempts}")
        break  # Exit the loop when the correct pin has been entered
    else:
        print("Pin incorrect. Please try again.")

    attempts = attempts + 1 # Causes the counter to go up with each attempt

# If all attempts are used and the PIN was not correct
if attempts > max_attempts:
    print("Sorry, you've used all your attempts!")