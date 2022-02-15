##Want to play with my new Chemistry set?

import time
import base64 as new_fun

liquids = "red orange yellow green blue purple pink".split()

establish = "KEZWY2K2LBFEIVSFLI3VU6SRPJSEIRTVLIYTS2KNGNJDAWSYJJTE4SCSMZRWUTRSJUZUU6SNK42W4WD2NM2U6RCJGBGTGMB5"

liquids_formatted = ", ".join(liquids)





def ask():
    print('''You have %s liquids:
%s''' % (len(liquids), liquids_formatted))
    amount = int(input('''How many would you like to mix?
'''))
    return amount

def which_mix(amount):
    your_choices = []
    for x in range(amount):
        
        if len(your_choices) > 0:
            order = 'next'
        else:
            order = 'first'

        time.sleep(0.5)
        sub = str(input('''Which color do you mix %s?
''' % order))
        
        if sub not in liquids:
            print("Please enter a color we have.")
            break
            
        else:
            time.sleep(0.5)
            print("Adding to vial...")
            your_choices.append(sub)


        if your_choices == ['red', 'blue', 'orange'] and amount == 3:
            time.sleep(0.5)
            print("Here's the flag!")
            print(new_fun.b64decode(new_fun.b32decode(establish)))
                

num = ask()
which_mix(num)

##print(ask())
