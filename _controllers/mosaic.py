import os
import shutil
from PIL import Image
from blogofile.cache import bf

config = {	
			"name"        	: 	"mosaic",	
			"description" 	: 	"A gallery.",
			"author"		:	"startlingthings@gmail.com",
			"url"         	: 	"github.com/startlingthings",
			"path"			: 	"mosaic",
			"dir"			:	"_photos",
			"enable"		:	False,
			"small"			:	(128, 128),
			"large"			:	(400, 400),
		}

def run():
	os.mkdir(os.path.join("_site", config['path']))
	photos	= read_photos(config['dir'])
	copy(photos)
	resize(photos, config['small'], "small")
	resize(photos, config['large'], "large")
	index(photos)
	photo_pages(photos)

def copy(photos):
	for photo in photos:
		shutil.copy2(os.path.join(config['dir'], photo), os.path.join("_site",config['path'],photo))

def resize(photos, size, destination):
	os.mkdir(os.path.join("_site", config['path'], destination))
	for photo in photos:
		original	= os.path.join(config['dir'], photo)
		to			= os.path.join("_site", config['path'], destination, photo)
		file, ext 	= os.path.splitext(original)
		im 			= Image.open(original)
		im.thumbnail(size, Image.ANTIALIAS)
		im.save(to)

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
