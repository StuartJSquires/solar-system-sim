import os
import glob

def prep_dir(pathway_address):

	status = os.path.isdir(pathway_address)

	if status == True:
		files = glob.glob(os.path.join(pathway_address, '*'))
		for f in files:
			os.remove(f)

	if status == False:
		os.makedirs(pathway_address)
