import subprocess
import os
import glob
from pathlib import Path
import shutil

files = glob.glob("Applied/*.json")
resx = glob.glob("scn/*.resx.json")
filtered = []

for i in range(len(resx)):
    shutil.copy(resx[i], "Applied/%s.json" % Path(resx[i]).stem)

for i in range(len(files)):
	if files[i].find("resx") == -1:
		filtered.append(files[i])

os.makedirs("Compiled", exist_ok=True)

for i in range(len(filtered)):
	print(Path(filtered[i]).stem)
	subprocess.run(["psbuild.exe", "-p", "krkr", r"%s" % os.path.abspath(filtered[i])], capture_output=True)
	shutil.move("%s.psb" % Path(filtered[i]).stem, "Compiled/%s.txt.scn" % Path(filtered[i]).stem)