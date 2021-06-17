let xButton = document.getElementsByClassName("close");

for (let i = 0; i < xButton.length; i++){
    function exit(){
        document.getElementsByClassName("alert")[i].style.display = "none";
    }
    xButton[i].addEventListener("click", exit);
}