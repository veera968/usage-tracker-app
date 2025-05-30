<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Usage Tracker App - Sign Up</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f4; }
        .signup-container {
            max-width: 400px;
            margin: 60px auto;
            background: #fff;
            padding: 32px 24px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        h2 { text-align: center; margin-bottom: 24px; }
        label { display: block; margin-bottom: 6px; }
        input[type="text"], input[type="email"], input[type="password"] {
            width: 100%;
            padding: 8px;
            margin-bottom: 16px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            width: 100%;
            padding: 10px;
            background: #007bff;
            color: #fff;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover { background: #0056b3; }
    </style>
</head>
<body>
    <div class="signup-container">
        <h2>Sign Up</h2>
        <form id="signupForm">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" required>

            <label for="email">Email</label>
            <input type="email" id="email" name="email" required>

            <label for="password">Password</label>
            <input type="password" id="password" name="password" required>

            <button type="submit">Create Account</button>
        </form>
    </div>
    <script>
        document.getElementById('signupForm').addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Sign up successful! (Demo only)');
            // Here you would add your sign up logic (e.g., send data to server)
        });
    </script>
</body>
</html>
