console.log("cau")

for(i=0; i <6; i++){
    console.log(i)
}
for(i=0; i <6; i++){
    console.log(i + ". hi")
}

const btn = document.querySelector("#btn")
const btn2 = document.querySelector("#btn2")
let nadpis = document.querySelector(".nadpis")
const body = document.querySelector("body")

btn.addEventListener("click", function(){
    nadpis.style.color = "pink"
    nadpis.style.fontSize = "100px"

})
btn2.addEventListener("click", function(){
    body.classList.toggle("bg-blue")
})