<!DOCTYPE html>
<html>
<head>
	<title>Login Page</title>
</head>
<body>
	<h1>Login Page</h1>
	<form method="post" action="index.php">
		<label for="username">Username:</label>
		<input type="text" id="username" name="username"><br><br>
		<label for="password">Password:</label>
		<input type="password" id="password" name="password"><br><br>
		<input type="submit" name="submit" value="Login">
	</form>

	<?php
	if(isset($_POST['submit'])){
		// Connect to the MySQL database
		$host = 'db';
		$dbname = 'example_db';
		$user = 'example_user';
		$pass = 'example_password';
		$conn = new mysqli($host, $user, $pass, $dbname);

		// Check for errors
		if($conn->connect_error){
			die("Connection failed: " . $conn->connect_error);
		}

		// Get the username and password entered by the user
		$username = $_POST['username'];
		$password = $_POST['password'];

		// Prepare and execute the SQL query
		$sql = "SELECT * FROM users WHERE username='$username' AND password='$password'";
		$result = $conn->query($sql);

		// Check if a row was returned
		
		if($result->num_rows > 0){
			while($row = mysqli_fetch_assoc($result)){
				printf("Login successful! You are authenticated as: %s\n", $row["username"]);
				echo "<br>";

			}
			// echo "<p>Login successful!</p>";
		} else {
			echo "<p>Login failed. Please try again.</p>";
		}
		

		// Close the database connection
		$conn->close();
	}
	?>
</body>
</html>
