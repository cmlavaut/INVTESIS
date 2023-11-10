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
  window.location.href = "/inicio";
}
