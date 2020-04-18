import subprocess
from pathlib import Path
import plistlib
import string


def clean(s, maxlen=255):
    s = s[:maxlen]
    return ''.join(x if (x.isalnum() or x in '.-_') else '_' for x in s)


js_path = str(Path(__file__).absolute().parent / 'chrome_tabs.js')
cmd = 'osascript', '-l', 'JavaScript', js_path

p = subprocess.run(cmd, text=True, capture_output=True)

if p.returncode == 0:
    url, title, path = p.stderr.splitlines()

    path   = Path(path)
    folder = path.parent
    name   = clean(path.name)

    with open(folder / name, 'wb') as f:
        plistlib.dump({'URL': url}, f)

