print('''

                      _________________________
                  __ /  ,------++---. .-------.`.
                    /  /      //    | ||       |.`.
                __ /  /      //     | ||       | `.`.
               __ |  '------++------' |`-------+--[)| `---..___
               __ !]            _     |             |    ______"""-.
                 _!]__________ |_|    |             |   ,,----.\___|_
                 |___ /',--. \\       |_____________|  // ,--.\\____|
                  \_-/'|    |! \----------------------'| |    |!|_/
                      \ `--' /!'----------------------' \ `--' /
                       `'---'                            `'---'

''')
print("Welcome to Treasure Hunting!\n")
print("Your mission in to find the treasure.")

left = input('There is two caves, where you want to go? "LEFT" or "RIGHT"? \n').upper()
if left == "LEFT":
    wait = input('Inside the cave there is a pond, "SWIM" or "WAIT"? \n').upper()
    if wait == "WAIT":
        yellow = input('Then mysterious door appear, which door? "RED" "YELLOW" "BLUE" \n').upper()
        if yellow == "YELLOW":
            print("Congratulations! you win a iphone 15+ promax 1terra storage")
        elif yellow  == "BLUE":
            print("Game Over! inside this door is a piece of blue dust")
        else:
            print("Game Over! inside this door is red dust.")
    else:
        print("Game Over! pond is deep, you don't know how to swim!")
else:
    print("Game Over! This cave have a dynamite blowing on you!")       




