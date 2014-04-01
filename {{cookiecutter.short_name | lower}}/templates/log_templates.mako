 <!-- An example log template -->
 <script type="text/html" id="{{cookicutter.short_name}}_file_added">
added file
{%raw%}
<a class="overflow log-file-link" data-bind="click: NodeActions.addonFileRedirect">{{ params.path }}</a> to
Dropbox in {{ nodeCategory }}
<a class="log-node-title-link overflow" data-bind="attr: {href: nodeUrl}">{{ nodeTitle }}</a>
</script>
{%endraw%}
