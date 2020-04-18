import subprocess
import tkinter.filedialog
from pathlib import Path
import plistlib



js_path = str(Path(__file__).absolute().parent / 'chrome_tabs.js')
cmd = 'osascript', '-l', 'JavaScript', js_path

p = subprocess.run(cmd, text=True, capture_output=True)

if p.returncode == 0:
    url, title, folder = p.stderr.splitlines()
    print(url)
    print(title)
    print(folder)

    with (Path(folder) / title).with_suffix('.webloc').open('wb') as f:
        plistlib.dump({'URL': url}, f)

# DEFAULT_SAVE_DIR = Path.home() / 'Documents/GoogleDrive/entrypoint/knowledge'
#
# # Make a top-level instance and hide since it is ugly and big.
# root = tkinter.Tk()
# root.withdraw()
#
# subprocess.run(['open', '-a', 'Python']) # i've tried many options to focus on savefile dialog in macOS, but only this works
# #
# # try:
# #
# # except AttributeError
#
# f = tkinter.filedialog.asksaveasfile(
#     mode             = 'wb',
#     # parent         = root,
#     title            = 'Where to Save',
#     initialdir       = DEFAULT_SAVE_DIR,
#     initialfile      = title           ,
#     defaultextension = 'webloc'        ,
# )
#
# if f:
