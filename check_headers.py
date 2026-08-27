import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.behance.net/gallery/249103323/JS-Insurance-Services'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    response = urllib.request.urlopen(req, context=ctx)
    print("Headers for " + url + ":")
    print(response.headers)
except Exception as e:
    print(f'Error fetching {url}: {e}')
