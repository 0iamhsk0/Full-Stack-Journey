function showMessage(){
    console.log("Click me button is pressed")
    alert("Initial event Triggered")
}

const button = document.getElementById("my_button")
button.onclick = function(event){
    console.log("Event Type: ${event.type}")
    console.log("Target Element: ${event.target.tagline}")
    alert("External event triggered")
}