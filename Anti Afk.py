from pynput import keyboard
import time
import threading

# Program header with instruction message
header = """
\x1b[45m\x1b[37m░█████╗░███╗░░██╗████████╗██╗  ░█████╗░███████╗██╗░░██╗
██╔══██╗████╗░██║╚══██╔══╝██║  ██╔══██╗██╔════╝██║░██╔╝
███████║██╔██╗██║░░░██║░░░██║  ███████║█████╗░░█████═╝░
██╔══██║██║╚████║░░░██║░░░██║  ██╔══██║██╔══╝░░██╔═██╗░
██║░░██║██║░╚███║░░░██║░░░██║  ██║░░██║██║░░░░░██║░╚██╗
╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝  ╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝
\x1b[0m
Press F5 to start the bot
Press ESC to stop the bot
"""

# Print header
print(header)

# Variable to control the script's running state
running = False

# Function to repeatedly press keys
def press_keys():
    global running
    while running:
        # Simulate pressing the keys W, A, S, D
        keyboard_controller.press('w')
        time.sleep(0.1)
        keyboard_controller.release('w')

        keyboard_controller.press('a')
        time.sleep(0.1)
        keyboard_controller.release('a')

        keyboard_controller.press('s')
        time.sleep(0.1)
        keyboard_controller.release('s')

        keyboard_controller.press('d')
        time.sleep(0.1)
        keyboard_controller.release('d')

        time.sleep(0.1)  # Additional delay to avoid very fast pressing

# Function to handle key presses
def on_press(key):
    global running
    if key == keyboard.Key.f5:  # Start the script when F5 is pressed
        if not running:
            print("\x1b[32mBot started\x1b[0m")  # Print "Bot started" in green
            running = True
            press_thread = threading.Thread(target=press_keys)
            press_thread.start()
    elif key == keyboard.Key.esc:  # Stop the script when ESC is pressed
        if running:
            print("\x1b[31mBot stopped\x1b[0m")  # Print "Bot stopped" in red
            running = False

# Set up the keyboard controller
keyboard_controller = keyboard.Controller()

# Set up a listener to capture key presses
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
