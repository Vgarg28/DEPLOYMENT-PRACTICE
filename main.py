from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>First Deployment Test</title>
        </head>
        <body>
            <h1>Python Deployment Test</h1>
            <p>This is a simple deployment test by VGARG.</p>
            <button onclick="showMessage()">Click Me!</button>
            <p id="message"></p>

        <script>
        function showMessage() {
            document.getElementById("message").innerHTML = "Hello world! Welcome to my test deployment.";
            }
        </script>
        </body>
    </html>
    """