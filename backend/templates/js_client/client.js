const loginForm = document.getElementById('login-form')
const baseEndpoint = "http://localhost:8000/api"
if (loginForm){
    loginForm.addEventListener('submit', handlerLogin)
}

function handlerLogin(event){
    console.log(event)
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
        // console.log(response)
        return response.json()
    })
    .then(x=>{
        console.log(x)
    })
    .catch(err=>{
        console.log('Error: ',err)
    })

}
