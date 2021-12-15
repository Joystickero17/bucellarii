/* esto es para hacer funcionar los modales */
function pass_info(table_row){
    let container = document.getElementById("content-destiny");
    let headers = document.getElementById("headers").children;
    let yes_delete = document.getElementById("yes_delete");
    
    yes_delete.href += 'del/'+table_row.children[0].innerText;
    container.innerText = '';
    console.log(yes_delete.href);

    for (let index = 0; index < table_row.children.length-1; index++) {
        console.log(headers);
        container.innerHTML += "<strong>"+headers[index].innerText +"</strong>:     "+table_row.children[index].innerText +"<br>";
        
    }

}

function redirect(url){
    window.location.replace(url);
}

function reload_page(){
    window.location.reload();
}

let modal = document.getElementById("aviso-borrar");
if (modal){
    modal.addEventListener('hidden.bs.modal', function(event){reload_page()})
}
