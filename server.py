from flask import Flask, render_template
import datetime as dt
import requests
import os

# Used Environment variable "BLOG_API_ENDPOINT" to store the API Endpoint for all the blogs
API_ENDPOINT = os.getenv("BLOG_API_ENDPOINT")
app = Flask(__name__)
current_year = dt.datetime.now().year
response = requests.get(API_ENDPOINT)
blogs = response.json()


# Routing to the home page of the blog website
@app.route('/')
def home():
    return render_template("index.html", year=current_year, blogs=blogs)


# Routing to the individual blog posts for the full content
@app.route('/<int:num>')
def blog_post(num):
    for blog in blogs:
        if num == blog["id"]:
            return render_template("blog.html", blog=blog)


if __name__ == "__main__":
    app.run()
