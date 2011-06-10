import os
import shutil
from blogofile.cache import bf

config = {	
			"name"        	: 	"mosaic",	
			"description" 	: 	"A gallery.",
			"author"		:	"startlingthings@gmail.com",
			"url"         	: 	"github.com/startlingthings",
			"path"			: 	"mosaic",
			"dir"			:	"_photos",
			"enable"		:	False,
		}

def run():
	os.mkdir(os.path.join("_site", config['path']))
	photos	= read_photos(config['dir'])
	copy(photos)
	index(photos)
	photo_pages(photos)

def copy(photos):
	for photo in photos:
		shutil.copy2(os.path.join(config['dir'], photo), os.path.join("_site",config['path'],photo))

def read_photos(directory):
	photos	= ([])
	for p in os.listdir(directory):
		if p.lower().endswith(".jpg"):
			photos.append(p)
	return photos

def photo_pages(photos):
	for photo in photos:
		bf.writer.materialize_template("mosaic_photo.mako",(config['path'],photo+".html"), 
			{"photo":photo})

def index(photos):
	bf.writer.materialize_template("mosaic_directory.mako",(config['path'],"index.html"), 
		{"photos":photos})
