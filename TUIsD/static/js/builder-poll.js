// Permite agregar nuevas opciones a la encuesta
$(document).on('click', "button#add-option", function(e){
  e.preventDefault();
  $('<div class="form-group">' +
      '<label for="opcion">Opcion:</label>' +
      '<input type="text" name="opcion" parsley-trigger="change" required ' +
             'placeholder="Escriba la opcion" class="form-control" id="opcion">' +
      '</div>').insertBefore($(this).parent())
})

function afterLoadPollConfigModal() {
  // Agregar dos opciones por defecto al cargar el modal
  $('#add-option').click();
  $('#add-option').click();
}