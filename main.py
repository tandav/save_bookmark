import subprocess
from pathlib import Path
import plistlib

def clean_title(title):
    return ''.join(x if x.isalnum() else '_' for x in title)


js_path = str(Path(__file__).absolute().parent / 'chrome_tabs.js')
cmd = 'osascript', '-l', 'JavaScript', js_path

p = subprocess.run(cmd, text=True, capture_output=True)

if p.returncode == 0:
    url, title, folder = p.stderr.splitlines()

    title = clean_title(title)

    with (Path(folder) / title).with_suffix('.webloc').open('wb') as f:
        plistlib.dump({'URL': url}, f)

