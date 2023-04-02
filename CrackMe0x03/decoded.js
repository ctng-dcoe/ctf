      function login() {
        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;
        // In a real application, you would typically send the username and password
        // to a server for authentication, but for this example we'll just check them
        // locally and return a magic value if they are correct.
        if (username === "example" && password === "password") {
          alert("Authentication successful! Your magic value is 42.");
        } else {
          alert("Authentication failed. Please try again.");
        }
      }
