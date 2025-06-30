// const heading = document.getElementById("main_heading");
// console.log(`This is heading: ${heading.textContent}`);  

// const para = document.getElementsByClassName("para");
// console.log("Elements with class 'para':", para);

// const para1 = document.querySelectorAll("p");
// console.log("All <p> elements:", para1);

// Select and log the paragraph with ID 'para1'
const para1 = document.querySelector("#para1");
console.log("Selected para1:", para1);

// Set background color to all <p> elements
const allParagraphs = document.querySelectorAll("p");
for (let p of allParagraphs) {
    p.style.backgroundColor = "yellow";
}

// Safely get the first child element of para1
const firstChild = para1.firstElementChild;
if (firstChild) {
    console.log("First child element of #para1:", firstChild);
    console.log("Node name:", firstChild.nodeName);
} else {
    console.log("No element child found inside #para1");
}

// Get ID attribute of first <p> element
const firstP = document.querySelector("p");
const idval = firstP.getAttribute("id");
console.log("ID of first <p>:", idval);

// Set class on a <span> (make sure it exists!)
const spanElement = document.querySelector("span");
if (spanElement) {
    spanElement.setAttribute("class", "span_class");
} else {
    console.log("<span> element not found.");
}
