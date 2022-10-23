// ------ alertas de exitos e de error -----------

const datosUrl = window.location.search;

if (datosUrl == '?aprovado'){
    alert("La solicitud fue completada exitosamente")
}

if (datosUrl == "?desaprovado"){
    alert("Lo sentimos ocurrio un error, intentelo nuevamente")
} 

// ------- Animacion Observe ---------

const $misionHome = document.querySelectorAll("blockquote.Mision-home")

const efectoObserber = (entrada, observer) => {

    entrada.forEach((element) => {

        if(element.isIntersecting){
         console.log(element.target)   
            element.target.classList.add("Observer-subir")
        }
    })
}


const observador = new IntersectionObserver(efectoObserber, {

    "root":null,
    "rootMargin": "0%",
    "threshold": .5
})

$misionHome.forEach(element => {
    observador.observe(element)
});








//------ Mostrar solamente las publicaciones que se seleccionan en el select -------- 

const categoriaBlog = document.getElementById("Select-blog")

categoriaBlog.addEventListener("change", x =>{
    document.location.href = categoriaBlog.value
})





