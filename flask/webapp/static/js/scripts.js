var humedadSelecc = document.getElementById("numeroHum");
var tiempoSelecc = document.getElementById("tiempo");

function enviarDatos(){
  var datosActual = humedadSelecc.value.toString() + "," + tiempoSelecc.value.toString();
  console.log(datosActual);
  $.get("/enviarData/" + datosActual);
  alert("Datos enviados");
}


function historial(){
  window.location.href = "/historial";
}
function regresar(){
  //var id = document.cookie tengo que leer una cookie que es el id del usuario para volver a regresar  
  window.location.href = "/inicio/";
}
