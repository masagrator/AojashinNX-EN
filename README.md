# AojashinNX-EN
English Translation Mod for Nintendo Switch version of game<br>`Hakuchuumu no Aojashin: The girl who's called the world` (Japanese title)<br>`Cyanotype Daydream -The Girl Who Dreamed the World-` (English title)

# Compiling scenario files
Requirements:
- Windows 7+
- Python 3.10+
- Python library `pyvips` (to work it requires adding [vips](https://github.com/libvips/libvips/releases) bin folder to PATH)
- FreeMoteToolkit (you can download it from [here](https://github.com/UlyssesWu/FreeMote/releases/tag/v3.4.0))

1. From FreeMoteToolkit copy: `PsbDecompile.exe`, `PsbDecompile.exe.config`, `PsBuild.exe`, `PsBuild.exe.config` and folder `lib` to root folder of repository
2. From romfs of game copy folders `scn` and `font` to root folder of repository
3. Use "decompile.cmd"
4. Run "Apply.py"
5. Run "Compile.py"
6. New scn files can be found in `Compiled` folder

# Notes
- English textures are included with game originally, so mod reuses as much English textures as possible in story, but in CG Mode they are not changed. Some of those textures include typos that you can find in `Notes.txt`
- Apply.py injects break lines based on font file from `font` folder, thus why it takes much more time to finish. If you plan to replace font in game, you need to compile scripts with new font to fix break lines. Apply.py includes limitations aborting process if rendered text will take too much lines, which would result in text being unreadable.
- Some name labels were changed to make them shorter
- One CG was removed from Switch version, it was bringed back in this mod, though you cannot see it in CG mode. 
- There were some small changes to scenario. The biggest one is in Prologue. Any new line was machine translated. Changes that were not typo fixes can be found [here](https://docs.google.com/spreadsheets/d/1e-P8xpzcSfnCgOXtp0_RX9rhB42Zchpd07Ou0jmHfq4/edit?usp=sharing)
- Switch version is using `KiriKiri Z` engine while original PC release is using `CatSystem2`. It seems converting scenario from one engine to another produced some bugs to scene switches in Interlude, it's not an issue introduced with mod. Blame devs for not fixing them.
- CASE-2 chapter 5 has some lines using wrong `meswintype`. This mod fixes them
