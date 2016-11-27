var toolbarOptions = [
  [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
  ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
  ['blockquote', 'code-block'],
  [{ 'list': 'ordered'}, { 'list': 'bullet' }],
  [{ 'script': 'sub'}, { 'script': 'super' }],      // superscript/subscript

  [{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme
  [{ 'align': [] }],
  ['clean']                                         // remove formatting button
];
var quill = new Quill('#scriptor', {
  theme: 'snow',
  strict: false,
  modules: {
    'clipboard': true,
    'history': true,
    'toolbar': toolbarOptions,
  }
});
if(typeof(String.prototype.trim) === "undefined")
{
    String.prototype.trim = function()
    {
        return String(this).replace(/^\s+|\s+$/g, '');
    };
}

quill.setContents(JSON.parse(document.getElementById('#scribe-content').innerHTML.trim()));

var form = document.querySelector('form');
form.onsubmit = function() {
  var about = document.querySelector('input[name=entry]');
  about.value = JSON.stringify(quill.getContents());
  form.submit();
};
