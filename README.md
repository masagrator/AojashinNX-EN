# AojashinNX-EN
English Translation Mod for Nintendo Switch version of game<br>`Hakuchuumu no Aojashin: The girl who's called the world` (Japanese title)<br>`Cyanotype Daydream -The Girl Who Dreamed the World-` (English title)

# Installation
1. Download package from Releases
2. Copy folder `01003B0018BC8000` to `atmosphere/contents/`
3. Play game

It should work with all game versions, mod is based on version 1.0.2<br>
It should work with any emulator, but for installation process seek help in emulators help sections or support (like dedicated Discords)

# Compiling scenario files
This section is only for people who want to use this repo as base for their translation or introduce changes.

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
- English textures are included with game originally, so mod reuses as much English textures as possible in story, but in CG Mode they are not changed. Some of those textures include typos (and in case of boot screen wrong translation of one sentence). You can find typos related to scenario in `Notes.txt`
- Apply.py injects break lines based on font file `SourceHanSansJP-Regular.otf` from `font` folder, thus why it takes much more time to finish. If you plan to replace font in game, you need to compile scripts with new font to fix break lines. Apply.py includes limitations aborting process if rendered text will take too much lines, which would otherwise result in text being unreadable.
- Some name labels were changed to make them shorter
- One CG was removed from Switch version, it was bringed back in this mod, though you cannot see it in CG mode. 
- There were some small changes to scenario. The biggest one is in Prologue. Any new line was machine translated. Changes that were not typo fixes can be found [here](https://docs.google.com/spreadsheets/d/1e-P8xpzcSfnCgOXtp0_RX9rhB42Zchpd07Ou0jmHfq4/edit?usp=sharing)
- Fixed many typos and wrongly translated lines introduced in original scenario files
- Game has some bugs that were not introduced with mod, this includes:
> - CASE-2 chapter 5 has some lines using wrong `meswintype` (fixed)
> - In "Interlude" scene switches related to branching paths have weird cuts (no plans to fix them)

# Thanks to (not directly involved with project)
- Contributors of [tlg2png](https://github.com/vn-tools/tlg2png)
- Contributors of [FreeMote](https://github.com/UlyssesWu/FreeMote)
