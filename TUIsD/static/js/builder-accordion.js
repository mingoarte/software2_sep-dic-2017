function sendAccordionData() {
    var form = $('#accordion-create-form').serialize();

    return {
        url: '../accordion-config/',
        data: {
            'form': form,
        }
    }
}

function afterLoadAccordionConfigModal() {
    //console.log("HUEHUEHUE");
}

$('.delete-panel-button').click(function (e) {

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

$('.edit-panel-button').click(function (e) {
    alert()
});
