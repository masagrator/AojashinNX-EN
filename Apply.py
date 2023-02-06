import sys
import os
import json
from pathlib import Path
import glob
import pyvips

font_name = "Source Han Sans JP Regular"

Translations = glob.glob(f"Texts/*.json")

event_orig = ["\"eva41.event\"", "\"eva42.event\"", "\"eva70.event\"", "\"evb92.event\"", "\"evb93.event\"", "\"evb94.event\"", "\"evb95.event\"", "\"evb97.event\"", "\"evd32.event\""]
event_en = ["\"eva41_en.event\"", "\"eva42_en.event\"", "\"eva70_en.event\"", "\"evb92_en.event\"", "\"evb93_en.event\"", "\"evb94_en.event\"", "\"evb95_en.event\"", "\"evb97_en.event\"", "\"evd32_en.event\""]

assert(len(event_en) == len(event_orig))

os.makedirs("Applied", exist_ok=True)

for i in range(len(Translations)):
	print(Translations[i])
	file = open(Translations[i], 'r', encoding="UTF-8")
	TRANSLATION = json.load(file)
	file.close()
	file = open("scn/%s.txt.json" % Path(Translations[i]).stem, 'r', encoding="UTF-8")
	SCENARIO = json.load(file)
	file.close()

	# Scenario fixes
	match(Path(Translations[i]).stem):
		case "c02_05":
			# This entry forces wrong meswintype. If it's not detected, then files were tampered with.
			assert(SCENARIO["scenes"][1]["lines"][1090][2] == "message_cinema")
			SCENARIO["scenes"][1]["lines"].pop(1090)
			for x in range(245, 256): # Those texts entries have wrong meswintype
				SCENARIO["scenes"][1]["texts"][x][4]["meswintype"] = "message_cinema_white"

	for x in range(len(SCENARIO["scenes"])):

		base = []
		scene_keys = SCENARIO["scenes"][x].keys()
		if "texts" not in scene_keys:
			if "selects" in scene_keys:
				for y in range(len(SCENARIO["scenes"][x]["selects"])):
					SCENARIO["scenes"][x]["selects"][y]["text"] = TRANSLATION["scenes"][x]["selects"][y]
			continue
		assert(len(SCENARIO["scenes"][x]["texts"]) == len(TRANSLATION["scenes"][x]["texts"]))
		for y in range(len(SCENARIO["scenes"][x]["texts"])):
			texts_keys = TRANSLATION["scenes"][x]["texts"][y].keys()
			if "name" in texts_keys:
				SCENARIO["scenes"][x]["texts"][y][0] = TRANSLATION["scenes"][x]["texts"][y]["name"]
				if (SCENARIO["scenes"][x]["texts"][y][1][0][0] != None):
					# Those names are used to override font rendering with prerendered texture asset
					# In case of not detecting name it falls back to font rendering
					# I am nulling it because I am not bothered by names not fitting in text window
					SCENARIO["scenes"][x]["texts"][y][1][0][0] = None
			try:
				img = pyvips.Image.text(TRANSLATION["scenes"][x]["texts"][y]["text"].replace("\\&", "&amp;"), dpi=159, font=font_name)
			except Exception as exc:
				print("Something went wrong!")
				print("Text to print:")
				print(TRANSLATION["scenes"][x][y]["string_ENG"])
				print(f"SCENE: {x}, ENTRY: {y}")
				print(exc)
				print("Aborting...")
				sys.exit()
			
			strlist = []
			try:
				if (SCENARIO["scenes"][x]["texts"][y][4]["meswintype"] in ["message_cinema", "message_cinema_white"]):
					lines_max = 3
					width_max = 951 # This is biggest value found that won't break backlog. Actual width max of message_cinema is 1000 which we will use only when necessary
				else:
					lines_max = 4
					width_max = 940
			except:
				lines_max = 4
				width_max = 940
			if img.width > width_max:
				string = TRANSLATION["scenes"][x]["texts"][y]["text"].split(" ")
				start = 0
				count = 1
				while(True):
					if pyvips.Image.text(" ".join(string[start:count]).replace("&", "&amp;"), dpi=159, font=font_name).width < width_max:
						if (count == len(string)):
							strlist.append(" ".join(string[start:count]))
							if (len(strlist) > lines_max):
								print(f"More than {lines_max} lines detected!")
								print(strlist)
								# This will break rendering text in backlog, but still allow to fit text in message_cinema in 3 lines
								if (lines_max == 3 and width_max < 1000):
									print("Detected message_cinema text. Falling back to width max 1000!")
									strlist = []
									width_max = 1000
									start = 0
									count = 1
									continue
								else:
									sys.exit()
							strlist = "\\n".join(strlist)
							break
						count += 1
						continue
					strlist.append(" ".join(string[start:count-1]))
					start = count-1
			else:
				strlist = TRANSLATION["scenes"][x]["texts"][y]["text"]
			WORKLIST = SCENARIO["scenes"][x]["texts"][y][1][0]
			WORKLIST[1] = strlist
			WORKLIST[2] = len(strlist.replace("\\n", ""))
			if (strlist.find("\\n") != -1):
				if (len(SCENARIO["scenes"][x]["texts"][y][1][0]) == 3):
					SCENARIO["scenes"][x]["texts"][y][1][0].append(strlist.replace("\\n", " "))
					SCENARIO["scenes"][x]["texts"][y][1][0].append(strlist.replace("\\n", " "))
				else:
					SCENARIO["scenes"][x]["texts"][y][1][0][3] = strlist.replace("\\n", " ")
					SCENARIO["scenes"][x]["texts"][y][1][0][4] = strlist.replace("\\n", " ")
			elif (len(SCENARIO["scenes"][x]["texts"][y][1][0]) > 3):
				SCENARIO["scenes"][x]["texts"][y][1][0].pop(4)
				SCENARIO["scenes"][x]["texts"][y][1][0].pop(3)
			SCENARIO["scenes"][x]["texts"][y][1][0] = WORKLIST

	TEXT_DUMP = json.dumps(SCENARIO, indent="\t", ensure_ascii=False)

	# Replace textures using Japanese texts with ones having English texts
	# They are included with game's assets
	for z in range(len(event_orig)):
		if (TEXT_DUMP.find(event_orig[z]) != -1):
			print(f"Found: {event_orig[z]}, replacing with {event_en[z]}")
			TEXT_DUMP = TEXT_DUMP.replace(event_orig[z], event_en[z])

	json_file = open("Applied/%s.json" % Path(Translations[i]).stem, "w", encoding="UTF-8")
	json_file.write(TEXT_DUMP)
	json_file.close()