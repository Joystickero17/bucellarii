/* var document.getElementById("id_excento");

addEventListener('click', event =>{
    let iva = document.getElementById("id_iva");
    if(event.target.checked){
        iva.options[0].selected = true;
        iva.disabled = true;
    }else{
        iva.disabled = false;
        iva.options[0].selected = false;
        
    }
} ) */
function searchItemsByContent(text_value, explore_list){
    /* console.log(text_value); */
    for (let i=0;i<explore_list.length; i++){
        if(text_value===explore_list[i].value){
            return i;
        }
    }

}
function addToList(event){
    // Selecciona un elemento del mutliselect en hidden para que django lo tenga en cuenta al enviar por post
    let pk_list = document.querySelectorAll("#lista1>.card>.row>.col-md-8>.card-body>#pk_productos");
    console.log(pk_list);
    for (let i=0;i<pk_list.length; i++){
        /* let index = searchItemsByContent(pk_list[i].textContent, multiple_products.options); */
        /* multiple_products.options[index].selected = true; */
    }

}


function removeFromList(event){
    // Deselecciona un elemento del mmutliselect en hidden para que django lo tenga en cuenta al enviar por post
    console.log(event);
    /* let index = searchItemsByContent(event.item.querySelector("#pk_productos").textContent, multiple_products.options); */
    /* multiple_products.options[index].selected = false; */
}

const lista1 = document.getElementById("lista1");
const lista2 = document.getElementById("lista2");
const multiple_products = document.getElementById("id_productos");


if (lista1){
    var sortable = Sortable.create(lista1,{group:"shared", onAdd:addToList, onRemove:removeFromList});
    var sortable_2 = Sortable.create(lista2, {group:"shared"});
    lista1.addEventListener("onAdd",(event)=>{console.log(event)})
}

