import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60) 
        print(f"{mins:02d}:{secs:02d}", end="\r") 
        time.sleep(1)
        seconds -= 1
    
    print("Time's Up! ⏰")


user_seconds = int(input("Enter countdown time in seconds: "))  
countdown_timer(user_seconds)
