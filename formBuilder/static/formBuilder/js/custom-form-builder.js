var templates = {
  captcha: function(fieldData) {
    $('#captcha-html').find('.captcha-wrapper').data('public-key', fieldData.public_key);
    $('#captcha-html').find('.captcha-wrapper').attr('data-public-key', fieldData.public_key);
    html = $('#captcha-html').html();
    return {
      field: html,
      onRender: function() {
        console.log('Rendering captcha... ' + $('.captcha-wrapper'));
        $("#actualizarCaptcha").trigger('click');
      }
    };
  }
};

var fbOptions = {
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
  disabledActionButtons: ['data', 'clear', 'save']
};

function unescapeHTML(html) {
  dom = new DOMParser().parseFromString(html, "text/html");
  return dom.documentElement.textContent;
}


function captchaField(formData) {
  formData.forEach(function(e) {
    if (('type' in formField) && (formField.type == 'captcha')) {
      return e;
    }
  })
  return null;
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
  console.log(formData);
  $markup.formRender({
    formData: formData,
    templates: templates
  });
  return addLineBreaks($markup[0].innerHTML);
}
