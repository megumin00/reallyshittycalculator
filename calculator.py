import PySimpleGUI as sg
#calculations

current = ''
valuecurrent = 0
Beforefinished=0
Afterfinished=0


numberList = []
operatorList = []

def calculation(numberList, operatorList):
    storeNumber = int(numberList[0])
    for i in range(0, len(numberList)-1):
        if operatorList[i] == "+":
            storeNumber = storeNumber + int(numberList[i+1])
        elif operatorList[i] == "-":
            storeNumber = storeNumber - int(numberList[i+1])
        elif operatorList[i] == "*":
            storeNumber = storeNumber * int(numberList[i+1])
        elif operatorList[i] == "/":
            storeNumber = storeNumber / int(numberList[i+1])
    return storeNumber

def numbers(value):
    if event in (None, value):
        global valuecurrent
        global current
        #makes it into a string
        valuecurrent=value
        current = current + valuecurrent
        valuecurrent = current
        print(current)

def symbols(types):
    if event in (None, types):
        global current
        global valuecurrent
        numberList.append(current)
        operatorList.append(types)
        current=''
        valuecurrent=''
        print(numberList)
        print(operatorList)
        
def unspaghettify_this():    
    numbers('1')
    numbers('2')
    numbers('3')
    numbers('4')
    numbers('5')
    numbers('6')
    numbers('7')
    numbers('8')
    numbers('9')
    symbols('+')
    symbols('-')
    symbols('*')
    symbols('/')

#PSG part

sg.change_look_and_feel('DarkAmber')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('God has left us, and programming is why - the calculator version')],
            [sg.Text()],
            [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('+')], 
            [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('-')], 
            [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('/')], 
            [sg.Button('ANS'), sg.Button('CE'), sg.Button('x'), sg.Button('*')],
            [sg.Button('GOD MAKE IT STOP PLEASE STOP IT')],]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'GOD MAKE IT STOP PLEASE STOP IT'):	# if user closes window or clicks cancel
        break
    unspaghettify_this()

window.close()


