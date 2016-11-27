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
    'formula': true,
    'history': true,
    'syntax': true,
    'toolbar': toolbarOptions,
  }
});
