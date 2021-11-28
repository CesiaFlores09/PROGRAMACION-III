window.zindex = 1;

$(document).ready(function(e){
    $("#mnxAppClinica a").click(function(event){
        event.preventDefault();

        let modulo = $(this).data("modulo"),
            formulario = $(this).data("formulario");
        abrir_ventana(modulo, formulario);
    });
    
});
function abrir_ventana(modulo, formulario){
    // console.log(`http://localhost:3008/${modulo}/${modulo}_${formulario}.html`);
    $(`#${modulo}_${formulario}`).load(`${modulo}/${modulo}_${formulario}.html`)
        .css("margin-top", "60px")
        .draggable()
        .click(function(e){
            $(this).css("z-index", ++zindex);
        });
}