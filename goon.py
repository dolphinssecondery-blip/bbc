python
import pyautogui
import time

# --- CONFIGURATION ---
MESSAGE = "Hello! This is an automated message. :)"
REPETITIONS = 10000
DELAY_BEFORE_START = 5  # Gives you time to click into the chat window
# ---------------------

def start_spam():
    print(f"Starting in {DELAY_BEFORE_START} seconds...")
    print("QUICK! Open your chat window now!")
    time.sleep(DELAY_BEFORE_START)

    try:
        for i in range(REPETITIONS):
            # Type the message and press enter
            pyautogui.typewrite(MESSAGE)
            pyautogui.press('enter')
            
            # Optional: add a tiny sleep to prevent the app from crashing
            # time.sleep(0.01) 
            
    except KeyboardInterrupt:
        print("\nStopped by user.")

if __name__ == "__main__":
    start_spam()
