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

    var wordLabel = lengths.words > 1 ? ' words' : ' word';
    var charLabel = lengths.chars > 1 ? ' characters' : ' character';

    this.wordContainer.innerHTML = lengths.words + wordLabel;
    this.charContainer.innerHTML = lengths.chars + charLabel;
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

quill.setContents(JSON.parse(document.getElementById('#scribe-content').innerHTML.trim()));

var form = document.querySelector('form');
form.onsubmit = function() {
  var about = document.querySelector('input[name=entry]');
  about.value = JSON.stringify(quill.getContents());
  form.submit();
};
