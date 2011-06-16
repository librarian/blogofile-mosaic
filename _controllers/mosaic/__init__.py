import os, shutil
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
	directory(config['dir'], config['path'])


def directory(source, destination):
	both = os.path.join("_site", destination)
	os.mkdir(both)
	photos	= read_photos(source)
	copy(photos, source, both)
	resize(photos, both, "small", config['small'])
	resize(photos, both, "large", config['large'],)
	index(photos, destination)
	photo_pages(photos, destination, source)

def copy(photos, source, destination):
	for photo in photos:
		shutil.copy2(os.path.join(source, photo), os.path.join(destination,photo))

def resize(photos, destination, subfolder, size):
	os.mkdir(os.path.join(destination, subfolder))
	for photo in photos:
		original	= os.path.join(destination, photo)
		to			= os.path.join(destination, subfolder, photo)
		im 			= Image.open(original)
		im.thumbnail(size, Image.ANTIALIAS)
		im.save(to)

def read_photos(directory):
	photos	= ([])
	for p in os.listdir(directory):
		if p.lower().endswith(".jpg"):
			photos.append(p)
	return photos

def photo_pages(photos, destination, source):
	for photo in photos:
		bf.writer.materialize_template(
			"mosaic_photo.mako",
			(destination, photo+".html"), 
			{"photo":photo, "caption":caption(source, photo)}
		)

def caption(source, photo):
	for f in os.listdir(source):
		if f.startswith(photo + "."):
			file_extension = os.path.splitext(f)[-1][1:]
			contents 	= open(os.path.join(config['dir'], f), 'r').read()
			filters 	= bf.config.controllers.blog.post_default_filters[file_extension]
			filtered	= bf.filter.run_chain(filters, contents)
			return filtered

def index(photos, destination):
	bf.writer.materialize_template(
		"mosaic_directory.mako",
		(destination,"index.html"), 
		{"photos":photos}
	)
