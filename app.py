from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():

    github_username = "octocat"

    github_url = f"https://api.github.com/users/{github_username}"

    response = requests.get(github_url)

    github_data = response.json()

    quote_response = requests.get("https://zenquotes.io/api/random")

    quote_data = quote_response.json()

    quote = quote_data[0]['q']

    return render_template(
        "index.html",
        github=github_data,
        quote=quote
    )

if __name__ == "__main__":
    app.run(debug=True)