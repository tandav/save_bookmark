import subprocess
import tkinter.filedialog
from pathlib import Path
import plistlib


# print(__package__, __path__, __file__)

js_path = str(Path(__file__).absolute().parent / 'chrome_tabs.js')
cmd = 'osascript', '-l', 'JavaScript', js_path
url, title = subprocess.run(cmd, check=True, text=True, capture_output=True).stderr.splitlines()
print(url)
print(title)


DEFAULT_SAVE_DIR = Path.home() / 'Documents/GoogleDrive/entrypoint/knowledge'

# Make a top-level instance and hide since it is ugly and big.
root = tkinter.Tk()
root.withdraw()

subprocess.run(['open', '-a', 'Python']) # i've tried many options to focus on savefile dialog in macOS, but only this works
#
# try:
#
# except AttributeError

f = tkinter.filedialog.asksaveasfile(
    mode             = 'wb',
    # parent         = root,
    title            = 'Where to Save',
    initialdir       = DEFAULT_SAVE_DIR,
    initialfile      = title           ,
    defaultextension = 'webloc'        ,
)

if f:
    plistlib.dump({'URL': url}, f)
