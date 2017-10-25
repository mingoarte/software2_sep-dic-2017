// Declaracion de variables globales
// i -> Lleva la cuenta de los patrones de interaccion creados en el template para
//      crear los id's de los contenedores de los mismos. 
var i = 0

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
	  $("#new_ask div div .modal-body form").append('<a id="add_more" style="margin-top: 10px;" ' + 
                                                     'class="btn btn-primary btn-sm" >' + 
                                                    '+ Opción' + 
                                                  '</a>');


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

	  $("#new_ask div div .modal-body").append('<form>' +
  	    '<input id="card-id" type="hidden" name="card-id">' +
  	    '<input id="position" type="hidden" name="position">' +
  	    '<input id="created" type="hidden" name="created">' +
  	    '<div class="input-group">' +
  	      '<span class="input-group-addon tags-unete" id=" basic-addon1"><b>Pregunta:</b></span>' +
  	      '<input id="pregunta" type="text" name="pregunta">' +
  	    '</div>' +
  	    '<div class="input-group">' +
  	      '<span class="input-group-addon tags-unete" id=" basic-addon1"><b>Opción:</b></span>' +
  	      '<input class=" tags-unete" id="opcion" type="text" name="opcion">' +
  	    '</div>' +
  	    '<div class="input-group">' +
  	      '<span class="input-group-addon tags-unete" id=" basic-addon1"><b>Opción:</b></span>' +
  	      '<input id="opcion" type="text" name="opcion">' +
  	    '</div>' +
  	    '<a style="margin-top: 10px;" class="btn btn-primary btn-sm" id="add_more">+ Opción</a>' +
  	'</form>');
  }

  // Se setean los valores de los input escondidos para la posicion y para el patron al que 
  // pertenece la configuracion actual del form del modal.
  $('#card-id').val(id);
  $('#position').val(id.split("_")[1]);
  
  $('#new_ask').modal('show');
});


// Permite agregar nuevas opciones a la encuesta
$(document).on('click', "a#add_more", function(){
  $("<div class='input-group'>" + 
  	  "<span class='input-group-addon tags-unete' basic-addon1'>" + 
  	    "<b>Opción:</b>" + 
  	  "</span>" +
  	  "<input id='opcion' type='text' name='opcion'>" +
  	"</div>").insertBefore(this)
})

function flush_poll_modal() {
	$("#accept_encuesta").parent().prev().empty();
	$("#accept_encuesta").parent().prev().append('<form>' +
																							    '<input id="card-id" type="hidden" name="card-id">' + 
																							    '<input id="position" type="hidden" name="position">' +
																							    '<div class="input-group">' +
																							      '<span class="input-group-addon tags-unete" id=" basic-addon1"><b>Pregunta:</b></span>' +
																							      '<input id="pregunta" type="text" name="pregunta">' +
																							    '</div>' +
																							    '<div class="input-group">' +
																							      '<span class="input-group-addon tags-unete" id=" basic-addon1"><b>Opción:</b></span>' +
																							      '<input class=" tags-unete" id="opcion" type="text" name="opcion">' +
																							    '</div>' +
																							    '<div class="input-group">' +
																							      '<span class="input-group-addon tags-unete" id=" basic-addon1"><b>Opción:</b></span>' +
																							      '<input id="opcion" type="text" name="opcion">' +
																							    '</div>' +
																							    '<a style="margin-top: 10px;" class="btn btn-primary btn-sm" id="add_more">+ Opción</a>' +
																						   '</form>');
}
