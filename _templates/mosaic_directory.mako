<%inherit file="_templates/site.mako" />
<br>
<center>
% for photo in photos:
	<a href="${photo}.html"><img src="small/${photo}"</a>
% endfor
</center>