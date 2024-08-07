import splunklib.client as client
import splunklib.results as results
import time
import csv

# Define your connection parameters
HOST = '192.168.1.66'
PORT = 8089  # Default management port
TOKEN = 'eyJraWQiOiJzcGx1bmsuc2VjcmV0IiwiYWxnIjoiSFM1MTIiLCJ2ZXIiOiJ2MiIsInR0eXAiOiJzdGF0aWMifQ.eyJpc3MiOiJhZG1pbiBmcm9tIHNwbHVuay1zZXJ2ZXIiLCJzdWIiOiJhZG1pbiIsImF1ZCI6ImFwaTEiLCJpZHAiOiJTcGx1bmsiLCJqdGkiOiI5OTk0NWMzZDQ1Y2FmMDA4ZDg4YTViOTY2YzE2MjJmNGY3MmYyNzViMDM4YmQyNThhZTM0YTE3ZmMwMTdmOTFlIiwiaWF0IjoxNzE2MjA1NjI2LCJleHAiOjE3MTg3OTc2MjYsIm5iciI6MTcxNjIwNTYyNn0.r92XVY13gGdmRm3Oyl5vcBXWpoqlQOhfvx7I2L_ioXeil0R6NSCyeG8NTDGtz-Zf9lveR1rfx6pX58-hXOGzKA'

# Create a Service instance and log in using the token
service = client.connect(
    host=HOST,
    port=PORT,
    token=TOKEN
)

# Verify the connection
for app in service.apps:
    print(app.name)

# Get the search query from the user
search_query = input("Please enter your search query: ")

# Create a job for the search
job = service.jobs.create(search_query, output_mode='json')

# Wait for the job to complete
while not job.is_done():
    print("Waiting for job to complete...")
    time.sleep(2)

# Get the results
result_stream = job.results(output_mode='json')

# Parse the results using JSONResultsReader
reader = results.JSONResultsReader(result_stream)

# Initialize an empty list to store results
result_list = []

for result in reader:
    if isinstance(result, results.Message):
        # Handle messages
        print(f"Message: {result}")
    elif isinstance(result, dict):
        # Handle actual results
        result_list.append(result)

# Define the output file path
output_file_path = "search_results.csv"

# Save the results to a CSV file
with open(output_file_path, 'w', newline='') as output_file:
    # Create a CSV writer object
    csv_writer = csv.writer(output_file)
    
    # Write the header row (column names)
    if result_list:
        header = result_list[0].keys()
        csv_writer.writerow(header)
        
        # Write the data rows
        for result in result_list:
            csv_writer.writerow(result.values())

print(f"Results saved to {output_file_path}")
