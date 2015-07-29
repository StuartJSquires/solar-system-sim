import os
import glob

def prep_dir(pathway_address):

	status = os.path.isdir(pathway_address)

	if status = true:
		files = glob.glob(os.path.join(pathway_address,*))
		for f in files:
		os.remove(f)

	if status = false:
		os.makedirs(pathway_address)