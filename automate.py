import pyautogui
import keyboard


def get_position(key):
    while True:
        if keyboard.is_pressed(key):
            x, y = pyautogui.position()
            break
    return x, y


def brute_force(start, end, field_pos_x, field_pos_y, button_pos_x, button_pos_y):
    for i in range(start, end):
        pyautogui.doubleClick(x=field_pos_x, y=field_pos_y)
        pyautogui.typewrite(f"{i}", interval=0.2)
        pyautogui.click(x=button_pos_x, y=button_pos_y, interval=0.7)
        if keyboard.is_pressed("esc"):
            pyautogui.FAILSAFE = False
            keyboard.unhook_all()
            break


if __name__ == "__main__":
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    print("Move mouse on field and press the left CTRL")
    field_pos_x, field_pos_y = get_position("ctrl")
    print("Move mouse on button and press the left SHIFT")
    button_pos_x, button_pos_y = get_position("shift")
    brute_force(start, end, field_pos_x, field_pos_y, button_pos_x, button_pos_y)
