function index(planta){
    document.cookie = "posicion = " + planta;
    window.location.href = "/sensor/"+planta.toString();
  }