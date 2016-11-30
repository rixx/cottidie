/* Counter class was taken from the quill guide for writing modules
at http://quilljs.com/guides/building-a-custom-module/ */
class Counter {
  constructor(quill, options) {
    this.quill = quill;
    this.options = options;
    this.wordContainer = document.querySelector(options.wordContainer);
    this.charContainer = document.querySelector(options.charContainer);
    quill.on('text-change', this.update.bind(this));
    this.update();
  }

  calculate() {
    let text = this.quill.getText();
    text = text.trim();
    return {
      'words': text.length > 0 ? text.split(/\s+/).length : 0,
      'chars': text.length,
    }
  }

  update() {
    var lengths = this.calculate();

    this.wordContainer.innerHTML = lengths.words;
    this.charContainer.innerHTML = lengths.chars;
  }
}

Quill.register('modules/counter', Counter);
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
    'counter': {
      wordContainer: '#scribe-words',
      charContainer: '#scribe-chars',
    }
  }
});

if(typeof(String.prototype.trim) === "undefined")
{
    String.prototype.trim = function()
    {
        return String(this).replace(/^\s+|\s+$/g, '');
    };
}

quill.root.innerHTML = document.getElementById('#scribe-content').innerHTML.trim();

var form = document.querySelector('form');
form.onsubmit = function() {
  var text = document.querySelector('input[name=entry]');
  var words = document.querySelector('input[name=words]');
  var characters = document.querySelector('input[name=characters]');

  text.value = quill.root.innerHTML;
  words.value = document.querySelector('#scribe-words').innerHTML;
  characters.value = document.querySelector('#scribe-chars').innerHTML;
  form.submit();
};
