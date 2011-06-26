<%inherit file="_templates/site.mako" />
<br>
<center>
% for d in directories:
	<a href="/${destination}/${d}/"><img src="/${destination}/${d}/index.jpg"></a>
% endfor
% for photo in photos:
	<a href="/${destination}/${photo}.html"><img src="/${destination}/small/${photo}"</a>
% endfor
</center>
