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

function getCookie(cookieName) {
    var cookies = document.cookie.split(';');

    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();

      if (cookie.indexOf(cookieName + '=') === 0) {
            // Devuelve el valor de la cookie
            return cookie.substring(cookieName.length + 1);
      }
    }

    // Devuelve null si la cookie no se encuentra
    return null;
}

function regresar(){
  var id = getCookie('usuario')
  if (id){
    console.log("valor" + id);
  } else {
    console.log("no hay cookie con ese nombre")
  } 

  window.location.href = "/inicio/"+ id.toString();
}
