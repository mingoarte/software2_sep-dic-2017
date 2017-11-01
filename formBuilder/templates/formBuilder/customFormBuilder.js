function unescapeHTML(html) {
  dom = new DOMParser().parseFromString(html, "text/html");
  return dom.documentElement.textContent;
}

function isCaptcha(formField) {
  return ('type' in formField) && (formField.type == 'captcha');
}

var templates = {
  captcha: function(fieldData) {
    captchaHTML = unescapeHTML(`{{escapedCaptchaHTML}}`);
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
      i18n: {
  			locale: 'es-ES'
  		},
      onSave: function(e, formData) {
        $('.render-wrap').formRender({
          formData: formData,
          templates: templates
        });
        var escapeEl = document.createElement('textarea');
        var code = document.getElementById('markup');
        var escapeHTML = function(html) {
          escapeEl.textContent = html;
          return escapeEl.innerHTML;
        };
        var addLineBreaks = function(html) {
          return html.replace(new RegExp('&gt; &lt;', 'g'), '&gt;\n&lt;').replace(new RegExp('&gt;&lt;', 'g'), '&gt;\n&lt;');
        };
        var $markup = $('<div/>');
        $markup.formRender({formData});
        var html = $markup[0].innerHTML;
        var parsedData = JSON.parse(formData);
        var captchaData = parsedData.find(isCaptcha)
        if (captchaData) {
          $.get({
            url: '/servecaptcha/captcha.js',
            data: {
              public_key: encodeURIComponent(captchaData.public_key)
            },
            success: function(captchaJS) {
              captchaJS = unescapeHTML(`&lt;script&gt;\n${captchaJS}\n&lt;/script&gt;`)
              html += captchaJS;
              code.innerHTML = addLineBreaks(escapeHTML(html));
            }
          });
        } else {
          code.innerHTML = addLineBreaks(escapeHTML(html));
        }
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
            maxlength: '64'
          }
        }
      }
    },
    formBuilder = $fbEditor.formBuilder(fbOptions);

  $('.edit-form', $formContainer).click(function() {
    $fbEditor.toggle();
    $formContainer.toggle();
  });
});
