from flask import Flask, render_template, request
app=Flask(__name__)
WEBSITES={
    "GitHub": "https://github.com/",
    "Reddit": "https://reddit.com/user/",
    "TikTok": "https://www.tiktok.com/@"
}
@app.route("/", methods=["GET", "POST"])
def home():
    results={}
    if request.method=="POST":
        username=request.form["username"]
        for site, url in WEBSITES.items():
            results[site]=url+username
    return render_template("index.html", results=results)
if __name__=="__main__":
    app.run(debug=True)