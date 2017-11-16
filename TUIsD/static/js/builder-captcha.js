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
      '<h4>Anote ambas claves y recuerde mantener su llave privada en un lugar secreto!</h4>' +
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
});

// Permite acceder a la configuración del captcha y generar nuevas llaves.
$(document).on('click', "button.config-captcha", function() {
  // Declaracion de variables locales
  // id -> Contiene el id del contenedor (card) del captcha.
  // content -> El formulario con la configuracion del patron de interaccion
  //            que se quiere configurar
  var id = $(this).parent().parent().attr('id');
  var content = $("#" + id + " div .pattern-content").html();
  var position = $(this).attr('data-position');

  // Elimina la configuracion que estaba seteada en el modal de configuracion.
  // Esto para actualizar el modal con la última configuración, es decir,
  // la que se encuentra en el card.
  $("#captcha_keys div div .modal-body form").remove();

  // Decidir qué hacer si el card tiene contenido (el captcha está configurado)
  // o no.
  if (content != "") {
    // Configuración existente.
    // Se agrega el contenido y el boton para agregar nuevas opciones
	  $("#captcha_keys div div .modal-body").append(content);
  }
  else{
    // Si no hay contenido anteriormente, debe crearse un captcha nuevo.
    // Primero hay que introducir los campos que él debe llenar.

    $("#captcha_keys div div .modal-body").append(
      '<form data-parsley-validate novalidate>' +
        '<h4>Anote ambas claves y recuerde mantener su llave privada en un lugar secreto!</h4>' +
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
  }

  // Independientemente del contenido, se vuelve a hacer una llamada para generar
  // nuevas llaves.
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

  // Se setean los valores de los input escondidos para la posicion y para el patron al que
  // pertenece la configuracion actual del form del modal.
  $('#captcha_keys div div .modal-body form #card-id').val(id);
  $('#captcha_keys div div .modal-body form #position').val(id.split("_")[1]);
  $('#captcha_keys').modal('show');
});

// Esta es la función que toma la configuración del Captcha hecha en el modal
// y que se envía al servidor para que lo guarde en la BD.
$('#accept_keys').click( function saveCaptchaToTemplate() {
  var private_key = $("#captcha_keys div div .modal-body form div input[name='private_key']").val()
  var public_key = $("#captcha_keys div div .modal-body form div input[name='public_key']").val()
  var position = $("#captcha_keys div div .modal-body form input[name='position']").val()

  console.log("posicion" + position)
  $.ajax({
    method: 'POST',
    url : "../captcha-config/",
    data : {
            'public_key': public_key,
            'private_key': private_key,
            'template': $('#template_id').val(),
            'position': position,
           },
  })
  .done(function(data){
    // Cuando se regrese del AJAX qué se hará.
    // Declaracion de variables locales
    // content -> El contenido extraido del modal de configuracion
    // id -> El identificador del patron de interaccion que se esta
    //       configurando
    // console.log(data)
    if (data.nuevo_patron == true){
      // Toma el contenedor del constructor y le agrega una nueva caja que representa
      // el nuevo patron escogido. Esto significa que se está creando el card
      // donde se mostará la configuración del patrón.
      $(".builder").append(
        "<div id=card_"+data.position+" class='card-box'>" +
          "<div class='btn-group pull-right'>" +
           "<button data-position="+data.position+" type='button' class='btn btn-default waves-effect config-captcha'>Configurar</button>" +
           "<button data-position="+data.position+" type='button' class='btn btn-danger waves-effect eliminar-captcha'>Eliminar</button>" +
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
    // console.log(id);

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
});

// Si se elige la opcion de eliminar un patron, se hace
// un request a la aplicacion para eliminar dicho patron
// de la bd
$(document).on('click', "button.eliminar-captcha", function(){
  var  id = $(this).parent().parent().attr('id')
  var position = $(this).attr('data-position');

  // console.log("Hola")
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
  // console.log(url);
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
