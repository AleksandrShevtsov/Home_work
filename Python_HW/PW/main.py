# For an internal project we are looking to scrape a website.
#
# https://us.sunpower.com/dealers-installers
#
#
# Objective 1:
# Go to url, fill in a postcode from provided list, find results. (for example use 90001)
#
# Objective 2
# For each dealer listed (Master DealersElite DealersAuthorized Dealers), click to view dealer details.
#
# Objective 3
# Save from new opened detailed page their email adress.
#
#
# Objective 4, repeat, repeat, repeat. This program must run by itself and work through the postcode list.
#
# Save all emails in a csv file
#
#
# If you can build this, please apply.

import requests
from bs4 import BeautifulSoup
import re
import csv

# Go to url, fill in a postcode from provided list, find results. (for example use 90001)
url = 'https://us.sunpower.com/dealers-installers'
response = requests.get(url)
