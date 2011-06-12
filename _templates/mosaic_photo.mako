<%inherit file="_templates/site.mako" />
<center>
<a href="${photo}"><img src="large/${photo}"></a>
</center>
% if caption != None:
${caption}
% endif
