$(".pattern-accordion").on('click', function() {
  var htmlString = "<div id=card_" + i + " class='card-box'>" + 
    "<div class='btn-group pull-right'>" + 
    "<button type='button' class='btn btn-default waves-effect' data-toggle='modal' data-target='#modal-accordion'>Configurar</button>" +
    //"<button type='button' class='btn btn-default waves-effect config-accordion'>Configurar</button>" + 
    "<button type='button' class='btn btn-danger waves-effect eliminar-accordion'>Eliminar</button>" + 
    "</div>" + 
    "<h1 class='header-title m-b-30'>Carrusel</h1>" + 
    "<div class='row'>" + 
    "<div class='col-md-12 pattern-content' style='text-align: center;'>" +
    "</div>" + 
    "</div>" + 
    "<input type='hidden' name='card_position' value=" + i + ">" + 
    "</div>"

  $(".builder").append(htmlString);

  i++;
});
