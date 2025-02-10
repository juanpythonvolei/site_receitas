function open_delete_recipe_popup(id, nome) {
  let popup = document.getElementById("popup");
  let mensagem = document.getElementById("label-apagar-lista");
  let input_apagar_receita = document.getElementById("input-apagar_receita");
  popup.style.display = "flex";
  mensagem.innerHTML = `Tem certeza que deseja apagar a receita: ${nome} ?`;
  input_apagar_receita.value = id;
}

function close_delete_recipe_popup() {
  let popup = document.getElementById("popup");
  popup.style.display = "none";
}
