const API = "https://api-grupos.herokuapp.com/listar_usuarios";

const listarusuarios = async () => {
  const res = await fetch(API);
  const data = await res.json();
  console.log(data);
};

window.addEventListener("load", function () {
  listarusuarios();
});
