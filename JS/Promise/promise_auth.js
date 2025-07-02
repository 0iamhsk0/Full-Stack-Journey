const timeout = 2000; // 2 seconds delay

const authTask = new Promise((resolve, reject) => {
    setTimeout(() => {
        const hasError = false;
        const username = "gamer123";
        if (hasError) {
            reject("Authentication failed: Invalid credentials.");
        } else {
            resolve({ username: username });
        }
    }, timeout);
});

authTask
    .then(user => {
        console.log("Authentication successful!");
        console.log("Welcome,", user.username);
    })
    .catch(error => {
        console.log("Authentication error:", error);
    });
