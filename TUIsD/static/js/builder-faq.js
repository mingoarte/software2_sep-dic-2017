$(".pattern-formulario").on('click', function() {
  // Elimina la configuracion que estaba seteada en el modal de configuracion
  $("#new_faq div div .modal-body form").remove();

  $("#new_faq div div .modal-body").append(
          '<form data-parsley-validate novalidate>' +
            '<input id="card-id" type="hidden" name="card-id">' +
            '<input id="position" type="hidden" name="position">' +
            '<div class="form-group">' +
              '<label for="categoria">Categoria</label>' +
              '<input type="text" name="categoria" parsley-trigger="change" required placeholder="Escriba el tema de las preguntas.(Opcional)" class="form-control" id="categoria">'+
            '</div>' +
            '<div class="form-group">' +
              '<label for="pregunta">Pregunta:</label>' +
              '<input type="text" name="pregunta" parsley-trigger="change" required placeholder="Escriba la pregunta " class="form-control" id="pregunta">'+
            '</div>' +
            '<div class="form-group">' +
              '<label for="respuesta">Respuesta:</label>' +
              '<textarea type="text" name="respuesta" parsley-trigger="change" required placeholder="Escriba la respuesta " class="form-control" id="respuesta"></textarea> '+
            '</div>' +
            '<div class="form-group text-right m-b-0">' +
              '<button id="add_more_faqs" class="btn btn-primary waves-effect waves-light" type="button">' +
                'Agregar otra opcion' +
              '</button>' +
            '</div>' +
          '</form>');

  $('#new_faq').modal('show');
  
});

$(document).on('click', "button#add_more_faqs", function(){
  $('<div class="form-group">' +
      '<label for="pregunta">Pregunta:</label>' +
      '<input type="text" name="pregunta" parsley-trigger="change" required placeholder="Escriba la pregunta " class="form-control" id="pregunta">'+
    '</div>' +
    '<div class="form-group">' +
      '<label for="respuesta">Respuesta:</label>' +
      '<textarea type="text" name="respuesta" parsley-trigger="change" required placeholder="Escriba la respuesta " class="form-control" id="respuesta"></textarea> '+
    '</div>').insertBefore($(this).parent())
})


// Permite enviar request a la app para guardar en bd el nuevo patron que se creara
$('#accept_formulario').click(function(){
  // Declaracion de variables locales
  // opciones -> Lista con las opciones de la encuesta que se quiere crear
  var preguntas = [];
  var respuestas = [];

  $("#new_faq div div .modal-body form div input[name='pregunta']").each(function() {
      preguntas.push($(this).val());
  });

  $("#new_faq div div .modal-body form div textarea").each(function() {
    respuestas.push($(this).val());
  });
  var categoria = $("#new_faq div div .modal-body form div input[name='categoria']").val()

  $.ajax({
    url : "../faq-config/",
    data : {
            'categoria': categoria,
            'preguntas': preguntas,
            'respuestas': respuestas,
            'template': $('#template_id').val(),
            'position': $('#position').val(),
           },

  })
  .done(function(data){
      // Declaracion de variables locales
      // content -> El contenido extraido del modal de configuracion
      // id -> El identificador del patron de interaccion que se esta
      //       configurando
      console.log(data)
      if (data.position != null){
        // Toma el contenedor del constructor y le agrega una nueva caja que representa
        // el nuevo patron escogido. 
        $(".builder").append(
          "<div id=card_"+data.position+" class='card-box'>" + 
            "<div class='btn-group pull-right'>" + 
             "<button data-position="+data.position+" type='button' class='btn btn-default waves-effect config_faq'>Configurar</button>" + 
             "<button data-position="+data.position+" type='button' class='btn btn-danger waves-effect eliminar_faq'>Eliminar</button>" + 
            "</div>" + 
            "<h1 class='header-title m-b-30'>Formulario</h1>" + 
            "<div class='row'>" + 
             "<div class='col-md-12 pattern-content' style='text-align: left;'>" +
             "</div>" + 
            "</div>" + 
            "<input type='hidden' name='card_position' value="+data.position+">" + 
          "</div>");
      }else{

      }
      var content = $("#accept_formulario").parent().prev().html();
      var id = "#card_" + data.position + " div .pattern-content";
      console.log(id);

      // Se vacia el contenedor del patron de interaccion y se rellena
      // con la informacion del formulario del modal
      $(id).empty();
      $(id).append(content);

      // Se eliminan las opciones y las preguntas, asi como el boton del contenido
      // del patron de interaccion
      $(id + " form div").remove();
      $(id + " form a").remove();

      // Se agrega el input de la pregunta y se llena con la informacion original de la
      // pregunta
      $(id + " form").append('<div class="form-group">' +
                               '<label for="categoria">Categoria</label>' +
                               '<input type="text" name="categoria" parsley-trigger="change" required ' +
                                      'placeholder="Escriba la pregunta" class="form-control" ' +
                                      'id="categoria" readonly>' +
                             '</div>');
      $(id + " form div #categoria").val(data.questions.tema);


      // Se agregan los inputs de las opciones de la encuesta y se llenam con la informacion
      // original de cada pregunta
      for (j = 0; j < data.questions.length; j++) {
        $(id + " form").append('<div class="form-group">' +
                                '<label for="pregunta">Pregunta:</label>' +
                                '<input type="text" name="pregunta" parsley-trigger="change" required placeholder="Escriba la pregunta " class="form-control" id="pregunta">'+
                              '</div>' +
                              '<div class="form-group">' +
                                '<label for="respuesta">Respuesta:</label>' +
                                '<textarea type="text" name="respuesta" parsley-trigger="change" required placeholder="Escriba la respuesta " class="form-control" id="respuesta"></textarea> '+
                              '</div>');
                                      }

      $(id + " form div #pregunta").each(function(index) {
        $(this).val(data.questions[index].pregunta);
      })

      $(id + " form div #respuesta").each(function(index) {
        $(this).val(data.questions[index].respuesta);
      })
      $('#guardar').show();
      var tem_id = $('#template_id').val().toString()
      var link = "/revisar_template/"+ tem_id
      $('#preview').attr('href',link)
      $('#preview-form').attr('action',link)
      $('#frm1_submit').show();
      $('#preview').show();

  });
})