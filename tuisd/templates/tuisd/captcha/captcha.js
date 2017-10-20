$("document").ready(function(){
  $("#actualizarCaptcha").trigger("click");
});

$( "#reproducirAudio" ).click(function(){
  var captchaAudio = document.getElementById('audioCaptcha');
  captchaAudio.play();
});


$( "#actualizarCaptcha" ).click(function() {
  $.ajax({
    url: '/servecaptcha/generate_captcha/{{public_key}}/',
    type: 'get',
    dataType: 'json',
    success: function(data) {
      $("#image_captcha").attr("src", "/servecaptcha/image/" + data.captcha_id);
    },
    failure: function(data) {
      alert("nada");
    }
  });
});
