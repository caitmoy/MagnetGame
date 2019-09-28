# Game in which the player must make it through a 'normal' Magnet school day

class Character(object):
    """character template"""
    def __init__(self, name):
        self.name = name
        self.gp = 100 # gp stands for "grade points"
        self.sp = 100 # sp stands for "self-esteem points"

    def bang_head_against_wall(self):
        """deducts 5 points from sp"""
        self.sp -= 5
        print(input('''You lost 5 self-esteem points.

[ENTER]'''))

    def powerschool(self):
        """Displays how many self-esteem/grade points the player has"""
        print(input(f'''You have {you.sp}/100 self-esteem points.
You have {you.gp}/100 grade points.

[ENTER]'''))

you = Character("you") # How the player is referred to the entire game

def end_game():
    """checks if player's sp/gp is less than or equal to zero"""
    if you.sp <= 0 or you.gp <= 0:
        print(input('''Magnet is too much for you.

You go back to your home district.

[ENTER]''')) # displayed if amounts are negative
        print("\033[H\033[J")
        print(input('Press [ENTER] to try again'))
        choice_1() # player can restart game

# Game introduction
print(input('''Welcome to Magnet: The Game!

It's an A day. Can you make it all the way to 2:50?

To continue, press [ENTER]'''))  # press ENTER to advance


# Choice_1: Has two options
# If the player inputs anything other than 'a' or 'b', the question will repeat itself
def choice_1():
    you.sp = 100  # resets sp value to 100 if the player plays the game multiple times
    you.gp = 100  # resets gp value to 100 if the player plays the game multiple times
    print("\033[H\033[J") # used throughout to clear the screen
    choice = ""
    while choice != "a" and choice != "b":
        choice = input('''The lovely smell of bus fumes at 7:55 AM fills the air. You know you’re a slow walker.
Do you cut across the grass like a barbarian, or walk along the pathway?
 a  I’m a barbarian
 b  Walk along pathway

Type a or b: ''')

    if choice is "a":
        print("\033[H\033[J")
        print(input('''You cut across the grass and trip on a rock. Good. You deserve it.

[ENTER]'''))
        choice_2()  # leads to choice_2

    if choice is "b":
        print("\033[H\033[J")
        print(input('''You walk the entire length of the pavement, taking in your surroundings.

The sun illuminates the sky. A flock of geese fly by. The gnome in the window of the magnet senior lounge waves “hi.”

[ENTER] '''))
        print("\033[H\033[J")
        print(input('''You’re so lost in the moment that you trip over a student who stopped to tie his shoelaces in the middle of the path.

You break your nose.

Minus 10 self-esteem points.

[ENTER]'''))
        you.sp -= 10  # subtracts 10 sp
        choice_2()  # leads to choice_2

# Choice_2: Has two options


def choice_2():
    print("\033[H\033[J")
    choice = ""
    while choice != "a" and choice !="b":
        print(input('''You approach the front doors of Magnet. Someone holds the door open for you. You give them a pat on the back.

[ENTER]'''))
        print("\033[H\033[J")
        choice = input('''You go to swipe in, but realize your lanyard isn’t hanging around your neck.

Do you wear a temporary ID or not?

 a  Wear temporary ID
 b  Don't wear temporary ID

 Type a or b: ''')

    if choice is "a":
        print("\033[H\033[J")
        print(input('''You wear your temporary ID. Three freshmen walk by and make fun of you.

Minus 10 self-esteem points.

[ENTER]'''))
        you.sp -= 10  # subtracts 10 sp
        print("\033[H\033[J")
        print(input('''You see Betia waving to you from down the hallway

[ENTER]'''))
        print("\033[H\033[J")
        print(input('''Betia: Hey! Did you know if you check Powerschool you can see how many self-esteem points and grade points you have?!?

[ENTER]'''))
        print(input('''You: What?

[ENTER]'''))
        print(input('''Betia: What?

[ENTER]'''))
        print(input('''Betia: *Barrel-rolls away*

[ENTER]'''))
        print("\033[H\033[J")
        print(input(''' You continue on to your locker on the second floor

[ENTER]'''))
        choice_3()  # leads to choice_3

    if choice is "b":  # GAME END
        print("\033[H\033[J")
        print(input('''You take the green sticker, rip it in half and stomp on it.

[ENTER]'''))
        print("\033[H\033[J")
        print(input('''Mr. Rafalowski sees the whole thing and lets out a disapproving sigh.

[ENTER]'''))
        print("\033[H\033[J")
        print(input('''You try to tape the pieces back together, but in doing so, you lose all your dignity.

Minus 100 self-esteem points.

[ENTER]'''))
        you.sp -= 100  # subtracts 100 sp
        end_game()  # game will end


# Choice_3: Has three choices
def choice_3():
    print("\033[H\033[J")
    choice = ""
    while choice != "a" and choice != "b" and choice != "c":
        choice = input('''Do you remember your locker combination?

 a  10-14-35
 b  Nope
 c  Check powerschool

Type a, b, or c: ''')
        if choice is "a":
            print("\033[H\033[J")
            print(input('''You remembered correctly!

Plus 5 self-esteem points.

[ENTER]'''))
            you.sp += 5  # plus 5 sp
            print("\033[H\033[J")
            print(input('''You open up your locker only to find a void of empty space.
Oh that's right, you don’t use your locker anyway.

[ENTER]'''))
            print("\033[H\033[J")
            print(input('''...
It's 7:59! You have one minute to get to class.

[ENTER]'''))
            print("\033[H\033[J")
            print(input('''You hurry over to English.
Once you get there, you see Ms. Arnold passing out tests.

You sit down and open up a textbook for some last-minute studying, but when you open it, you find what looks like the answer key stuck in the pages!

[ENTER]'''))

            choice_4()  # leads to choice_4
        if choice is "b":  # GAME END
            print("\033[H\033[J")
            print(input('''You don’t remember, so you try every possible combination of numbers sequentially.

[ENTER]'''))
            print(input('''Life goes on.

[ENTER]'''))
            print(input('''You finally get the correct combination, but everyone has graduated high school already.

Minus 100 self-esteem points.

[ENTER]'''))
            you.sp -= 100  # subtracts 100 sp
            end_game()  # game will end
        if choice is "c":
            print("\033[H\033[J")
            you.powerschool()  # checks powerschool
            choice_3()  # back to choice_3


# Choice_4: Has 3 choices
def choice_4():
    print("\033[H\033[J")
    choice = ""
    while choice != "a" and choice != "b" and choice != "c":
        choice = input('''Do you cheat and use the answer key?

 a  Yes
 b  No
 c  powerschool

Type a, b, or c: ''')
        if choice is "a":
            print("\033[H\033[J")
            print(input('''You hide the key underneath your desk and copy down the answers exactly...

    1. C, 2. C, 3. C, 4. C, 5. C...

[ENTER]'''))
            print(input('''But the questions were all "True or False."

Minus 50 grade points.

[ENTER]'''))
            you.gp -= 50  # subtract 50 gp
            print("\033[H\033[J")
            print(input('''BELL BELL BELL

You leave English. It's been a stressful morning.

[ENTER]'''))
            choice_5()  # leads to choice_5
        if choice is "b":
            print("\033[H\033[J")
            print(input('''You remember the academic honesty policy that you signed at the beginning of the year and choose not to cheat.

But you didn't study anyway.

Minus 20 grade points.

[ENTER]'''))
            you.gp -= 20  # subtracts 20 gp
            print("\033[H\033[J")
            print(input('''BELL BELL BELL

You leave English. It's been a stressful morning.

[ENTER]'''))
            choice_5()  # leads to choice_5

        if choice is "c":
            print("\033[H\033[J")
            you.powerschool()  # checks powerschool
            choice_4()  # leads to choice_4


# Choice 5: three options
def choice_5():
    end_game()  # possible game end, depending on how many times player repeats
    print("\033[H\033[J")
    choice = ""
    while choice != "a" and choice != "b" and choice != "c":
        choice = input('''**You’ve learned a new coping mechanism!**

[bang_head_against_wall]

Use now?

 a  Yes
 b  No

Type a or b: ''')
        if choice is "a":
            print("\033[H\033[J")
            you.bang_head_against_wall()  # subtracts 5 sp
            choice_6()  # leads to choice_6

        if choice is "b":
            print("\033[H\033[J")
            print(input('''You make it to your ¾ class– Tech.

Before you can sit down and open up your chromebook, you hear the fire alarm!
The clock is flashing FIRE FIRE FIRE. You walk over to the doorway.

[ENTER]'''))
            choice_7()  # leads to choice_7


# Choice_6: three options
def choice_6():
    end_game()  # possible game end, depending on how many times player repeats
    print("\033[H\033[J")
    choice = ""
    while choice != "a" and choice != "b" and choice != "c":
        choice = input('''Repeat?

 a  Bang head against wall again
 b  Have a little self-respect
 c  Powerschool

Type a, b, or c: ''')
        if choice is "a":
            print("\033[H\033[J")
            you.bang_head_against_wall()  # subtracts 5 sp
            choice_6()  # leads to choice_6
        if choice is "b":
            print("\033[H\033[J")
            print(input('''You make it to your ¾ class– Tech.

Before you can sit down and open up your chromebook, you hear the fire alarm!
The clock is flashing FiRE FiRE FiRE. You walk over to the doorway.

[ENTER]'''))
            choice_7()  # leads to choice_7
        if choice is "c":
            print("\033[H\033[J")
            you.powerschool()  # checks powerschool
            choice_6()  # back to choice_6


# Choice 7: three options
def choice_7():
    print("\033[H\033[J")
    choice = ""
    while choice != "a" and choice != "b" and choice != "c":
        choice = input("""Do you know how to make it out of the building?

 a  left, forward, left
 b  right, forward, left
 c  right, right, right
 d  Powerschool

Type a, b, c, or d: """)

        if choice is "a":
            print("\033[H\033[J")
            print(input('''Good thing Magnet’s floorplan is essentially a circle. You do a lap around the first floor and then join the class outside under the AIT bridge.

[ENTER]'''))
            print("\033[H\033[J")

            print(input('''Safely outside, you stand in a line with your classmates.

You take a look around. It’s been 2 and half hours since you’ve been outside and the expanse of the wilderness inspires you.

You realize you could do anything at this moment.

Self-esteem? Grades? What’s the point?

[ENTER]'''))
            choice_8()  # leads to choice_8
        if choice is "b":
            print("\033[H\033[J")

            print(input('''You push your fellow classmates down and make a break for the exit.

[ENTER]'''))
            print("\033[H\033[J")

            print(input('''Safely outside, you stand in a line with your classmates.

You take a look around. It’s been 2 and half hours since you’ve been outside and the expanse of the wilderness inspires you.

You realize you could do anything at this moment.

Self-esteem? Grades? What’s the point?

[ENTER]'''))
            choice_8()  # leads to choice_8
        if choice is "c":
            print("\033[H\033[J")
            print(input('''You panic and walk in a circle. You are blocking the exit to the classroom.

Ms. Gerstein is forced to drag your body outside so that the rest of the class can get through.

Minus 10 self-esteem points.

[ENTER]'''))
            you.sp -= 10  # subtracts 10 sp
            print("\033[H\033[J")
            print(input('''Safely outside, you stand in a line with your classmates.

You take a look around. It’s been 2 and half hours since you’ve been outside and the expanse of the wilderness inspires you.

You realize you could do anything at this moment.

Self-esteem? Grades? What’s the point?

[ENTER]'''))
            choice_8()  # leads to choice_8

        if choice is "d":
            print("\033[H\033[J")
            print('You check your grades in this time of crisis.')
            you.powerschool()  # checks powerschool
            choice_7()  # leads to choice_7


# Choice 8: three options
def choice_8():
    print("\033[H\033[J")
    choice = ""
    while choice != "a" and choice != "b" and choice != "c":
        choice = input('''The world is your oyster.

 a  Run
 b  Cry
 c  Powerschool
 d  Bang head against wall

Type a, b, c, or d: ''')
        if choice is "a":  # WINNING GAME END
            print("\033[H\033[J")
            print(input('''You rip off your temporary ID and toss it into the wind. You run north.

Everyone calls out after you, but you don't listen. You feel the cool air of Scotch Plains filling your lungs as you continue to sprint away in a single direction.

Your self-esteem points and grade points max out. You are elevated to a higher level of existence.

YOU WIN

Press [ENTER] to play again'''))
            choice_1()  # goes back to start

        if choice is "b":  # LOSING GAME END
            print("\033[H\033[J")
            print(input('''A single tear glides down your cheek.

Everything is just so beautiful.

Life is so overwhelming. Suddenly, Janessa slaps you across the face and shouts, "Get a grip, man!!"

But you don't want to.

Minus 476 self-esteem points.
Minus 298 grade points.

THE END

Press [ENTER] to play again'''))
            choice_1()  # goes back to choice_1

        if choice is "c":  # won't access powerschool
            print("\033[H\033[J")
            print(input('''[Powerschool is closed]

[ENTER]'''))
            choice_8()  # back to choice_8
        if choice is "d":  # possible game end
            print("\033[H\033[J")
            you.bang_head_against_wall()
            end_game()
            choice_8()  # back to choice_8


choice_1()  # starts the game
