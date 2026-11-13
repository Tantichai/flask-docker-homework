import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "log.txt")
os.makedirs(LOG_DIR, exist_ok=True)

FORM_HTML = """
<!doctype html>
<title>Submit Message</title>
<h1>Submit your message</h1>
<form method="post">
  <textarea name="message"></textarea><br>
  <input type="submit" value="Submit">
</form>
"""

RESULT_HTML = """
<!doctype html>
<title>Message received</title>
<h1>Message received:</h1>
<p>{{ message }}</p>
<a href="/">Back</a>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form.get("message", "")
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(message + "\n")
        return render_template_string(RESULT_HTML, message=message)
    return FORM_HTML

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)