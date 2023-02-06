import subprocess
import os
import glob
from pathlib import Path
import shutil

files = glob.glob("Applied/*.json")
filtered = []

for i in range(len(files)):
	if files[i].find("resx") == -1:
		filtered.append(files[i])

os.makedirs("Compiled", exist_ok=True)

for i in range(len(filtered)):
	print(Path(filtered[i]).stem)
	subprocess.run(["psbuild.exe", "-p", "krkr", r"%s" % os.path.abspath(filtered[i])], capture_output=True)
	file = open("%s.psb" % Path(filtered[i]).stem, "rb")
	new_file = open("Compiled/%s.txt.scn" % Path(filtered[i]).stem, "wb")
	new_file.write(file.read())
	new_file.close()
	file.close()
	os.remove("%s.psb" % Path(filtered[i]).stem)