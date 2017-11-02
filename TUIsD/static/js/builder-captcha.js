// Declaracion de variables globales
// i -> Lleva la cuenta de los patrones de interaccion creados en el template para
//      crear los id's de los contenedores de los mismos.
var i = 0

// Prevenimos el comportamiento por default del form de hacer post
$(".forms").click(function() {
  event.preventDefault();
});

// Crea un nuevo patron de interaccion una vez se selecciona en el sidebar.
// Tambien modifica la variable global i.
// NOTA: Por ahora esta funcion esta hecha para que solamente cree encuestas
// dado que es el unico patron de interaccion disponible
$(".captcha_pattern").on('click', function() {

  // Toma el contenedor del constructor y le agrega una nueva caja que representa
  // el nuevo patron escogido.
  $(".builder").append("<div id=card_captcha_"+i+" class='card-box'>" +
  	                     "<div class='btn-group pull-right'>" +
                           "<button type='button' class='btn btn-default waves-effect captcha-llaves'>Generar llaves</button>" +
                           "<button type='button' class='btn btn-default waves-effect captcha-generar'>Generar Captcha</button>" +
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


// Permite acceder a las configuraciones de la nueva encuesta del template
$(document).on('click', "button.captcha-generar", function() {
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

  // Elimina la configuracion que estaba seteada en el modal de configuracion
  $("#new_captcha div div .modal-body form").remove();

  // Se escribe lo que aparecerá en el modal.
  $("#new_captcha div div .modal-body").append(
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
  $('#new_captcha').modal('show');
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

// Permite enviar request a la app para guardar en bd el nuevo patron que se creara
$('#accept_captcha').click(function(){
  // Declaracion de variables locales
  // public_key: La llave pública del CAPTCHA.

  var public_key = $("#captcha_keys div div .modal-body form div input[name='public_key']").val()
  console.log(public_key)

  // Llamada al API para generar llaves públicas y privadas.
  url = 'http://localhost:8000'
  $.ajax({
    url: '/servecaptcha/generate_captcha/' + public_key + '/',
    type: 'get',
    dataType: 'json',
    failure: function(data) {
      alert("nada");
    },
    success: function(data) {
      // Declaracion de variables locales
      //     // content -> El contenido extraido del modal de configuracion
      //     // id -> El identificador del patron de interaccion que se esta
      //     //       configurando
      var content = $("#captcha_keys").parent().prev().html();
      var id = "#" + $("#card-id").val() + " div .pattern-content";
      console.log(id);

      // Se vacia el contenedor del patron de interaccion y se rellena
      // con la informacion del formulario del modal
      $(id).empty();
      $(id).append(content);

      // Se eliminan las opciones y las preguntas, asi como el boton del contenido
      // del patron de interaccion
      $(id + " form div").remove();
      $(id + " form a").remove();

      // Se obtienen las variables.
      $("#image_captcha").attr("src", url + "/servecaptcha/image/" + data.captcha_id);
      $("#captcha-id").val(data.captcha_id);
      $("#audioCaptcha").attr("src", url + "/servecaptcha/audio/" + data.captcha_id);

  //     // Se agrega el input de la pregunta y se llena con la informacion original de la
  //     // pregunta
  //     $(id + " div .col").append(<img id="image_captcha" class="card-img-top" src="" />
  //
  //       '<div class="form-group">' +
  //                              '<label for="pregunta">Pregunta</label>' +
  //                              '<input type="text" name="pregunta" parsley-trigger="change" required ' +
  //                                     'placeholder="Escriba la pregunta de la encuesta" class="form-control" ' +
  //                                     'id="pregunta">' +
  //                            '</div>');
  //     $(id + " form div #pregunta").val(data.question[0].texto_pregunta);
  //
  //     // Se agregan los inputs de las opciones de la encuesta y se llenam con la informacion
  //     // original de cada pregunta
  //     for (j = 0; j < data.options.length; j++) {
  //       $(id + " form").append('<div class="form-group">' +
  //                                '<label for="opcion">Opcion:</label>' +
  //                                '<input type="text" name="opcion" parsley-trigger="change" required ' +
  //                                       'placeholder="Escriba la opcion" class="form-control" id="opcion">' +
  //                              '</div>');
  //     }
    }
  });
  //
  // $.ajax({
  //   url : "../poll-config/",
  //   data : {
  //           'pregunta': pregunta,
  //           'opciones': opciones,
  //           'template': $('#template_id').val(),
  //           'position': $('#position').val(),
  //          },
  //
  // })
  // .done(function(data){
  //     // Declaracion de variables locales
  //     // content -> El contenido extraido del modal de configuracion
  //     // id -> El identificador del patron de interaccion que se esta
  //     //       configurando
  //     var content = $("#accept_captcha").parent().prev().html();
  //     var id = "#" + $("#card-id").val() + " div .pattern-content";
  //     console.log(id);
  //
  //     // Se vacia el contenedor del patron de interaccion y se rellena
  //     // con la informacion del formulario del modal
  //     $(id).empty();
  //     $(id).append(content);
  //
  //     // Se eliminan las opciones y las preguntas, asi como el boton del contenido
  //     // del patron de interaccion
  //     $(id + " form div").remove();
  //     $(id + " form a").remove();
  //
  //     // Se agrega el input de la pregunta y se llena con la informacion original de la
  //     // pregunta
  //     $(id + " form").append('<div class="form-group">' +
  //                              '<label for="pregunta">Pregunta</label>' +
  //                              '<input type="text" name="pregunta" parsley-trigger="change" required ' +
  //                                     'placeholder="Escriba la pregunta de la encuesta" class="form-control" ' +
  //                                     'id="pregunta">' +
  //                            '</div>');
  //     $(id + " form div #pregunta").val(data.question[0].texto_pregunta);
  //
  //     // Se agregan los inputs de las opciones de la encuesta y se llenam con la informacion
  //     // original de cada pregunta
  //     for (j = 0; j < data.options.length; j++) {
  //       $(id + " form").append('<div class="form-group">' +
  //                                '<label for="opcion">Opcion:</label>' +
  //                                '<input type="text" name="opcion" parsley-trigger="change" required ' +
  //                                       'placeholder="Escriba la opcion" class="form-control" id="opcion">' +
  //                              '</div>');
  //     }
  //
  //     $(id + " form div #opcion").each(function(index) {
  //       $(this).val(data.options[index].texto_opcion);
  //     })
  //
  //     $('#guardar').show();
  //     var tem_id = $('#template_id').val().toString()
  //     var link = "/revisar_template/"+ tem_id
  //     $('#preview').attr('href',link)
  //     $('#preview-form').attr('action',link)
  //     $('#frm1_submit').show();
  //     $('#preview').show();
  //
  // });
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
