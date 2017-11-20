function sendPatternData(patternName) {
  // Agrega aqui la referencia a la funcion que devuelve { url: ..., data:... }
  // para crear/guardar tu patron.
  ajaxOptsPatterns = {
    'encuesta': sendPollData,
    'formulario': sendFormData,
    'faq': sendFAQData,
    'captcha': sendCaptchaData,
  };
  
  ajaxOpts = ajaxOptsPatterns[patternName.toLowerCase()]();
  ajaxOpts.data.template = $('#template_id').val();
  ajaxOpts.data.position = $('#modal-configuracion').data('position');
  ajaxOpts.method = 'POST';

  return $.ajax(ajaxOpts);
}

function afterLoadPatternConfigModal(patternName) {
  // Funcion que se ejecuta al cargar el modal INICIAL (no al editar)
  patternFuncs = {
    'encuesta': afterLoadPollConfigModal,
    'formulario': afterLoadFormConfigModal,
    'faq': afterLoadFAQConfigModal,
    'captcha': afterLoadCaptchaConfigModal,
  }

  if (patternFuncs.hasOwnProperty(patternName)) {
    patternFuncs[patternName]();
  }
}

function afterSendPatternData(patternName, data) {
  // Funcion opcional que se ejecuta luego de guardar satisfactoriamente tu patron.
  // Recibe como argumento el objeto json data recibido como respuesta al guardar/crear
  patternFuncs = {
    'formulario': afterSendFormData
  }

  if (patternFuncs.hasOwnProperty(patternName)) {
    patternFuncs[patternName](data);
  }
}


$(".forms").click(function() {
  event.preventDefault();
});

$(".pattern").on('click', function() {
  patternName = $(this).data('pattern-name');
  // Limpiar modal
  $('#modal-configuracion .modal-dialog').html('');
  $.get({
    url: '/builder/config-modal',
    data: {
      "pattern-name": patternName
    },
    success: function (res) {
      $('#modal-configuracion .modal-dialog').html(res);
      $('#modal-configuracion').data('pattern-name', patternName);
      afterLoadPatternConfigModal(patternName);
    }
  })
  $('#modal-configuracion').modal('show');
});

// Permite acceder a las configuraciones de la nueva encuesta del template
$(document).on('click', "button.config", function() {
  patternContainer = $(this).parents('.pattern-container');
  patternName = patternContainer.data('pattern-name');
  templateComponentID = patternContainer.data('template-component-id');
  position = patternContainer.data('position');

  // Settear nombre del patron, el id del componente y su posición en el modal para usarlo al momento de guardar los cambios
  $('#modal-configuracion').data('pattern-name', patternName);
  $('#modal-configuracion').data('template-component-id', templateComponentID);
  $('#modal-configuracion').data('position', position);

  // Limpiar modal
  $('#modal-configuracion .modal-dialog').html('');
  $.get({
    url: '/builder/config-modal',
    data: {
      "template-component-id": templateComponentID
    },
    success: function (res) {
      $('#modal-configuracion .modal-dialog').html(res);
    }
  })
  $('#modal-configuracion').modal('show');
});

// Si se elige la opcion de eliminar un patron, se hace
// un request a la aplicacion para eliminar dicho patron
// de la bd
$(document).on('click', "button.eliminar", function(){
  patternContainer = $(this).parents('.pattern-container');
  templateComponentID = patternContainer.data('template-component-id');
  $.ajax({
      url: "/builder/delete-pattern",
      data: {
        'template-component-id': templateComponentID
      }

  })
  .done(function(data){
    patternContainer.remove()
  });
});

// Permite enviar request a la app para guardar en bd el nuevo patron que se creara
$(document).on('click', 'button.accept-modal', function(e){
  /* Cada patron envia su data de la forma que quiera, lo que importa es que el servidor retorne un json de la forma
   *
   *  {
        "position": <Posicion en el template>,
        "html": <HTML a mostrar en el card>
      }
   *
   */

  patternName = $('#modal-configuracion').data('pattern-name');
  console.log("Enviando data del patron ", patternName);

  sendPatternData(patternName).done(function(data){

      if (data.position != null) {
        // Si se esta editando el patron, modificar el card existente
        if ($(".pattern-container[data-position='"+ data.position +"']").length) {
          $(".pattern-container[data-position='"+ data.position +"']").replaceWith(data.html);
        }
        else {
          $(".builder").append(data.html);
        }
      }

      $('#guardar').show();
      var tem_id = $('#template_id').val().toString()
      var link = "/revisar_template/"+ tem_id
      $('#preview').attr('href',link)
      $('#preview-form').attr('action',link)
      $('#frm1_submit').show();
      $('#preview').show();

      // Limpiar modal
      $('#modal-configuracion').data('pattern-name', patternName);
      $('#modal-configuracion').data('template-component-id', templateComponentID);
      $('#modal-configuracion').data('position', position);

      afterSendPatternData(patternName, data);
  });
})

// Una vez tenemos el nombre del template se hace request a la
// aplicacion para guardar el nuevo template en bd
$('#accept_name_template').click(function(){
  $('#title').text($('#template_name').val())
  $.ajax({
      url : "../new-template/",
      data :  {'name': $('#template_name').val()},

  })
  .done(function(data){
    if(data){
      $('#template_id').val(data.id);
      $('#new_template').modal('hide');
    }
  });
});
