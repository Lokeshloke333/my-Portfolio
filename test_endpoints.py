import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = [
    'https://www.behance.net/gallery/249103323/JS-Insurance-Services?iframe=1',
    'https://www.behance.net/gallery/249103323/JS-Insurance-Services?embed=1',
    'https://www.behance.net/embed/project/249103323',
    'https://www.behance.net/embed/project/249103323?ilo0=1'
]

for url in urls:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        response = urllib.request.urlopen(req, context=ctx)
        html = response.read().decode('utf-8')
        print(f"\n--- {url} ---")
        print("X-Frame-Options:", response.headers.get('X-Frame-Options', 'None'))
        if 'View Project' in html or 'project-modules' in html:
            if 'project-modules' in html:
                print("Appears to contain full project modules.")
            else:
                print("Appears to be a limited widget.")
        print("Length:", len(html))
    except Exception as e:
        print(f'Error fetching {url}: {e}')
