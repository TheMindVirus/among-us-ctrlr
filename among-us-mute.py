import XInput as xinput #./python.exe -m pip install XInput-python
import pyautogui as HID #./python.exe -m pip install pyautogui

while True:
    try:
        events = xinput.get_events()
        for event in events:
            #print(event)
            if ((event.user_index == 0)
            and (event.type == xinput.EVENT_BUTTON_PRESSED)
            and (event.button == "BACK")):
                print("Mute")
                current = HID.getActiveWindow()
                HID.getWindowsWithTitle("Discord")[0].activate()
                HID.hotkey("Ctrl", "Shift", "M")
                current.activate()
    except Exception as e:
        print(e, file = sys.stderr)
