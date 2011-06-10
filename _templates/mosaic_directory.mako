<%inherit file="_templates/site.mako" />
My Photos:
<ul>
% for photo in photos:
	<li><a href="${photo}.html">${photo}</a></li>
% endfor
</ul>