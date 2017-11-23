//Inicia ventana de configuración
$(".pattern-carousel").on('click', function() {
    var modal = $('#modal-carousel');
    modal.modal('show');
    
    $.ajax({
        url: $(this).attr("data-action"),
        data: {
          'template': $('#template_id').val(),
          'position': ""
        }
    }).done(function(response) {
        modal.html(response);
    });
});

$(document).on('click', "button#eliminarCarousel", function() {
  var position = $(this).attr('data-position');
  var carousel_id = $(this).parent().parent().find("input[name='idCarousel']").val();
  var id = $(this).parent().parent().attr('id')

  $.ajax({
      url : $(this).attr('data-action'),
      data :  {
        'template': $('#template_id').val(),
        'position': position
      },
  })
  .done(function(data) {
    card = document.getElementById(id);
    card.remove()
  });
});

$(document).on('click', "button#modificarCarousel", function() {
  var position = $(this).attr('data-position');
  var carousel_id = $(this).parent().parent().find("input[name='idCarousel']").val();
  var modal = $('#modal-carousel');
  
  $.ajax({
    url: $(this).attr('data-action') + carousel_id,
    data: {
      'template': $('#template_id').val(),
      'position': position
    }
  }).done(function(res) {
    modal.modal('show');
    modal.html(res);
  });

  $('#card-id').val(position);
  $('#position').val(position);
});