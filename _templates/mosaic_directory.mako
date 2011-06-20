<%inherit file="_templates/site.mako" />
<br>
<center>
% for d in directories:
	<a href="${d}/"><img src="${d}/index.jpg"></a>
% endfor
% for photo in photos:
	<a href="${photo}.html"><img src="small/${photo}"</a>
% endfor
</center>