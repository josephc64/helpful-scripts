import subprocess, os

os.chdir('..\Bin\Emu')                          #Directory in which to execute the script
command = "retroarch.exe"                       #Emulator .exe
core = r".\cores\RETROARCH-CORE.dll"            #Retroarch core
rom = r".\roms\ROM.EXT"                         #ROM
args = ["-L", core, rom]                        #Combined Arguments

subprocess.run([command] + args, shell=True)    #Assembled Command