// Se muestra el modal inicial para crear nombre de template
$(document).ready(function() {
  $('#new_template').modal('show');
});

// Una vez se agrega el primer patron al template, se elimina
// el mensaje de bienvenida
$(".pattern, .pattern-carousel, .pattern-accordion").on('click', function() {
  $("#welcome").hide();
});
