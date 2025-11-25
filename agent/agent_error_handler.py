import traceback

class ErrorHandlingAgent:
    def __init__(self, notification_agent, log_path="error_log.txt"):
        self.notifier = notification_agent
        self.log_path = log_path

    def handle(self, error):
        error_msg = f"\n=== ERROR OCCURRED ===\n{str(error)}\n{traceback.format_exc()}\n"

        # Log to file
        with open(self.log_path, "a") as f:
            f.write(error_msg)

        # Notify
        self.notifier.notify_console(error_msg)
        self.notifier.notify_slack(f"Error occurred:\n{str(error)}")
