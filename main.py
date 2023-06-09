
print ("i love isla")
#hi this is a note
print ("hi!")

import requests

def trace(*args):
  """Used for debug output"""
  print (*args)  # Comment out this line to remove debug output
  pass

# This base URL works, but doesn't return anything too interesting
# After running this script, read https://www.boredapi.com/ and
# figure out how to change it to get back a filtered activity.
# The filter is up to you: number of people, category, price, etc.
# Tip: try testing the API URLs directly in a browser first
URL = "https://www.boredapi.com/api/activity?participants=1"


# Get data from the web site and put it into Python collections
# trace ("Calling", URL)
# response = requests.get(URL) # Get data from the URL
# response.raise_for_status()  # Throw an exception if the request failed
data = response.json()       # Parse the response into JSON

# See what the raw data looks like
# trace ("\nText returned:", response.text)

# You can also loop through each item (name/value pairs) in the JSON
# trace ("\nHere are all the kay/value pairs in the JSON response:")
for key, value in data.items():
  trace (key, ": ", value)

# After running this script and using the right URL to get the data
# you need, comment out the print statement in the trace function to
# remove the debug output, and add your own print statement at the end.
# Something that shows both the filter you used and the activity
print (f"Here's a one person activity for you: {data['activity']}")