function sendAccordionData() {
    var form = $('#accordion-create-form').serializeArray();

    return {
        url: '../accordion-config/',
        data: {
            'form': JSON.stringify(form),
            'dataType': 'json',
        }
    }
}

function afterLoadAccordionConfigModal() {
    console.log("afterload");    
}
