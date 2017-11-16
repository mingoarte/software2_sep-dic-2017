// Crea un nuevo patron de interaccion una vez se selecciona en el sidebar.
// Tambien modifica la variable global i.
// NOTA: Por ahora esta funcion esta hecha para que solamente cree encuestas
// dado que es el unico patron de interaccion disponible
$(".captcha_pattern").on('click', function() {

  // Toma el contenedor del constructor y le agrega una nueva caja que representa
  // el nuevo patron escogido.
  $(".builder").append("<div id=card_captcha_"+i+" class='card-box'>" +
  	                     "<div class='btn-group pull-right'>" +
                           "<button type='button' class='btn btn-default waves-effect captcha-llaves'>Configurar</button>" +
  	                       "<button type='button' class='btn btn-danger waves-effect eliminar-captcha'>Eliminar</button>" +
  	                     "</div>" +
  	                     "<h1 class='header-title m-b-30'>CAPTCHA</h1>" +
  	                     "<div class='row'>" +
  	                       "<div class='col-md-12 pattern-content' style='text-align: center;'>" +
  	                       "</div>" +
  	                     "</div>" +
  	                     "<input type='hidden' name='card_position' value="+i+">" +
  	                   "</div>");
  i = i + 1;
});

// Permite acceder a las configuraciones de la nueva encuesta del template
$(document).on('click', "button.captcha-llaves", function() {
  // Declaracion de variables locales
  // id -> Contiene el id del contenedor del patron de interaccion que
  //       se quiere configurar.
  // content -> El formulario con la configuracion del patron de interaccion
  //            que se quiere configurar
  var id = $(this).parent().parent().attr('id');
  var content = $("#" + id + " div .pattern-content").html();

  // Llamada al API para generar llaves públicas y privadas.
  url = 'http://localhost:8000'
  $.ajax({
    url: '/servecaptcha/generate_apikey/',
    type: 'get',
    dataType: 'json',
    success: function(data) {
      $("#public_key").val(data.public_key);
      $("#private_key").val(data.private_key);
    },
    failure: function(data) {
      alert("nada");
    }
  });

  // Elimina la configuracion que estaba seteada en el modal de configuracion
  $("#captcha_keys div div .modal-body form").remove();

  // Se escribe lo que aparecerá en el modal.
  $("#captcha_keys div div .modal-body").append(
        '<form data-parsley-validate novalidate>' +
          '<input id="card-id" type="hidden" name="card-id">' +
          '<input id="position" type="hidden" name="position">' +
          '<div class="form-group">' +
            '<label for="public_key">Llave Pública</label>' +
            '<input type="text" name="public_key" parsley-trigger="change" required readonly ' +
                  'placeholder="Espere mientras generamos su llave pública." class="form-control" id="public_key">' +
            '<label for="private_key">Llave Privada</label>' +
            '<input type="text" name="private_key" parsley-trigger="change" required readonly ' +
                  'placeholder="Espere mientras generamos su llave privada." class="form-control" id="private_key">' +
          '</div>' +
        '</form>');

  // Se setean los valores de los input escondidos para la posicion y para el patron al que
  // pertenece la configuracion actual del form del modal.
  $('#card-id').val(id);
  $('#position').val(id.split("_")[2]);

  // Se muestra el modal.
  $('#captcha_keys').modal('show');
});

// Si se elige la opcion de eliminar un patron, se hace
// un request a la aplicacion para eliminar dicho patron
// de la bd
$(document).on('click', "button.eliminar-captcha", function(){
  var  id = $(this).parent().parent().attr('id')
  $('#position').val(id.split("_")[1]);
  $.ajax({
      url : "../erase-question/",
      data :  {'template': $('#template_id').val(),
                'position': $('#position').val()},

  })
  .done(function(data){
    card = document.getElementById(id);
    card.remove()
    });
});

// Hacer dos funcioens, una que se encargue de guardar la llave publica y la llave
// privada, y otra que se encargue de traerse en JSON todo para poder ponerlo en el HTML.
// Permite enviar request a la app para guardar en bd el nuevo patron que se creara
$('#accept_captcha').click( function saveCaptchaToTemplate() {
  $.ajax({
    method: 'POST',
    url : "../captcha-config/",
    data : {
            'template': $('#template_id').val(),
            'position': $('#position').val(),
           },
  }).done(function(data){
    var position = $('#position').val();
    $('#captcha_keys').modal('hide');
    // $('#card_'+position+' .pattern-content').html(
    //
    // );

  });
  $('#actualizarCaptcha').trigger("click");
});

$(document).on('click', '#actualizarCaptcha', function() {
  url = 'http://localhost:8000';
  console.log(url);
  $.ajax({
    url: '/servecaptcha/generate_captcha/{{public_key}}/',
    type: 'get',
    dataType: 'json',
    success: function(data) {
      $("#image_captcha").attr("src", url + "/servecaptcha/image/" + data.captcha_id);
      $("#captcha-id").val(data.captcha_id);
      $("#audioCaptcha").attr("src", url + "/servecaptcha/audio/" + data.captcha_id);
    },
    failure: function(data) {
      alert("nada");
    }
  });
});
