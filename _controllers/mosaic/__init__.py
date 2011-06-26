import os, shutil
from PIL import Image, ImageDraw, ImageFont
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
			"dir_thumb"		:	(128, 128),
		}

def run():
	directory(config['dir'], config['path'], "")


def directory(source, destination, short):
	both = os.path.join("_site", destination)
	os.mkdir(both)
	photos, directories	= read(source)
	copy(photos, source, both)
	resize(photos, both, "small", config['small'])
	resize(photos, both, "large", config['large'],)
	directory_thumb(photos[0], source, both, short)
	index(photos, destination, directories)
	photo_pages(photos, destination, source)
	for d in directories:
		directory(os.path.join(source, d), os.path.join(destination, d), d)

def copy(photos, source, destination):
	for photo in photos:
		shutil.copy2(os.path.join(source, photo), os.path.join(destination,photo))

def directory_thumb(photo, source, destination, short):
	original	= os.path.join(source, photo)
	to			= os.path.join(destination, "index.jpg")
	
	im 			= Image.open(original)
	im.thumbnail(config['dir_thumb'], Image.ANTIALIAS)
	
	x, y		= im.size
	down		= int(y * .8)
	height		= 10
	
	draw 		= ImageDraw.Draw(im)
	draw.rectangle([(0, down),(x, down + height)], fill="#ffffff")
	font		= ImageFont.load_default()
	draw.text((2, down), short, font=font, fill="#000000")
	
	im.save(to)

def resize(photos, destination, subfolder, size):
	os.mkdir(os.path.join(destination, subfolder))
	for photo in photos:
		original	= os.path.join(destination, photo)
		to			= os.path.join(destination, subfolder, photo)
		im 			= Image.open(original)
		im.thumbnail(size, Image.ANTIALIAS)
		im.save(to)

def read(directory):
	photos		= ([])
	directories	= ([])
	for p in os.listdir(directory):
		if p.lower().endswith(".jpg"):
			photos.append(p)
		if os.path.isdir(os.path.join(directory, p)):
			directories.append(p)
	return photos, directories

def photo_pages(photos, destination, source):
	for photo in photos:
		bf.writer.materialize_template(
			"mosaic_photo.mako",
			(destination, photo+".html"), 
			{"photo":photo, "caption":caption(source, photo),"destination":destination}
		)

def caption(source, photo):
	for f in os.listdir(source):
		if f.startswith(photo + "."):
			file_extension = os.path.splitext(f)[-1][1:]
			contents 	= open(os.path.join(config['dir'], f), 'r').read()
			filters 	= bf.config.controllers.blog.post_default_filters[file_extension]
			filtered	= bf.filter.run_chain(filters, contents)
			return filtered

def index(photos, destination, directories):
	bf.writer.materialize_template(
		"mosaic_directory.mako",
		(destination,"index.html"), 
		{"photos":photos, "directories":directories, "destination": destination}
	)
