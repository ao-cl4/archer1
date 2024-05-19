from faker import Faker
import csv

# Initialize Faker
fake = Faker()

# Function to generate fake data for each row
def generate_fake_row():
    return [
        fake.ipv4(),                           # Host IP
        fake.hostname(),                       # Hostname
        fake.domain_name(),                    # Active Directory Domain Name
        fake.word(),                           # Process Name
        fake.sentence(nb_words=6),             # Process Command Line
        fake.word()                            # Process Parent Name
    ]

# Number of rows to generate
num_rows = 10

# CSV file path
csv_file_path = 'fake_data.csv'

# Generate and write fake data to CSV
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Host IP', 'Hostname', 'Active Directory Domain Name', 'Process Name', 'Process Command Line', 'Process Parent Name'])
    for _ in range(num_rows):
        writer.writerow(generate_fake_row())

print(f"Fake data has been generated and saved to '{csv_file_path}'.")
