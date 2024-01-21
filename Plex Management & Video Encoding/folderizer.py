#FOLDERIZER - PUT YOUR STUFF IN FOLDERS
# 12/27/2022 - Joseph Peterson

import os

for n in os.scandir():
	if n.is_file():
		fileName = (n.path[2:-4])
		fileExt = (n.path[-3:])
		if(fileExt in ["iso"]):
			if not os.path.exists(fileName): os.makedirs(fileName)
			os.replace(f"{fileName}.{fileExt}", f"{fileName}/{fileName}.{fileExt}")	
