import subprocess
import tkinter.filedialog
from pathlib import Path
import plistlib

cmd = 'osascript', '-l', 'JavaScript', 'chrome_tabs.js'
url, title = subprocess.run(cmd, check=True, text=True, capture_output=True).stderr.splitlines()
print(url)
print(title)

with tkinter.filedialog.asksaveasfile(
    mode             = 'wb'                   ,
    title            = 'Where to Save'        ,
    initialdir       = Path.home() / 'Desktop',
    initialfile      = title                  ,
    defaultextension = 'webloc'               ,
) as f:
    plistlib.dump({'URL': url}, f)
