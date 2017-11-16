// Se muestra el modal inicial para crear nombre de template
$(document).ready(function() {
  $('#new_template').modal('show');
});


// Una vez se agrega el primer patron al template, se elimina
// el mensaje de bienvenida
$(".pattern").on('click', function() {
  $("#welcome").hide();
});


// Se bloquea el modal del nombre del template para evitar que
// desaparezca al hacer click fuera de el o presionando la te-
// cla ESC. 
$('#new_template').modal({
  backdrop: 'static',
  keyboard: false
});