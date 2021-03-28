import xinput #import XInput as xinput #python.exe -m pip install xinput
import pyautogui as HID #python.exe -m pip install pyautogui
import sys, time

TRIGGER_THRESHOLD = 0.8
left_trigger = 0
right_trigger = 0

STICK_THRESHOLD = 0.5
CURSOR_FREQ = 0.010
CURSOR_PIXELS = 20
cursor_deltax = 0
cursor_deltay = 0

move_up = [0, 0]
move_down = [0, 0]
move_left = [0, 0]
move_right = [0, 0]

HID.FAILSAFE = True # Set this to false if the mouse gets stuck

while True:
    try:
        events = xinput.get_events()
        for event in events:
            #print(event)
            if (event.user_index == 0):
                if (event.type == xinput.EVENT_BUTTON_PRESSED):
                    if (event.button == "A"):
                        HID.click()
                    if (event.button == "B"):
                        HID.press("esc")
                    if (event.button == "START"):
                        HID.press("enter")
                    if (event.button == "BACK"):
                        print("Mute")
                        current = HID.getActiveWindow()
                        HID.getWindowsWithTitle("Discord")[0].activate()
                        HID.hotkey("Ctrl", "Shift", "M")
                        current.activate()
                    if (event.button == "DPAD_UP"):
                        HID.press("up")
                    if (event.button == "DPAD_DOWN"):
                        HID.press("down")
                    if (event.button == "DPAD_LEFT"):
                        HID.press("left")
                    if (event.button == "DPAD_RIGHT"):
                        HID.press("right")
                if (event.type == xinput.EVENT_TRIGGER_MOVED):
                    if (event.trigger == xinput.LEFT):
                        if ((event.value > TRIGGER_THRESHOLD)
                        and (left_trigger != 1)):
                            left_trigger = 1
                        elif ((event.value <= TRIGGER_THRESHOLD)
                        and (left_trigger == 1)):
                            left_trigger = 0
                    if (event.trigger == xinput.RIGHT):
                        if ((event.value > TRIGGER_THRESHOLD)
                        and (right_trigger != 1)):
                            HID.mouseDown()
                            right_trigger = 1
                        elif ((event.value <= TRIGGER_THRESHOLD)
                        and (right_trigger == 1)):
                            HID.mouseUp()
                            right_trigger = 0
                if (event.type == xinput.EVENT_STICK_MOVED):
                    if (event.stick == xinput.LEFT):
                        if (event.x < -1 * STICK_THRESHOLD):
                            move_left[0] = 1
                        elif (event.x > STICK_THRESHOLD):
                            move_right[0] = 1
                        else:
                            move_left[0] = 0
                            move_right[0] = 0
                        if (event.y < -1 * STICK_THRESHOLD):
                            move_down[0] = 1
                        elif (event.y > STICK_THRESHOLD):
                            move_up[0] = 1
                        else:
                            move_down[0] = 0
                            move_up[0] = 0
                    if (event.stick == xinput.RIGHT):
                        if (left_trigger == 1):
                            if (event.value > STICK_THRESHOLD):
                                cursor_deltax = event.x * CURSOR_PIXELS
                                cursor_deltay = event.y * CURSOR_PIXELS * -1
                            else:
                                cursor_deltax = 0
                                cursor_deltay = 0
        if (left_trigger):
            HID.move(int(cursor_deltax), int(cursor_deltay), _pause = False)
        if (move_up[0]):
            HID.keyDown("w", _pause = False)
            move_up[1] = 1
        elif (move_up[1]):
            HID.keyUp("w", _pause = False)
            move_up[1] = 0
        if (move_down[0]):
            HID.keyDown("s", _pause = False)
            move_down[1] = 1
        elif (move_down[1]):
            HID.keyUp("s", _pause = False)
            move_down[1] = 0
        if (move_left[0]):
            HID.keyDown("a", _pause = False)
            move_left[1] = 1
        elif (move_left[1]):
            HID.keyUp("a", _pause = False)
            move_left[1] = 0
        if (move_right[0]):
            HID.keyDown("d", _pause = False)
            move_right[1] = 1
        elif (move_right[1]):
            HID.keyUp("d", _pause = False)
            move_right[1] = 0
        time.sleep(CURSOR_FREQ)
    except Exception as e:
        print(e, file = sys.stderr)
