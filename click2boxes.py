# Made this to be able to use the lockpicking boxes in Redridge
# without actually needing to click on them over and over. At
# some point I found the sound soothing, so I decided to add in
# the recording commands into it.
import pyautogui, time

time.sleep(2)  # This gives time to cancel if needed.

# I set this to a random location as I knew it would be where it
# needed to be on my screen. Could probably work this better
# in the future by looking for the WoW window.
pyautogui.click(800, 800, button='left')  #getting in window
print('Position the cursor over the first box.')
time.sleep(3)  #time to line up box one
box1 = pyautogui.position()  # getting the position of the first box
print('Position of first box recorded at', box1.x, 'x', box1.y)
print('\a')

print('Position the cursor over the second box.')
time.sleep(3)  # time to line up the next box
box2 = pyautogui.position()  # getting the position of the second box
print('Position of second box recorded at', box2.x, 'x', box2.y)
print('\a')

time.sleep(.5)  # just seemed better this way
pyautogui.hotkey('alt', 'f9')  # in theory starts the recording
time.sleep(.5)  # needed a little delay at the beginning.
print('Starting the clicking.')
clickCount = int(0)
for i in range(360):
    pyautogui.click(box1.x, box1.y, button='right')
    pyautogui.moveTo(1920, 540)
    time.sleep(5.5)  # the actual timing is 5, but it sounded bad
    clickCount = clickCount + 1
    pyautogui.click(box2.x, box2.y, button='right')
    pyautogui.moveTo(1920, 540)
    time.sleep(5.5)  # same as above
    clickCount = clickCount + 1

pyautogui.hotkey('alt', 'f9')
print('I have just clicked', clickCount, 'times.')
print('Clicking complete.')
