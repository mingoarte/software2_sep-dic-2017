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
$(".pattern").on('click', function() {
  
  // Toma el contenedor del constructor y le agrega una nueva caja que representa
  // el nuevo patron escogido. 
  $(".builder").append("<div id=card_"+i+" class='card-box'>" + 
  	                     "<div class='btn-group pull-right'>" + 
                           "<button type='button' class='btn btn-default waves-effect config'>Configurar</button>" + 
  	                       "<button type='button' class='btn btn-danger waves-effect eliminar'>Eliminar</button>" + 
  	                     "</div>" + 
  	                     "<h1 class='header-title m-b-30'>Encuesta</h1>" + 
  	                     "<div class='row'>" + 
  	                       "<div class='col-md-12 pattern-content' style='text-align: center;'>" +
  	                       "</div>" + 
  	                     "</div>" + 
  	                     "<input type='hidden' name='card_position' value="+i+">" + 
  	                   "</div>");
  i = i + 1;
});

// Permite acceder a las configuraciones de la nueva encuesta del template
$(document).on('click', "button.config", function() {
  // Declaracion de variables locales
  // id -> Contiene el id del contenedor del patron de interaccion que
  //       se quiere configurar.
  // content -> El formulario con la configuracion del patron de interaccion
  //            que se quiere configurar
  var  id = $(this).parent().parent().attr('id');
  var content = $("#" + id + " div .pattern-content").html();
  
  // Elimina la configuracion que estaba seteada en el modal de configuracion
  $("#new_ask div div .modal-body form").remove();
  
  // Si el contenido de configuracion del patron de interaccion no esta vacio
  // se agrega al contenido de configuracion del modal.
  if (content != "") {
	  
    // Se agrega el contenido y el boton para agregar nuevas opciones
	  $("#new_ask div div .modal-body").append(content);
	  $("#new_ask div div .modal-body form").append(
              '<button id="add_more" class="btn btn-primary waves-effect waves-light" type="button">' +
                'Agregar otra opcion' +
              '</button>'); 


    // Se setean los nuevos datos de los input 
	  var tmp = $("#" + id + " div .pattern-content form div #pregunta").val();
	  $("#new_ask div div .modal-body form div #pregunta").val(tmp);

	  var tmp2 = [];
	  $("#" + id + " div .pattern-content form div #opcion").each(function(index) {
	  	tmp2.push($(this).val())
	  })

    $("#new_ask div div .modal-body form div #opcion").each(function(index) {
    	$(this).val(tmp2[index]);
    });
  }
  // Si el contenido de configuracion estaba vacio, indica que se necesitaba crear
  // una configuracion nueva, por lo que se crea un nuevo formulario
  else {

	  $("#new_ask div div .modal-body").append(
          '<form data-parsley-validate novalidate>' +
            '<input id="card-id" type="hidden" name="card-id">' +
            '<input id="position" type="hidden" name="position">' +
            '<div class="form-group">' +
              '<label for="pregunta">Pregunta</label>' +
              '<input type="text" name="pregunta" parsley-trigger="change" required ' +
                     'placeholder="Escriba la pregunta de la encuesta" class="form-control" id="pregunta">' +
            '</div>' +
            '<div class="form-group">' +
              '<label for="opcion">Opcion:</label>' +
              '<input type="text" name="opcion" parsley-trigger="change" required ' +
                     'placeholder="Escriba la opcion" class="form-control" id="opcion">' +
            '</div>' +
            '<div class="form-group">' +
              '<label for="opcion">Opcion:</label>' +
              '<input type="text" name="opcion" parsley-trigger="change" required ' +
                     'placeholder="Escriba la opcion" class="form-control" id="opcion">' +
            '</div>' +
            '<div class="form-group text-right m-b-0">' +
              '<button id="add_more" class="btn btn-primary waves-effect waves-light" type="button">' +
                'Agregar otra opcion' +
              '</button>' +
            '</div>' +
          '</form>');
  }

  // Se setean los valores de los input escondidos para la posicion y para el patron al que 
  // pertenece la configuracion actual del form del modal.
  $('#card-id').val(id);
  $('#position').val(id.split("_")[1]);
  
  $('#new_ask').modal('show');
});

// Permite agregar nuevas opciones a la encuesta
$(document).on('click', "button#add_more", function(){
  $('<div class="form-group">' +
      '<label for="opcion">Opcion:</label>' +
      '<input type="text" name="opcion" parsley-trigger="change" required ' +
             'placeholder="Escriba la opcion" class="form-control" id="opcion">' +
      '</div>').insertBefore($(this).parent())
})

// Si se elige la opcion de eliminar un patron, se hace
// un request a la aplicacion para eliminar dicho patron
// de la bd 
$(document).on('click', "button.eliminar", function(){
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
$(document).on('click', "button.accept-encuesta", function() {
  // Declaracion de variables locales
  // opciones -> Lista con las opciones de la encuesta que se quiere crear
  var opciones = [];
  
  $("#new_ask div div .modal-body form div input[name='opcion']").each(function() {
      opciones.push($(this).val());
  });
  var pregunta = $("#new_ask div div .modal-body form div input[name='pregunta']").val()
  console.log(pregunta)
  $.ajax({
    url : "../poll-config/",
    data : {
            'pregunta': pregunta,
            'opciones': opciones,
            'template': $('#template_id').val(),
            'position': $('#position').val(),
           },
   
  })
  .done(function(data){
      // Declaracion de variables locales
      // content -> El contenido extraido del modal de configuracion
      // id -> El identificador del patron de interaccion que se esta
      //       configurando
      var content = $(".accept-encuesta").parent().prev().html();
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

      // Se agrega el input de la pregunta y se llena con la informacion original de la
      // pregunta 
      $(id + " form").append('<div class="form-group">' +
                               '<label for="pregunta">Pregunta</label>' +
                               '<input type="text" name="pregunta" parsley-trigger="change" required ' +
                                      'placeholder="Escriba la pregunta de la encuesta" class="form-control" ' +
                                      'id="pregunta">' +
                             '</div>');
      $(id + " form div #pregunta").val(data.question[0].texto_pregunta);
      
      // Se agregan los inputs de las opciones de la encuesta y se llenam con la informacion
      // original de cada pregunta
      for (j = 0; j < data.options.length; j++) {
        $(id + " form").append('<div class="form-group">' +
                                 '<label for="opcion">Opcion:</label>' +
                                 '<input type="text" name="opcion" parsley-trigger="change" required ' +
                                        'placeholder="Escriba la opcion" class="form-control" id="opcion">' +
                               '</div>');
      }

      $(id + " form div #opcion").each(function(index) {
        $(this).val(data.options[index].texto_opcion);
      })

      $('#guardar').show();
      var tem_id = $('#template_id').val().toString()
      var link = "/revisar_template/"+ tem_id
      $('#preview').attr('href',link) 
      $('#preview-form').attr('action',link) 
      $('#frm1_submit').show();
      $('#preview').show();

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
