# Main file into Python project

import requests as rq
import pandas as pd

apiKey = "33a792c68888383c3eaa4b96a3c6678a798a9dd3"
numVersion = "3"

response = requests.get("https://api.jcdecaux.com/vls/v{0}/stations?apiKey={1}").format(numVersion,apiKey)

print(response.status_code)