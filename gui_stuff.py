import math
import tkinter as tk
from tkinter import * 

#establishing the window

calc = tk.Tk()
calc.title('calculator')

calc.geometry("950x900")

calc.configure(background='black')

#screen variable

visibleValues = ""
mathValues = ""

#establishing 'screen'

text= Text(calc, width= 73, height= 5, background=
"gray71",foreground="#fff",font= ('Sans Serif', 13, 'italic bold'))

text.place(x = 150, y = 100)

text.insert(INSERT, visibleValues)



#button functions


def oneButton():
        global mathValues
        mathValues = mathValues + "1"
        text.insert(INSERT, visibleValues + " 1")
        print(mathValues)

def twoButton():
        global mathValues
        mathValues = mathValues + "2"
        text.insert(INSERT, visibleValues + " 2")
        print(mathValues)

def threeButton():
        global mathValues
        mathValues = mathValues + "3"
        text.insert(INSERT, visibleValues + " 3")
        print(mathValues)

def fourButton():
        global mathValues
        mathValues = mathValues + "4"
        text.insert(INSERT, visibleValues + " 4")
        print(mathValues)
def fiveButton():
        global mathValues
        mathValues = mathValues + "5"
        text.insert(INSERT, visibleValues + " 5")
        print(mathValues)

def sixButton():
        global mathValues
        mathValues = mathValues + "6"
        text.insert(INSERT, visibleValues + " 6")
        print(mathValues)

def sevenButton():
        global mathValues
        mathValues = mathValues + "7"
        text.insert(INSERT, visibleValues + " 7")
        print(mathValues)

def eightButton():
        global mathValues
        mathValues = mathValues + "8"
        text.insert(INSERT, visibleValues + " 8")
        print(mathValues)

def nineButton():
        global mathValues
        mathValues = mathValues + "9"
        text.insert(INSERT, visibleValues + " 9")
        print(mathValues)

def plusButton():
        global mathValues
        mathValues = mathValues + "+"
        text.insert(INSERT, visibleValues + " +")
        print(mathValues)

def minusButton():
        global mathValues
        mathValues = mathValues + "-"
        text.insert(INSERT, visibleValues + " -")
        print(mathValues)

def equalsButton():
        global mathValues
        text.delete(1.0,END)

        try:
                text.insert(INSERT, eval(mathValues))
        except SyntaxError:
                text.insert(INSERT, "syntax error - integer may start with zero")
        
def multiplyButton():
        global mathValues      
        mathValues = mathValues + "*"
        text.insert(INSERT, visibleValues + " x")
        print(mathValues)

def divideButton():
        global mathValues
        mathValues = mathValues + "/"
        text.insert(INSERT, visibleValues + "÷")
        print(mathValues)

def clearButton():
        global mathValues
        mathValues = ""
        text.delete(1.0,END)

def zeroButton():
        global mathValues      
        mathValues = mathValues + "0"
        text.insert(INSERT, visibleValues + " 0")
        print(mathValues)

def openBracketButton():
        global mathValues      
        mathValues = mathValues + "("
        text.insert(INSERT, visibleValues + " (")
        print(mathValues)

def closeBracketButton():
        global mathValues
        mathValues = mathValues + ")"
        text.insert(INSERT, visibleValues + " )")
        print(mathValues)

def squaredButton():
        global mathValues       
        mathValues = mathValues + "**2"
        text.insert(INSERT, visibleValues + "^2")
        print(mathValues)

def powerOfXButton():
        global mathValues       
        mathValues = mathValues + "**"
        text.insert(INSERT, visibleValues + "^")
        print(mathValues)



        


       


#establishing buttons

one = tk.Button( 
                calc,
                text = "1",
                bg = "orange",
                bd = 5,
                height = 10,
                width = 17,
                command = oneButton,
                        )

one.place(x = 150,y = 600)


two = tk.Button( 
                calc,
                text = "2",
                bg = "orange",
                bd = 5,
                height = 10,
                width = 17,
                command = twoButton,
                        )

two.place(x = 300,y = 600)

three = tk.Button( 
                calc,
                text = "3",
                bg = "orange",
                bd = 5,
                height = 10,
                width = 17,
                command = threeButton,
                        )

three.place(x = 450,y = 600)

four = tk.Button( 
                calc,
                text = "4",
                bg = "orange",
                bd = 5,
                height = 10,
                width = 17,
                command = fourButton,
                        )

four.place(x = 150,y = 410)

five = tk.Button( 
                calc,
                text = "5",
                bg = "orange",
                bd = 5,
                height = 10,
                width = 17,
                command = fiveButton,
                        )

five.place(x = 300,y = 410)

six = tk.Button( 
                calc,
                text = "6",
                bg = "orange",
                bd = 5,
                height = 10,
                width = 17,
                command = sixButton,
                        )

six.place(x = 450,y = 410)

seven = tk.Button( 
                calc,
                text = "7",
                bg = "orange",
                bd = 5,
                height = 10,
                width = 17,
                command = sevenButton
                        )

seven.place(x = 150,y = 220)

eight = tk.Button( 
                calc,
                text = "8",
                bg = "orange",
                bd = 5,
                height = 10,
                width = 17,
                command = eightButton
                        )

eight.place(x = 300,y = 220)

nine = tk.Button( 
                calc,
                text = "9",
                bg = "orange",
                bd = 5,
                height = 10,
                width = 17,
                command = nineButton,
                        )

nine.place(x = 450,y = 220)

plus = tk.Button( 
                calc,
                text = "+",
                bg = "red",
                bd = 5,
                height = 10,
                width = 12,
                command = plusButton,
                        )

plus.place(x = 600,y = 220)

minus = tk.Button( 
                calc,
                text = "-",
                bg = "red",
                bd = 5,
                height = 10,
                width = 12,
                command = minusButton,
                        )

minus.place(x = 600,y = 410)

equals = tk.Button( 
                calc,
                text = "=",
                bg = "red",
                bd = 5,
                height = 10,
                width = 12,
                command = equalsButton,
                        )

equals.place(x = 600,y = 600)

multiply = tk.Button( 
                calc,
                text = "x",
                bg = "red",
                bd = 5,
                height = 10,
                width = 12,
                command = multiplyButton,
                        )

multiply.place(x = 710,y = 220)

divide = tk.Button( 
                calc,
                text = "÷",
                bg = "red",
                bd = 5,
                height = 10,
                width = 12,
                command = divideButton,
                        )

divide.place(x = 710,y = 410)

clear = tk.Button( 
                calc,
                text = "del",
                bg = "red",
                bd = 5,
                height = 10,
                width = 12,
                command = clearButton,
                        )

clear.place(x = 710,y = 600)

zero = tk.Button( 
                calc,
                text = "0",
                bg = "red",
                bd = 5,
                height = 4,
                width = 17,
                command = zeroButton,
                        )

zero.place(x = 150,y = 780)

openBracket = tk.Button( 
                calc,
                text = "(",
                bg = "red",
                bd = 5,
                height = 4,
                width = 17,
                command = openBracketButton,
                        )

openBracket.place(x = 300,y = 780)

closeBracket = tk.Button( 
                calc,
                text = ")",
                bg = "red",
                bd = 5,
                height = 4,
                width = 17,
                command = closeBracketButton,
                        )

closeBracket.place(x = 450,y = 780)

squared = tk.Button( 
                calc,
                text = "^2",
                bg = "red",
                bd = 5,
                height = 4,
                width = 12,
                command = squaredButton,
                        )

squared.place(x = 600,y = 780)

powerOfX = tk.Button( 
                calc,
                text = "^(x)",
                bg = "red",
                bd = 5,
                height = 4,
                width = 12,
                command = powerOfXButton,
                        )

powerOfX.place(x = 710,y = 780)
































calc.mainloop()