const firstTask = new Promise((resolve, reject) => {
    setTimeout(() => {
        console.log("Async Task completed");
        resolve();
    }, 2000);
});

firstTask.then(() => console.log("First task resolved"));
