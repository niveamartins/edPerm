//colocar opção de fechar ao clicar em qualquer local na tela
function showHelp() {
    let elem = document.getElementById("help");
    if (elem.style.display === "none") {
        elem.style.display = "block";
    } else {
        elem.style.display = "none";
    }
}
