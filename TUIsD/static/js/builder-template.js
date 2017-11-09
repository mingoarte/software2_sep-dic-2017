// VARIABLE GLOBAL: ID del componente que se esta editando en el momento
var editingID = null;


// Se muestra el modal inicial para crear nombre de template
$(document).ready(function() {
  $('#new_template').modal('show');
});


// Una vez se agrega el primer patron al template, se elimina
// el mensaje de bienvenida
$(".pattern").on('click', function() {
  $("#welcome").hide();
});

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
