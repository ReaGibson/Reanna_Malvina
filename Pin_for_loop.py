
#hardcoded PIN
correct_pin = "1234"
max_attempts = 3

#starting loop with 3 attempts
# 'for' loop which runs for a specific number of attempts. range is going from 1-max attempts (because it counts from 0 you need to +1 inorder to count to 3)
for attempts in  range(1, max_attempts +1):
    #ask user to input their pin.
    supplied_pin = input(f"Attempt {attempts}/{max_attempts} - Enter Pin Here:")
    #Checks if the entered pin is correct
    if supplied_pin == correct_pin:
        print(f"Pin correct! {attempts}")
        break #exit the loop when the correct pin has been entered
    else:
        print("Pin incorrect Please try again.")
