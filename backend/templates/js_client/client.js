const contentContainer = document.getElementById('content-container')
const loginForm = document.getElementById('login-form')
const searchForm = document.getElementById('search-form')
const baseEndpoint = "http://localhost:8000/api"
if (loginForm){
    loginForm.addEventListener('submit', handlerLogin)
}

if (searchForm){
    searchForm.addEventListener('submit', handlerSearch)
}
// =========================================================|Login and Retrieve data|=======================================================================
function handlerLogin(event){
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    let bodyStr = JSON.stringify(loginObjectData)

    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: bodyStr
    }
    fetch(loginEndpoint, options)
    .then(response=>{
        return response.json()
    })
    .then(authData=>{
        handleAuthData(authData, getProductList)
    })
    .catch(err=>{
        console.log('Error: ', err)
    })
}

function handleAuthData(authData, callback){
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.refresh)
    if(callback){
        callback()
    }
    
}

function validateJWTToken(){
    const endpoint = `${baseEndpoint}/token/verify/`
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({token: localStorage.getItem('access')})
    }
    fetch(endpoint, options)
    .then(response=>{
        return response.json()
    })
    .then(x=>{
        // refresh token 
    })
}
function writeToContianer(data){
    console.log(data)
    if(contentContainer){
        contentContainer.innerHTML = "<pre>" + JSON.stringify(data, null, 4) + "</pre>"
    }
}

function isTokenValid(jsonData){
    if(jsonData.code && jsonData.code === 'token_not_valid'){
        alert("Invalid Username or Password, Please Login again")
        return false
    }
    return true
}

function getFetchOptions(method, body){
    return {
        method: method === null ? "GET": method,
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem('access')}`
        },
        body: body ? body: null
    }
}
function getProductList(){
    const endpoint = `${baseEndpoint}/product/`
    const options = getFetchOptions()
    fetch(endpoint, options)
    .then(response=>{
        return response.json()
    })
    .then(data=>{
        const vaildData = isTokenValid(data)
        
        if(vaildData){
            writeToContianer(data)
        }
    })
}
validateJWTToken()

// ========================================================================|Searching|===================================================================

function handlerSearch(event){
    event.preventDefault()
    let formData = new FormData(searchForm)
    let data = Object.fromEntries(formData)
    let searchParams = new URLSearchParams(data)
    const endpoint = `${baseEndpoint}/search/?${searchParams}`
    const headers = {
        "Content-Type": "application/json",
    }
    const authToken = localStorage.getItem('access')
    if(authToken){
        headers['Authorization'] = `Bearer ${authToken}`
    }
    const options = {
        method: "GET",
        headers: headers 
    }
    fetch(endpoint, options)
    .then(response=>{
        return response.json()
    })
    .then(data=>{
        const vaildData = isTokenValid(data)
        if(vaildData && contentContainer){
            contentContainer.innerHTML = ""
            if(data && data.hits){
                let htmlStr = ""
                for(let result of data.hits){
                    htmlStr += "<li>" +
                        "Title: "+result.title + '<br>'+
                        "Price: "+result.price + '<br>'+
                        "Body: "+result.body +
                    "</li>" + "<br>"
                }
                contentContainer.innerHTML = htmlStr
                if(data.hits.length===0){
                    contentContainer.innerHTML = "<p> No results found </p>"
                }
            }
            else{
                contentContainer.innerHTML = "<p> No results found </p>"
            }
        }
    })
    .catch(err=>{
        console.log('Error: ', err)
    })
}

// ==================================================================|Algolia Search|============================================================

const searchClient = algoliasearch('CR3YO17ED9', 'd134b8802e2962367012655197a51b02');
const search = instantsearch({
  indexName: 'rab_Product',
  searchClient,
});

search.addWidgets([
  instantsearch.widgets.searchBox({
    container: '#searchbox',
  }),

  instantsearch.widgets.clearRefinements({
    container: "#clear-refinements",
    
  }),

  instantsearch.widgets.refinementList({
    container: "#public-list",
    attribute: 'public'
  }),

  instantsearch.widgets.refinementList({
    container: "#user-list",
    attribute: 'user'
  }),

  instantsearch.widgets.hits({
    container: '#hits',
    templates: {
        item: `<div>
            <div>{{#helpers.highlight}} {"attribute": "title"} {{/helpers.highlight}}</div>
            <div>{{#helpers.highlight}} {"attribute": "body"} {{/helpers.highlight}}</div>
            <p>
                Price: {{price}}<br>
                User: {{user}}
            </p>
        </div>`
    }
  })
]);

search.start();

