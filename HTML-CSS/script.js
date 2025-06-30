const heading = document.getElementById("main_heading");
console.log(`This is heading: ${heading.textContent}`);  // template string fix

const para = document.getElementsByClassName("para");
console.log("Elements with class 'para':", para);

const para1 = document.querySelectorAll("p");
console.log("All <p> elements:", para1);
