// Function executed after loading config modal for carousel pattern
function afterLoadCarouselConfigModal() {
  $('.formset_row').formset({
    addText: 'Añadir elemento',
    deleteText: 'Eliminar elemento',
    prefix: 'content_set'
  });

  $('#modal-configuracion .modal-dialog').addClass("modal-lg");

  return;
}

function sendCarouselData() {
  return {
    url: "../../carousel/configurar/",
    data: $('form#carousel-create').serialize(),
  }
}

$(document).on('click', "#accept-carousel", function () {
  var form_options = { 
    target: '#modal-configuracion .modal-dialog', 
    data: {
      "template": $('#template_id').val(),
      "position": $('#new-ask').data('position'),
    },
    success: function(responseText, statusText) {
      console.log(responseText, statusText);
    },
  };
  $('#carousel-create').ajaxForm(form_options);
});
