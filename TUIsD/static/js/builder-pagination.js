// Envia informacion de creacion de patron
function sendPaginationData() {
  console.log("pagination data");
  // Locales con las opciones que quiero tomar del html del modal
  var title = $('#modal-configuracion input[name="title"]').val();
  var nItemsOnPage = $('#modal-configuracion input[name="nItemsOnPage"]').val();
  var content = $('#modal-configuracion select[name="content"]').val();
  
  // Json con los datos y el url al que debe llamar
  return {
    url: "../../pagination/configurar/",
    data: {
		'title' : title,
		'nItemsOnPage' : nItemsOnPage,
		'content' : content
    }
  }
}
