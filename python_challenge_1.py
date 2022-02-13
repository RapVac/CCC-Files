##Can you get the flag?

import time

establish = [36, 49, 109, 112, 108, 51, 95, 114, 51, 86, 51, 114, 115, 51, 95, 51, 110, 103, 49, 110, 69, 69, 82, 49, 78, 71, 95, 57, 51, 53]

while True:
    
    user_input = str(input('What is the password? '))
    
    if user_input == 'password123':
        
        print('Password is correct! Printing flag now. . .')
        
        for x in range(0, 3):
            print('.')
            time.sleep(1)
            
        print("Get ready to write it down!")
        time.sleep(1)

        for y in range(len(establish)):
             establish[y] = chr(establish[y])
        
        print("".join(establish))
        time.sleep(0.5)
        print("Don\'t forget to submit in CyberCTF{xxxxx} format!")
            
        break
    else:
        print("Wrong! Try again.")
        time.sleep(2)
