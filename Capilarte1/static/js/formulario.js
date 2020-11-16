$(document).ready(function () {

    $("#formulario").submit(function (eventoSubmit) {
      eventoSubmit.preventDefault();
  
      var rut = $("#rut").val();
      var nom = $("#nombre").val();
      var apellidos = $("#apellidos").val();
      var email = $("#email").val();
      var tel = $("#telefono").val();
      var comentarios = $("#comentarios").val();
  
      if (rut == null || rut.trim().length > 10 || rut.trim().length < 9 ) {
        swal("Rut inválido", "", "error");
        $("#rut").focus();
        return false;
      }
  
      if (nom == null || nom.trim().length < 3 ) {
        swal("Nombre inválido", "", "error");
        $("#nom").focus();
        return false;
      }
  
      if ( apellidos == null || apellidos.trim().length < 5 ) {
        swal("Apellido inválido", "", "error");
        $("#apellidos").focus();
        return false;
      }
  
      if (email == null || email.trim().length == 0) {
        swal("Email inválido", "", "error");
        $("#email").focus();
        return false;
      }
  
      if (tel == null || tel.trim().length < 9 || tel.length >= 10 ) {
        swal("Teléfono inválido", "", "error");
        $("#tel").focus();
        return false;
      }
  
      if (comentarios == null || comentarios.length < 5) {
        swal("Comentario inválido", "", "error");
        $("#comentarios").focus();
        return false;
      }


      swal("Formulario enviado correctamente","","success");
    });
  });