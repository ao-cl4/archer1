import csv
from faker import Faker
from random import randint, choice
from datetime import datetime, timedelta

fake = Faker()

# Generate a list of users
users = [fake.user_name() for _ in range(10)]

# Helper function to generate timestamps
def random_date(start, end):
    return start + timedelta(seconds=randint(0, int((end - start).total_seconds())))

# Define the time range for the data
start_date = datetime.now() - timedelta(days=30)
end_date = datetime.now()

# Generate a list of typical binary process names
binary_processes = [
    "explorer.exe", "cmd.exe", "powershell.exe", "taskmgr.exe", 
    "notepad.exe", "calc.exe", "mspaint.exe", "svchost.exe",
    "chrome.exe", "firefox.exe"
]

# Generate Splunk query results for Windows binary processes
with open('splunk_query_results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['timestamp', 'username', 'binary_process'])

    for _ in range(100):  # Generate 100 process executions
        timestamp = random_date(start_date, end_date).isoformat()
        username = choice(users)
        binary_process = choice(binary_processes)
        writer.writerow([timestamp, username, binary_process])

# Generate user login data
with open('user_logins.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['timestamp', 'username'])

    for _ in range(50):  # Generate 50 login entries
        timestamp = random_date(start_date, end_date).isoformat()
        username = choice(users)
        writer.writerow([timestamp, username])

print("Data generation complete.")
