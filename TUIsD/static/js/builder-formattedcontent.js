// Envia informacion de creacion de patron
function sendFormattedcontentData() {
  // Locales con las opciones que quiero tomar del html del modal
  var title = $('#modal-configuracion input[name="title"]').val()
  var content = $('#modal-configuracion textarea[name="content"]').val()
  
  // Json con los datos y el url al que debe llamar
  return {
    url: "../../formattedcontent/configurar/",
    data: {
		'title' : title,
		'content' : content
    }
  }
}
