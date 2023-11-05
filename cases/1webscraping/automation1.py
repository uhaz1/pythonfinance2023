

#! python3
# searchpypi.py - Open several search results
# https://automatetheboringstuff.com/2e/chapter12/


# https://beautiful-soup-4.readthedocs.io/en/latest/#
# https://requests.readthedocs.io/en/latest/
# https://docs.python.org/3/library/webbrowser.html

import requests, sys, webbrowser, bs4

# check terms and condition of use of the website
# https://pypi.org/policy/acceptable-use-policy/
# https://pypi.org/policy/terms-of-use/

print('Searching...')    # display text while downloading the search result page
res = requests.get('https://pypi.org/search/?q='
+ ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each results
linkElems = soup.select('.package-snippet')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
