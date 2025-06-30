function showMessage(){
    console.log("Click me button is pressed")
    alert("Initial event Triggered")
}

const button = document.getElementById("my_button")
button.onclick = function(){
    alert("External event triggered")
}