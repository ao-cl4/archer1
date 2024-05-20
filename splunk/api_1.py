import splunklib.client as client

# Define your connection parameters
HOST = 'https://192.168.1.66:8089'
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
