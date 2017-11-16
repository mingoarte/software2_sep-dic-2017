$(".forms").click(function() {
  event.preventDefault();
});

// Crea un nuevo patron de interaccion una vez se selecciona en el sidebar.
// Específicamente, crea el patrón CAPTCHA.
// Esta función debe escribir el HTML que tendrá el Modal y al final deberá
// mostrarlo con un show.
$(".pattern-captcha").on('click', function() {
  // Elimina la configuracion que estaba seteada en el modal de configuración
  // De esta manera se sabe que se trabajará siempre en un captcha nuevo.
  $("#captcha_keys div div .modal-body form").remove();

  // Inserta el HTML en el modal. Aún no se han hecho las llamadas correspondientes
  // para llenar las llaves. Este HTML se inserta en el body del modal.
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

  // Se procede a hacerse las llamadas al Backend para obtener las llaves públicas
  // y privadas del captcha.
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

  $('#captcha_keys').modal('show');


  // // Toma el contenedor del constructor y le agrega una nueva caja que representa
  // // el nuevo patron escogido.
  // $(".builder").append("<div id=card_captcha_"+i+" class='card-box'>" +
  // 	                     "<div class='btn-group pull-right'>" +
  //                          "<button type='button' class='btn btn-default waves-effect captcha-llaves'>Configurar</button>" +
  // 	                       "<button type='button' class='btn btn-danger waves-effect eliminar-captcha'>Eliminar</button>" +
  // 	                     "</div>" +
  // 	                     "<h1 class='header-title m-b-30'>CAPTCHA</h1>" +
  // 	                     "<div class='row'>" +
  // 	                       "<div class='col-md-12 pattern-content' style='text-align: center;'>" +
  // 	                       "</div>" +
  // 	                     "</div>" +
  // 	                     "<input type='hidden' name='card_position' value="+i+">" +
  // 	                   "</div>");
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

// Esta es la función que toma la configuración del Captcha hecha en el modal
// y que se envía al servidor para que lo guarde en la BD.
$('#accept_keys').click( function saveCaptchaToTemplate() {
  $.ajax({
    method: 'POST',
    url : "../captcha-config/",
    data : {
            'public_key': $('#public_key').val(),
            'private_key': $('#private_key').val(),
            'template': $('#template_id').val(),
            'position': $('#position').val(),
           },
  })
  .done(function(data){
    // Cuando se regrese del AJAX qué se hará.
    // Declaracion de variables locales
    // content -> El contenido extraido del modal de configuracion
    // id -> El identificador del patron de interaccion que se esta
    //       configurando
    console.log(data)
    if (data.position != null){
      // Toma el contenedor del constructor y le agrega una nueva caja que representa
      // el nuevo patron escogido. Esto significa que se está creando el card
      // donde se mostará la configuración del patrón.
      $(".builder").append(
        "<div id=card_"+data.position+" class='card-box'>" +
          "<div class='btn-group pull-right'>" +
           "<button data-position="+data.position+" type='button' class='btn btn-default waves-effect config'>Configurar</button>" +
           "<button data-position="+data.position+" type='button' class='btn btn-danger waves-effect eliminar'>Eliminar</button>" +
          "</div>" +
          "<h1 class='header-title m-b-30'>Captcha</h1>" +
          "<div class='row'>" +
           "<div class='col-md-12 pattern-content' style='text-align: left;'>" +
           "</div>" +
          "</div>" +
          "<input type='hidden' name='card_position' value="+data.position+">" +
        "</div>");
    }else{
      // No se hace nada si ya está configurado el patrón.
    }
    // Se obtiene el contenido del modal y el ID del card completo.
    var content = $("#accept_keys").parent().prev().html();
    var id = "#card_" + data.position + " div .pattern-content";
    console.log(id);

    // Dado que la configuración pudo haber cambiado, se elimina el html que está
    // y se rellena con el HTML del modal.
    $(id).empty();
    $(id).append(content);

    // Se eliminan las llaves públicas y privadas.
    $(id + " form div").remove();
    $(id + " form a").remove();

    // Se agrega el input de la llave pública y se llena con ésta
    $(id + " form").append('<div class="form-group">' +
                             '<label for="public_key">Llave pública</label>' +
                             '<input type="text" name="public_key" parsley-trigger="change" required readonly ' +
                                    'placeholder="Espere mientras se inserta la llave pública" class="form-control" ' +
                                    'id="public_key">' +
                           '</div>');
    $(id + " form div #public_key").val(data.captcha.public_key);

    // Se agrega el input de la llave privada y se llena con ésta
    $(id + " form").append('<div class="form-group">' +
                             '<label for="private_key">Llave privada</label>' +
                             '<input type="text" name="private_key" parsley-trigger="change" required readonly ' +
                                    'placeholder="Espere mientras se inserta la llave privada" class="form-control" ' +
                                    'id="private_key">' +
                           '</div>');
    $(id + " form div #private_key").val(data.captcha.private_key);

    // Guardar todo.
    $('#guardar').show();
    var tem_id = $('#template_id').val().toString()
    var link = "/revisar_template/"+ tem_id
    $('#preview').attr('href',link)
    $('#preview-form').attr('action',link)
    $('#frm1_submit').show();
    $('#preview').show();
  });
  // $('#actualizarCaptcha').trigger("click");
});

// Si se elige la opcion de eliminar un patron, se hace
// un request a la aplicacion para eliminar dicho patron
// de la bd
$(document).on('click', "button.eliminar", function(){
  var  id = $(this).parent().parent().attr('id')
  var position = $(this).attr('data-position');
  $.ajax({
      url : "../erase-captcha/",
      data :  {'template': $('#template_id').val(),
               'position': position},

  })
  .done(function(data){
    card = document.getElementById(id);
    card.remove()
    });
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
