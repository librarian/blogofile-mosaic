<%inherit file="_templates/site.mako" />
<center>
<a href="/${destination}/${photo}"><img src="/${destination}/large/${photo}"></a>
</center>
% if caption != None:
${caption}
% endif
