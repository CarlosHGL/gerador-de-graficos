document.addEventListener("DOMContentLoaded", function(){
    const receivedData = JSON.parse('{{ data | tojson | safe}}')
    // Aqui você pode manipular os dados recebidos como desejar
    console.log(receivedData); // Exemplo: Mostrar no console do navegador

    // Por exemplo, alterar a cor de um elemento com base nos dados recebidos
    // if (receivedData.success) {
    //     document.getElementById('elemento').style.color = 'green';
    // } else {
    //     document.getElementById('elemento').style.color = 'red';
    // }
})