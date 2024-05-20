import time
import splunklib.client as client
import splunklib.results as results
import logging

# Define your connection parameters
HOST = '192.168.1.66'
PORT = 8089  
TOKEN = 'eyJraWQiOiJzcGx1bmsuc2VjcmV0IiwiYWxnIjoiSFM1MTIiLCJ2ZXIiOiJ2MiIsInR0eXAiOiJzdGF0aWMifQ.eyJpc3MiOiJhZG1pbiBmcm9tIHNwbHVuay1zZXJ2ZXIiLCJzdWIiOiJhZG1pbiIsImF1ZCI6ImFwaTEiLCJpZHAiOiJTcGx1bmsiLCJqdGkiOiI5OTk0NWMzZDQ1Y2FmMDA4ZDg4YTViOTY2YzE2MjJmNGY3MmYyNzViMDM4YmQyNThhZTM0YTE3ZmMwMTdmOTFlIiwiaWF0IjoxNzE2MjA1NjI2LCJleHAiOjE3MTg3OTc2MjYsIm5iciI6MTcxNjIwNTYyNn0.r92XVY13gGdmRm3Oyl5vcBXWpoqlQOhfvx7I2L_ioXeil0R6NSCyeG8NTDGtz-Zf9lveR1rfx6pX58-hXOGzKA'

# Function to connect to Splunk service
def connect_to_splunk(host, port, token):
    try:
        service = client.connect(
            host=host,
            port=port,
            token=token
        )
        logging.debug("Successfully connected to Splunk")
        return service
    except Exception as e:
        logging.error(f"Failed to connect to Splunk: {e}")
        return None

# Main function
def main():
    # Connect to Splunk service
    service = connect_to_splunk(HOST, PORT, TOKEN)
    if not service:
        return

    # Get the search query from the user
    search_query = input("Enter your search query: ")

    try:
        # Create a job for the search
        job = service.jobs.create(search_query)

        # Wait for the job to complete
        while not job.is_done():
            print("Waiting for job to complete...")
            time.sleep(2)

        # Get the results
        result_stream = job.results()

        # Parse the results
        reader = results.ResultsReader(result_stream)

        for result in reader:
            if isinstance(result, results.Message):
                # Handle messages
                print(f"Message: {result}")
            elif isinstance(result, dict):
                # Handle actual results
                print(result)
    except Exception as e:
        logging.error(f"Error during search: {e}")

if __name__ == "__main__":
    main()
