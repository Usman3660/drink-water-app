import time
from datetime import datetime
from plyer import notification

def log_reminder(message):
    """Logs the reminder to a file with a timestamp."""
    with open("water_reminder_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")

def get_user_interval():
    """Gets the reminder interval (in hours) from the user."""
    while True:
        try:
            interval = float(input("Enter the reminder interval in hours (e.g., 1 for 1 hour): "))
            if interval <= 0:
                print("Interval must be greater than 0. Please try again.")
                continue
            return interval
        except ValueError:
            print("Invalid input. Please enter a number.")

def drink_water_reminder(interval_hours=1):
    """Reminds the user to drink water at specified intervals."""
    interval_seconds = interval_hours * 3600  # Convert hours to seconds

    print(f"Water Reminder is set to notify every {interval_hours} hour(s). Press Ctrl+C to stop.")
    log_reminder("Program started.")

    try:
        while True:
            # Notification content
            title = "Time to Hydrate!"
            message = "Stay healthy and hydrated. Drink a glass of water now!"

            # Send a notification
            notification.notify(
                title=title,
                message=message,
                app_name="Water Reminder",
                timeout=10  # Notification duration in seconds
            )
            print(f"Reminder sent: {datetime.now()}")
            log_reminder("Reminder sent: Drink water.")

            # Wait for the next reminder
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print("\nWater Reminder stopped.")
        log_reminder("Program stopped by user.")

if __name__ == "__main__":
    print("Welcome to the Water Reminder Program!")
    print("This program will remind you to drink water at regular intervals.")
    print("A log of reminders will be saved in 'water_reminder_log.txt'.\n")

    # Get the reminder interval from the user
    interval = get_user_interval()

    # Start the reminder loop
    drink_water_reminder(interval_hours=interval)
