# AojashinNX-EN
English Translation Mod for Nintendo Switch version of game `Hakuchuumu no Aojashin: The girl who's called the world` (Japanese title) / `Cyanotype Daydream -The Girl Who Dreamed the World-` (English title)

# Compiling scenario files
Requirements:
- Windows 7+
- Python 3.10+
- Python library `pyvips` (to work it requires adding [vips](https://github.com/libvips/libvips/releases) bin folder to PATH)
- psbuild (you can download it from [here](https://github.com/UlyssesWu/FreeMote/releases/tag/v3.4.0)

1. From FreeMoteToolkit copy: `PsbDecompile.exe`, `PsbDecompile.exe.config`, `PsBuild.exe`, `PsBuild.exe.config` and folder `lib` to root folder of repository
2. From romfs of game copy folders `scn` and `font` to root folder of repository
3. Use "decompile.cmd"
4. Run "Apply.py"
5. Run "Compile.py"
6. New scn files can be found in `Compiled` folder
