import urllib.request
from html.parser import HTMLParser
import ssl
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = {
    'js-insurance.jpg': 'https://www.behance.net/gallery/249103323/JS-Insurance-Services',
    'ecommerce.jpg': 'https://www.behance.net/gallery/247460375/Ecommerce',
    'nri-payments.jpg': 'https://www.behance.net/gallery/247566309/NRI-Payments',
    'shrimp.jpg': 'https://www.behance.net/gallery/247459937/Shrimp',
    'construction-material.jpg': 'https://www.behance.net/gallery/248371935/Construction-material'
}

class OGImageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.og_image = None
    def handle_starttag(self, tag, attrs):
        if tag == 'meta':
            attrs_dict = dict(attrs)
            if attrs_dict.get('property') == 'og:image':
                self.og_image = attrs_dict.get('content')

def get_og_image(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
        parser = OGImageParser()
        parser.feed(html)
        return parser.og_image
    except Exception as e:
        print(f'Error fetching {url}: {e}')
        return None

out_dir = 'e:/Lokesh/Development/my-Portfolio/assets/images/projects'
os.makedirs(out_dir, exist_ok=True)

for filename, url in urls.items():
    print(f'Processing {filename}...')
    img_url = get_og_image(url)
    if img_url:
        print(f'Found image URL: {img_url}')
        try:
            req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            img_data = urllib.request.urlopen(req, context=ctx).read()
            filepath = os.path.join(out_dir, filename)
            with open(filepath, 'wb') as f:
                f.write(img_data)
            print(f'Saved {filepath}')
        except Exception as e:
            print(f'Failed to download {img_url}: {e}')
    else:
        print(f'No og:image found for {url}')
