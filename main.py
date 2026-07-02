import re 
import sys
from plyer import notification
import time

YES_PATTERN = re.compile(r"^(y+|yes+|yeah+|yep+|yup+|yea+|ya+|yee+)$", re.IGNORECASE)
NO_PATTERN = re.compile(r"^(n+|no+|nah+|nope+|na+)$")
NUM_SECONDS_IN_MINUTE = 60
NUM_WORKING_SESSIONS = 2

def main(): 
    while(True): 
        print("Welcome to Pomodoro Timer. Do you want to start a work session? (yes/no)")
        response = input()

        if is_pattern(response, YES_PATTERN): 
            break
        elif is_pattern(response, NO_PATTERN): 
            print("exiting...")
            sys.exit()

    for _ in range(NUM_WORKING_SESSIONS):  
        print("starting timer for working session")
        countdown_timer(25 * NUM_SECONDS_IN_MINUTE)
        print("starting timer for short break...")
        countdown_timer(5 * NUM_SECONDS_IN_MINUTE)

    notification.notify(
        title="Done",
        message="You have finished a working session!",
        app_name="Pomodoro Timer",
        timeout=5
    )

def is_pattern(response, pattern): 
    return bool(pattern.fullmatch(response.strip()))

def countdown_timer(seconds): 
    while seconds > 0: 
        mins, secs = divmod(seconds, NUM_SECONDS_IN_MINUTE)

        print(f"{mins:02d}:{secs:02d}", end="\r")

        time.sleep(1)
        seconds -= 1

if __name__== "__main__":
    main()