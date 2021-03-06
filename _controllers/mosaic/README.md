mosaic
========
An image gallery controller for [blogofile](https://github.com/EnigmaCurry/blogofile).

Installation With Git
---------------------------
If you have a git repository in your blogofile root, you can install this pretty easily.

Add this repository as remote so you can pull updates easily, then pull:

	git remote add mosaic git://github.com/startlingthings/blogofile-mosaic.git
	git pull mosaic master
	
Add the following lines to you config:

	# mosaic controller
	mosaic                  = controllers.mosaic
	mosaic.enabled          = True

You can also change, for example, the size of the thumbnails on your index page:

	mosaic.small			= (150, 150)
	
Images go in _photos by default. You can also have comments in this folder -- for example: if you had a photo called pegasus.jpg, you can have a comment saved as pegasus.jpg.markdown. You can have subdirectories, too, and the first photo alphabetically will be the "cover" for the subdirectory.

Installation Without Git
---------------------------
Copy the following from here:

	_controllers/mosaic/__init__.py
	_templates/mosaic_directory.mako
	_templates/mosaic_photo.mako
	
into the appropriate directories in your blogofile root.

Add the following lines to you config:

	# mosaic controller
	mosaic                  = controllers.mosaic
	mosaic.enabled          = True

You can also change, for example, the size of the thumbnails on your index page:

	mosaic.small			= (150, 150)
	
Images go in _photos by default. You can also have comments in this folder -- for example: if you had a photo called pegasus.jpg, you can have a comment saved as pegasus.jpg.markdown. You can have subdirectories, too, and the first photo alphabetically will be the "cover" for the subdirectory.