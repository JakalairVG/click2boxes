# Made this to be able to use the lockpicking boxes in Redridge
# without actually needing to click on them over and over. At
# some point I found the sound soothing, so I decided to add in
# the recording commands into it.
import pyautogui, time
import pyinputplus as pyip
# Some information on screen.
print('This program will right click on two different loactions.')
print('It was intended to help in training lockpicking in WoW.')
print('Please, move/resize this window to be able to see 2 boxes.')
time.sleep(2)  # This gives time to cancel if needed.
print('How many times to you want to click both boxes?')
print('(Each round takes approximately 11 seconds.)')
clickResponse = pyip.inputInt(prompt='Enter a number:')

print('\nDo you want to record the session? (Y/n)')
recResponse = pyip.inputYesNo(default='Yes', blank=True)
if recResponse == 'yes':
    print('We will try and record.')
if recResponse == 'no':
    print('We will not record.')

# I set this to a random location as I decided to chosing would be better.
# print('Please place the mouse over the WoW window and press enter.')
# wowResponse = pyip.inputStr()
# wowLocation = pyautogui.position() #getting WoW window location.
# pyautogui.click(wowLocation.x, wowLocation.y, button='left')  #getting in window
print('Position the cursor over the first box, then press enter.')
wowResponse = pyip.inputStr(blank=True)
# time.sleep(1)  # just a pause now
box1 = pyautogui.position()  # getting the position of the first box
print('Position of first box recorded at', box1.x, 'x', box1.y)
print('\a')

print('Position the cursor over the second box, then press enter.')
wowResponse = pyip.inputStr(blank=True)
# time.sleep(1)  # time to line up the next box
box2 = pyautogui.position()  # getting the position of the second box
print('Position of second box recorded at', box2.x, 'x', box2.y)
print('\a')
print('Press enter to begin.')
wowResponse = pyip.inputStr(blank=True)
pyautogui.click(box1.x, box1.y, button='right')
time.sleep(.5)  # just seemed better this way

if recResponse == 'yes':
    pyautogui.hotkey('alt', 'f9')  # in theory starts the recording

time.sleep(.5)  # needed a little delay at the beginning.
print('Starting the clicking.')
clickCount = int(0)
for i in range(clickResponse):
    pyautogui.click(box1.x, box1.y, button='right')
    time.sleep(0.5)
    pyautogui.moveTo(box2.x, box2.y, duration=5)
    # time.sleep(5.5)  # the actual timing is 5, but it sounded bad
    clickCount = clickCount + 1
    pyautogui.click(box2.x, box2.y, button='right')
    time.sleep(0.5)
    pyautogui.moveTo(box1.x, box1.y, duration=5)
    # time.sleep(5.5)  # same as above
    clickCount = clickCount + 1

if recResponse == 'yes':
    pyautogui.hotkey('alt', 'f9')
print('I have just clicked', clickCount, 'times.')
print('Clicking complete.')
