import time
from plyer import notification

def drink_water_reminder(interval_hours=1):
    """Reminds the user to drink water at specified intervals."""
    interval_seconds = interval_hours * 3600  # Convert hours to seconds
    while True:
        # Send a notification
        notification.notify(
            title="Drink Water Reminder",
            message="Stay hydrated! Drink a glass of water now.",
            app_name="Water Reminder",
            timeout=10  # Notification duration in seconds
        )
        # Wait for the next reminder
        time.sleep(interval_seconds)

if __name__ == "__main__":
    try:
        print("Water Reminder is running. Press Ctrl+C to stop.")
        drink_water_reminder(interval_hours=1)  # Set interval to 1 hour
    except KeyboardInterrupt:
        print("\nWater Reminder stopped.")
