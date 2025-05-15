import threading
import time
from datetime import datetime

def log(msg):
    """Helper function to log with timestamp and thread name."""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] [{threading.current_thread().name}] {msg}")
def walk_dog(first, last):
    time.sleep(8)
    log(f"You finish walking {first} {last}")
def take_out_trash():
    time.sleep(2)
    log("You take out the trash")
def get_mail():
    time.sleep(4)
    log("You get the mail")
def main():
    log("Starting chores...")
    # Creating threads
    chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"), name="WalkDogThread")
    chore2 = threading.Thread(target=take_out_trash, name="TrashThread")
    chore3 = threading.Thread(target=get_mail, name="MailThread")
    # Starting threads
    chore1.start()
    chore2.start()
    chore3.start()
    # Waiting for all threads to finish
    chore1.join()
    chore2.join()
    chore3.join()
    log("All chores are complete!")

if __name__ == "__main__":
    main()
