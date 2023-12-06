// document.addEventListener("DOMContentLoaded", function() {
//     document.getElementById('loginForm').addEventListener('submit', function(event) {
//         event.preventDefault() // Impede o envio padrão do formulário
        
//         var username = document.getElementsByName('Email').value
//         var password = document.getElementByName('Senha').value
        
//         var errorParagraph = document.getElementById('error');
//         if (errorParagraph) {
//             errorParagraph.parentNode.removeChild(errorParagraph);
//         }
        
//         // Requisição AJAX para enviar os dados do formulário para a rota do Flask
//         var xhr = new XMLHttpRequest()
//         xhr.open('POST', '/login', true)
//         xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
//         xhr.onreadystatechange = function() {
//             if (xhr.readyState === XMLHttpRequest.DONE) {
//                 var response = JSON.parse(xhr.responseText)
//                 if (response.success) {
//                     // Autenticação bem-sucedida, redireciona para a página inicial ou outra ação desejada
//                     window.location.replace('/profile/dashboard')
//                 } else {
//                     // Credenciais inválidas, exibe a mensagem de erro no formulário
//                     var form = document.getElementById('loginForm');
//                     var errorMessage = document.createElement('p');
//                     errorMessage.innerText = response.error;
//                     errorMessage.style.color = 'red';
//                     form.insertBefore(errorMessage, form.firstChild);
//                 }
//             }
//         }
//         xhr.send('username=' + encodeURIComponent(username) + '&password=' + encodeURIComponent(password))
//     })
// })