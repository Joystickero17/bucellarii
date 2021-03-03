const HOST = 'http://127.0.0.1:8000/'
const STATICROOT = 'media/'

/* 
en este archivo se guardan las clases para construir listas a partir de las llamadas 
asincronas, y un elemento del html

clase ListView
 */



class ListView {
    constructor(htmlId, urlAsyncGet, meta = { onChangeElement: "", loaderElement: "" }) {
        this.documentElement = document.getElementById(htmlId);
        this.urlAsyncGet = urlAsyncGet;
        this.onChangeElement = document.getElementById(meta.onChangeElement);
        this.loaderElement = document.getElementById(meta.loaderElement);

        if (this.onChangeElement) {
            this.onChangeElement.addEventListener("input", (e) => { this.buildList(e.target.value) })
        }

        if (!this.loaderElement) {
            // obligatoriamente se debe definir un elemento loader para la espera de las consultas asíncronas
            throw "Must Define LoaderElement, in meta object of init";
        }

        if (this.documentElement) {

            this.buildList();
        }


    }

    loading(){
        
        this.loaderElement.style.visibility = "visible";
    }

    loaded(){
        this.loaderElement.style.visibility = "hidden";
    }

    htmlSingleElement(data) {
        //pass
    }

    clearList() {
        this.documentElement.innerHTML = "";
    }

    buildList(keyword) {
        this.clearList();
        this.loading();
        if (keyword) {
            fetch(HOST + this.urlAsyncGet + "?keyword=" + keyword)
                .then(data => {
                    
                    return data.json()
                }

                ).then((item) => {
                    this.loaded();
                    this.fillList(item["object_list"]);
                })
        } else {
            fetch(HOST + this.urlAsyncGet)
                .then(data => {
                    
                    return data.json()
                }

                ).then((item) => {
                    this.loaded();
                    this.fillList(item["object_list"]);
                })
        }

    }

    fillList(data) {
        console.log(data);
        data.map((element) => {
            this.documentElement.insertAdjacentHTML("beforeend", this.htmlSingleElement(element));
        })
    }
}

class ProductListView extends ListView {
    htmlSingleElement(data) {
        var htmlText = `
    <div class="card mb-3 card-size-fix" >
    <div class="row d-flex flex-nowrap">
      <div class="col-4">
        <img src="${HOST}${STATICROOT}${data["img"]}" class="img-product-search" alt="...">
      </div>
      <div class="col-8">
        <div class="card-body">
          <h5 class="card-title responsive-text">${data.name} </h5>
          <p class="card-text responsive-text">${data.price} $</p>
          <button class="btn btn-success d-block"><i class="fas fa-plus-circle"></i></button>
        </div>
      </div>
      
    </div>
  </div>`
        return htmlText
    }
}

class ClientesListView extends ListView {
    htmlSingleElement(data) {
        var htmlText = `<div class="card border-dark mx-3 mb-3" style="max-width: 18rem;">
              <div class="card-header">${data.name} ${data.last_name}</div>
              <div class="card-body text-dark">
            
            <p class="card-text">identidad: ${data.cedula}</p>
          </div>
  `
        return htmlText
    }
}


document.addEventListener("DOMContentLoaded", () => {
    const productos = new ProductListView("product-list-results", "async/products", { onChangeElement: "products-search", loaderElement:"products-loader" });
    const clientes = new ClientesListView("client-list-results", 'async/clients', { onChangeElement: "clients-search", loaderElement: "clients-loader" });

})

/*var client_list = document.getElementById("client-list-results"); */