function sendAccordionData() {
    var form = $('#accordion-create-form').serialize();

    return {
        url: '../accordion-config/',
        data: {
            'form': form,
            'dataType': 'json',
        }
    }
}

function afterLoadAccordionConfigModal() {
    console.log("afterload");
}

$(document).on('click', "a.delete-panel-button",function (e) {

    var $this = $(this);
    var acordeon_id = $this.data('accordion-id')
    var eliminar_hijo = confirm("¿Eliminar este acordeon?");

    if(eliminar_hijo) {
        $.get({
            url: '/acordeon/eliminar/' + acordeon_id,
            success: function (res) {
                $this.closest(".panel").remove()
            }
        })
    }
});

$(document).on('click', "a.edit-panel-button",function (e) {

    var $this = $(this);
    var acordeon_id = $this.data('accordion-id')
    var $modal = $('#modal-configuracion');
    var $modal_dialog = $modal.find('.modal-dialog');

    $modal.data('accordion-id', acordeon_id);

    // Limpiar modal
    $modal_dialog.html('');
    $modal_dialog.removeClass("modal-lg");
    $.get({
        url: '/acordeon/get-modal-editar-panel',
        data: {
          "acordeon-id": acordeon_id
        },
        success: function (res) {
          $modal_dialog.html(res.html);
          $modal.modal('show');
        },
        error:function (res) {
            console.log(res.responseText)
        }
    })
});


$(document).on('click', "button#panel-edit-submit",function (e) {
    e.preventDefault();

    var $modal = $('#modal-configuracion');
    var $form = $modal.find('#panel-edit-form');

    var acordeon_id = $modal.data('accordion-id');

    if(!acordeon_id) return;

    var data = $form.serializeArray().reduce(function(obj, item) {
        obj[item.name] = item.value;
        return obj;
    }, {});

    $.get({
        url: '/acordeon/editar/'+acordeon_id,
        data: data,
        success: function (res) {
            $modal.modal('hide');
            // TODO: Falta mostrar a "tiempo real" el cambio
        },
        error:function (res) {
            console.log(res.responseText)
        }
    })

});
