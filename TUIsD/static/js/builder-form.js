$('.pattern.formulario, .pattern.formulario a').click(function(e) {
  $(".builder").append("<div id=card_"+i+" class='card-box card-formulario' data-id='"+i+"'>" +
                         "<div class='btn-group pull-right'>" +
                           "<button type='button' class='btn btn-default waves-effect config'>Configurar</button>" +
                           "<button type='button' class='btn btn-danger waves-effect eliminar'>Eliminar</button>" +
                         "</div>" +
                         "<h1 class='header-title m-b-30'>Formulario</h1>" +
                         "<div class='row'>" +
                           "<div class='col-md-12 pattern-content' style='text-align: center;'>" +
                           "</div>" +
                         "</div>" +
                         "<input type='hidden' name='card_position' value="+i+">" +
                       "</div>");
  i = i + 1;
})

$(document).on('click', '.card-formulario button.config', function(e) {
  editingID = $(this).parents('.card-formulario').data('id');
  $('#new-form-modal').modal('show');
})

$(document).on('click', ".card-formulario button.eliminar", function(){
  id = $(this).parents('.card-formulario').data('id');
  position = $(this).parents('.card-formulario').children('.fb-rendered-form-wrapper').data('position');
  console.log($(this).parents('.card-formulario').children('.fb-rendered-form-wrapper'))
  $.ajax({
      url : "../erase-formulario/",
      data :  {'template': $('#template_id').val(),
                'position': position
              }

  })
  .done(function(data){
    card = document.getElementById(id);
    card.remove()
    });
});

$(document).ready(function() {
  $('.fb-rendered-form').each(function(i,e) {
    json = formsJSON[$(e).parents('.fb-rendered-form-wrapper').data('position')];
    console.log(json);
    $('.pattern.formulario').click();
    $('#card_'+i+' .pattern-content').html(formDataToHTML(json));
  })
})
