#!/usr/bin/env python3

# == step 0: import dependencies ==
import PySimpleGUI as sg

# == step 1: set variables ==
# TODO better encapsulate these fields into a Calculator object
currentToken = ''
currentTokenAsInt = 0
Beforefinished = 0
Afterfinished = 0


numberList = []
operatorList = []

# == step 2: PSG setup ==
# Under the current design, this needs to happen sooner in order for the actual
# calculator business logic to update the "Answer" indicator

sg.change_look_and_feel('DarkAmber')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('God has left us, and programming is why - the calculator version')],
            [sg.Text(size=(64, 1), key="ACC")],
            [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('+')],
            [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('-')],
            [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('/')],
            [sg.Button('0')],
            [sg.Button('ANS'), sg.Button('CE'), sg.Button('x'), sg.Button('*')],
            [sg.Button('GOD MAKE IT STOP PLEASE STOP IT')]]

# Create the Window
window = sg.Window('Window Title', layout)

# == step 3: calculator business logic ==
def evaluateFullExpression():
    accumulator = numberList[0]
    for i in range(0, len(numberList)-1):
        # TODO make an enum type for the OPERATOR
        # it's times like these when
        # I wish python 3 had a built-in switch/case feature...
        if operatorList[i] == "+":
            accumulator = accumulator + numberList[i+1]
        elif operatorList[i] == "-":
            accumulator = accumulator - numberList[i+1]
        elif operatorList[i] == "*":
            accumulator = accumulator * numberList[i+1]
        elif operatorList[i] == "/":
            if (numberList[i+1] == 0):
                print("ERR: Division by zero detected!")
                exit()
            else:
                accumulator = accumulator / numberList[i+1]
        else:
            print("ERR: button identifier %s not supported" % operatorList[i])
    return accumulator

# A function that responds to each button click (determined by its unique
#     identifier) by updating the relevant lists.
def process_next_button(identifier):
    # I still hate this "globals" practice and think we should refactor it
    #     into an object or something
    global currentTokenAsInt
    global currentToken
    global numberList
    global operatorList
    if (identifier == None or len(identifier) < 1):
        print("ERR: button identifier is read as None or empty string. Check button definitions.")
    elif (identifier[0] >= '0' and identifier[0] <= '9'): 
        # Note: the above checks are deliberate. We want to use ASCII values
        # (namely 48 and 57 in decimal) for the CHARACTERS '0' through '9'
        # notice, this ensures that currentTokenAsInt is a String type
        currentToken = currentToken + identifier
        currentTokenAsInt = int(currentToken)
        print(currentToken)
    elif (identifier == "ANS"):
        numberList.append(currentTokenAsInt)
        accumulator = evaluateFullExpression()
        print(accumulator)

        # here, we want to clear all variables to their defaults
        numberList = []
        operatorList = []
        currentToken = ""
        currentTokenAsInt = 0
        # update the GUI with the accumulator somehow
        window['ACC'].update('ANS: '+str(accumulator))
    else:
        # we delay evaluation until 'ANS' button is clicked
        numberList.append(currentTokenAsInt)
        operatorList.append(identifier)
        currentToken = ""
        currentTokenAsInt = 0
#        print(numberList)
#        print(operatorList)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'GOD MAKE IT STOP PLEASE STOP IT'):	# if user closes window or clicks cancel
        break
    # extract the actual identifier for the button pressed;
    # pass it in as parameter.
    process_next_button(event)

window.close()

