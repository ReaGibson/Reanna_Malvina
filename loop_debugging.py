#defining variable's
i = 45
j = 12

#'while' is a loop structure. this means that as long as the condition ('i' is less than 42) is true the loop will keep running
while i < 42:
    i = i * 2 #every time the loop runs 'i' is multiplied by 2
    if i > j: # this means that once 'i' is bigger than 'j' the loop will break/finish
        break #control statement - this interrupts and exits the loop immediately

#'else' will only  run if the initial 'while' condition is 'false'. ('i' is bigger than 42)
#only print if the loop doesn't run
else: # 'i' > 42 (meaning initial condition is false)
    print("Loop expired: ", i)

#this print command will always execute,regardless of if the loop ran or not
#once 'i' is larger than 'j' after running the loop it will print the final value of 'i' after all the operations
print("Final value: ", i)