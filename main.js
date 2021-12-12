window.zindex = 1;
const duiRegExp = /(^\d{8})-(\d$)/;
const nitRegExp = /((^\d{4})-(\d{6})-(\d{3})-(\d$))|(^\d{14}$)/;
const carPlateRegExp = /^(O|N|CD|CC|P|A|C|V|PR|T|RE|AB|MI|MB|F|M|D|PNC|E)\d{1,6}$/i;
const municipalitiesLookup = { '01': 12, '02': 13, '03': 16, '04': 33, '05': 22, '06': 19, '07': 16, '08': 22, '09': 9, '10': 13, '11': 23, '12': 20, '13': 26, '14': 18,};

$(document).ready(function(e){
    accederPaciente();
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
function accederPaciente() {
    $.get('http://localhost:3008/permitir-entrada-personal', function(data) {
        console.log(data);
        if (data.resp == true) {
                console.log("acceso permitido");
            } else {
                window.location.href = "index.html";
            }
    }, 'json');
}
$('#cerrarSesion').click(function(){
    $.post('http://localhost:3008/cerrar_sesion_personal', JSON.stringify({}), function(data) {
        if (data.resultado == true) {
                window.location.href = "index.html";
            } else {
                console.log("Algo falló al cerrar la sesion");
            }
    }, 'json');
});