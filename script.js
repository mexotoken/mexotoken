document.addEventListener("DOMContentLoaded", () => {

const menuToggle = document.getElementById("menu-toggle");
const mobileMenu = document.getElementById("mobile-menu");

if(menuToggle){

menuToggle.addEventListener("click",()=>{

mobileMenu.classList.toggle("active");

});

}

const copyBtn = document.getElementById("copy-btn");
const contract = document.getElementById("contract");

if(copyBtn){

copyBtn.addEventListener("click",()=>{

navigator.clipboard.writeText(contract.innerText);

copyBtn.innerText="Copied ✓";

setTimeout(()=>{

copyBtn.innerText="Copy Contract";

},2000);

});

}

const faqButtons=document.querySelectorAll(".faq-question");

faqButtons.forEach(btn=>{

btn.addEventListener("click",()=>{

const answer=btn.nextElementSibling;

const icon=btn.querySelector("span");

document.querySelectorAll(".faq-answer").forEach(item=>{

if(item!==answer){

item.style.display="none";

}

});

document.querySelectorAll(".faq-question span").forEach(item=>{

if(item!==icon){

item.innerText="+";

}

});

if(answer.style.display==="block"){

answer.style.display="none";

icon.innerText="+";

}else{

answer.style.display="block";

icon.innerText="−";

}

});

});

});

window.addEventListener("scroll", () => {

const header = document.querySelector(".header");

if (window.scrollY > 40) {

header.style.background = "rgba(0,0,0,.82)";
header.style.borderBottom = "1px solid rgba(255,215,0,.18)";

} else {

header.style.background = "rgba(0,0,0,.45)";
header.style.borderBottom = "1px solid rgba(255,215,0,.08)";

}

});

const observer = new IntersectionObserver((entries) => {

entries.forEach((entry) => {

if (entry.isIntersecting) {

entry.target.animate(

[
{
opacity:0,
transform:"translateY(40px)"
},
{
opacity:1,
transform:"translateY(0)"
}
],
{
duration:800,
fill:"forwards",
easing:"ease"
}
);

observer.unobserve(entry.target);

}

});

},{
threshold:0.15
});

document.querySelectorAll(
".glass-card,.team-card,.token-card,.timeline-item,.faq-item,.cta"
).forEach((el)=>{

observer.observe(el);

});
