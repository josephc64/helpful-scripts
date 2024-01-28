# Joseph Peterson
# 01/28/2024
# Shortpacker - Uses PyInstaller + Image2Icon to create a shortcut
import os, sys, subprocess, shutil
from image2icon import convertImageToIco


def packer(finalName):
    # Create temp directory if it does not exist, then
    # move necessary files into it, and enter it.
    if not os.path.exists("./temp"): os.makedirs("./temp")
    os.replace("script.py", "./temp/script.py")
    os.replace("icon.png", "./temp/icon.png")
    os.chdir("./temp")

    # Convert icon.png into an icon file, then pack it
    # and the script into a pyInstaller .exe file
    convertImageToIco('icon.png')
    subprocess.run(f"pyinstaller --onefile --icon=icon.ico script.py")

    # Move the finished product out of the temp folder,
    # and back into the execution folder.
    shutil.move("./dist/script.exe", f"../{finalName}.exe")

    # Delete all temporary files
    shutil.rmtree("../__pycache__")
    shutil.rmtree("build")
    shutil.rmtree("dist")
    os.remove("script.spec")
    os.remove("icon.ico")

    # Move back into execution folder and turn the
    # temp folder into 'original-files', which now
    # only contains the original files.
    os.chdir("../")
    if not os.path.exists("original-files"):
        os.rename("temp", "original-files")
    else:
        allTemp = os.listdir("temp")
        for fileName in allTemp:
            os.rename(f"temp/{fileName}", f"original-files/{fileName}")


# Name defaults to 'script' if one is not specified
def main(name="script"):
    if len(sys.argv) > 1:
        for file in sys.argv[1:]:
            name = file
    packer(name)


if __name__ == "__main__":
    main()