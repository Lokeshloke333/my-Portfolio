import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.behance.net/gallery/249103323/JS-Insurance-Services/iframe'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    response = urllib.request.urlopen(req, context=ctx)
    print("Status:", response.status)
except Exception as e:
    print(f'Error fetching {url}: {e}')

url2 = 'https://www.behance.net/embed/project/249103323?ilo0=1'
req2 = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
try:
    response2 = urllib.request.urlopen(req2, context=ctx)
    print("Headers for embed URL:", response2.headers)
except Exception as e:
    print(f'Error fetching {url2}: {e}')
