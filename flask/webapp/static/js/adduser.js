var id_add = document.getElementById("iduser"); //traigo la variable de html
var name_add = document.getElementById("idname");
var email_add = document.getElementById("idemail");
var userdb_add = document.getElementById("iduserdb");
var passw_add = document.getElementById("idpassw");



function agregar(){
  lista= [id_add.value.toString(), name_add.value.toString(), email_add.value.toString(), userdb_add.value.toString(), passw_add.value.toString()]
  console.log(lista)
  window.location.href = "/useragregado/" + lista;
  alert("Cliente agregado exitosamente");
}