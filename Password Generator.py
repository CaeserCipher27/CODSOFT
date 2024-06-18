import random

logo = ''' ___   __    __   __  _   _   __   ___  __     __  ___  __  _  ___  ___   __  _____  __   ___  
| _,\ /  \ /' _//' _/| | | | /__\ | _ \| _\   / _]| __||  \| || __|| _ \ /  \|_   _|/__\ | _ \ 
| v_/| /\ |`._`.`._`.| 'V' || \/ || v /| v | | [/\| _| | | ' || _| | v /| /\ | | | | \/ || v / 
|_|  |_||_||___/|___/!_/ \_! \__/ |_|_\|__/   \__/|___||_|\__||___||_|_\|_||_| |_|  \__/ |_|_\     '''

all_ = ['a', 'b', 'c', 'd', '5', '6', '7', '8', '9', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', ')', '*', '+', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
        'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4',
        '!', '#', '$', '%', '&', '(']

another_pass = None
flag = True

print("Welcome to Python Password Generator")
print(logo)


def Generated():
    global another_pass, flag
    length = int(input("Specify the length of Password: "))
    password = ""
    for i in range(0, length):
        password += random.choice(all_)
    print(f"\nYour Password is {password}\n")
    another_pass = input("Do you wish to generate another password?\n(Yes/No)\n").lower()
    if another_pass == 'yes':
        Generated()
    else:
        flag = False
        print('Thank You for using Python Password Generator!')


Generated()
