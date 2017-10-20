var i = 0
$(".pattern").on('click', function() {
  $(".builder").append("<div id=card_"+i+" class='card-box'>" + 
  	                     "<div class='btn-group pull-right'>" + 
  	                       "<button type='button' class='btn btn-default waves-effect config'>Configurar</button>" + 
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

  var  id = $(this).parent().parent().attr('id');
  var content = $("#" + id + " div .pattern-content").html();
  // console.log(content == "");
  if (content != "") {
	  
	  $("#new_ask div div .modal-body form").remove();
	  $("#new_ask div div .modal-body").append(content);
	  $("#new_ask div div .modal-body").append('<a style="margin-top: 10px;" class="btn btn-primary btn-sm" id="add_more">+ Opción</a>');



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
