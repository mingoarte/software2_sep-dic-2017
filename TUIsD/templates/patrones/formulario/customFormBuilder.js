function unescapeHTML(html) {
  dom = new DOMParser().parseFromString(html, "text/html");
  return dom.documentElement.textContent;
}

function isCaptcha(formField) {
  return ('type' in formField) && (formField.type == 'captcha');
}

function formDataToHTML(formData) {
  var escapeHTML = function(html) {
    escapeEl.textContent = html;
    return escapeEl.innerHTML;
  };
  var addLineBreaks = function(html) {
    return html.replace(new RegExp('&gt; &lt;', 'g'), '&gt;\n&lt;').replace(new RegExp('&gt;&lt;', 'g'), '&gt;\n&lt;');
  };
  var $markup = $('<div/>');
  $markup.formRender({formData});
  return addLineBreaks($markup[0].innerHTML);
}

function saveFormToTemplate(formData) {
  $.ajax({
    method: 'POST',
    url : "../form-config/",
    data : {
            'form_json': formData,
            'template': $('#template_id').val(),
            'position': $('#position').val(),
           },
  }).done(function(data){
    $('#new-form-modal').modal('hide');
    $('#card_'+editingID+' .pattern-content').html(formDataToHTML(formData));
  });
}

var templates = {
  captcha: function(fieldData) {
    captchaHTML = unescapeHTML(`{% include 'patrones/captcha/view.html' %}`);
    return {
      field: captchaHTML,
      onRender: function() {
        $("#actualizarCaptcha").trigger('click');
      }
    };
  }
};

jQuery(function($) {
  var $fbEditor = $(document.getElementById('fb-editor')),
    $formContainer = $(document.getElementById('fb-rendered-form')),
    fbOptions = {
      onSave: function(e, formData) {
        $('.render-wrap').formRender({
          formData: formData,
          templates: templates
        });
        saveFormToTemplate(formData);
        // TODO: Refactorizar, DRY
        $('#guardar').show();
        var tem_id = $('#template_id').val().toString()
        var link = "/revisar_template/"+ tem_id
        $('#preview').attr('href',link)
        $('#preview-form').attr('action',link)
        $('#frm1_submit').show();
        $('#preview').show();
      },
      i18n: {
        locale: 'es-ES'
      },
      templates: templates,
      fields: [{
        label: 'Captcha',
        attrs: {
          type: 'captcha'
        },
        icon: 'C '
      }],
      typeUserAttrs: {
        captcha: {
          public_key: {
            label: 'Clave pública',
            value: 'demoPublicKey',
            maxlength: '64'
          }
        }
      },
      disabledActionButtons: ['data', 'clear']
    },
    formBuilder = $fbEditor.formBuilder(fbOptions);
});
