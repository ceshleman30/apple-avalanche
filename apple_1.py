#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.bgpic("background.gif")
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
apple.penup()

letterlist = ["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H", "I" , "J" , "K" , "L" , "M" , "N" , "O" , "P" , "Q" , "R" , "S", "T" , "U" , "V" , "W" , "X" , "Y" , "Z"]
apple_list = []
apple_letters = []

currletter = ""

number_of_apples = 5

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple , letter):
  active_apple.shape(apple_image)
  active_apple.showturtle()
  wn.update()
  draw_letter(active_apple, letter)

# make apple fall
def apple_fall(letter):
  index = apple_letters.index(letter)
  apple_letters.pop(index)
  active_apple = apple_list
  x = apple.xcor()
  y = apple.ycor()
  while (y >= -300):
    y = y - 25
    apple.goto(x , y)
    active_apple.clear()
  apple.hideturtle()
  resetapple(apple)

# This function takes care of font and color. 
def draw_letter(active_apple, letter):
  x = active_apple.xcor()
  y = active_apple.ycor()
  x = x - 23
  y = y - 50
  active_apple.goto(x , y)
  active_apple.color("white")
  active_apple.write(letter , font=("Arial", 55, "bold")) 
  wn.onkeypress(apple_fall, currletter.lower())


#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the 
# turtle with a new letter selected at random from the list of letters
def resetapple(active_apple):
  global currletter
  if (len(letterlist) != False):
    active_apple.goto(rand.randint(-200 , 200) , rand.randint(0 , 150))
    currletter = letterlist.pop(rand.randint(0 , len(letterlist) - 1))
    draw_apple(active_apple, currletter)
    apple_letters.append(currletter)


#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)

#TODO Create a function that takes a turtle (apple) and its corresponding ltter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.

for i in range(0, number_of_apples):
  #Your code here
  active_apple = trtl.Turtle(shape = apple_image)
  active_apple.penup()
  resetapple(active_apple)
  apple_list.append(active_apple)

#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the 
# apple and letter have dropped, call the apple reseting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.

#-----function calls-----
resetapple(apple)


wn.listen()
wn.mainloop()