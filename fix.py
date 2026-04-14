import os
import shutil
import subprocess

paris_cwd = os.getcwd()

for answer in os.listdir(paris_cwd + '/ans_folders'):
	for answer2 in os.listdir(paris_cwd + '/ans_folders/'+answer):
		# print(answer2)
		shutil.copy(paris_cwd + '/ans_folders/'+answer + '/'+answer2, paris_cwd + '/ans')

toremove = []
for f in os.listdir(paris_cwd + '/ans'):
	oldname = paris_cwd+'\\ans\\'+f
	newname = oldname.replace(' ', '')
	newf = f.replace(' ', '')
	# print(newname)
	os.rename(oldname, newname)
	
	if '.ipynb' in newname:
		print(newf)
		subprocess.run(['cmd', '/c', "jupyter nbconvert --to script "+newname])

		newnamepy = newname.replace('.ipynb', '.py')
		if os.path.isfile(newnamepy):
			toremove.append(newname)

for file in toremove:
	os.remove(file)
