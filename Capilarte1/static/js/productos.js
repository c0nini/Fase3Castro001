$(document).ready(function () {

  var compras = 0;

  function TotalAPagar(precio, cantidad) {
    return precio * cantidad;
  }

  function SumarProductos(cantidad){
    compras = compras + parseInt(cantidad);
    $("#compras").text(compras);
  }

  $(".comprar").click(function (eventoOnclick) {
    swal("Ingrese la cantidad", {
      content: "input",
    }).then((cantidad) => {
      if (cantidad > 0) {
        var precio = 5000;
        SumarProductos(cantidad);
        swal(`El total a pagar es: $${TotalAPagar(precio, cantidad)}`);
      } else {
        swal("Error", "Debe ingresar una cantidad mayor a 0", "error");
      }
    });
  });

  $("#botoncomprar").click(function (eventoOnclick) {
    swal("Ingrese la cantidad", {
      content: "input",
    }).then((cantidad) => {
      if (cantidad > 0) {
        var precio = 2500;
        SumarProductos(cantidad);
        swal(`El total a pagar es: $${TotalAPagar(precio, cantidad)}`);
      } else {
        swal("Error", "Debe ingresar una cantidad mayor a 0", "error");
      }
    });
  });
  
});
