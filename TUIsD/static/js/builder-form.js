// variable global que guarda el form builder
var $formBuilder = null;

function sendFormData() {
  formData = $formBuilder.formData;
  return {
    url : "../form-config/",
    data : {
      'form_json': formData,
    }
  }
}

function afterLoadFormConfigModal() {

  var $fbEditor = $(document.getElementById('fb-editor')),
      $formContainer = $(document.getElementById('fb-rendered-form')),
      fbOptions = {
        disabledActionButtons: ['data', 'clear', 'save']
      }

  // Initialize form builder plugin
  $formBuilder = $fbEditor.formBuilder(fbOptions);
}
function afterSendFormData(data) {
  $(".pattern-container[data-position='"+ data.position +"'] .fb-rendered-form").html(formDataToHTML(data.form_json));
}