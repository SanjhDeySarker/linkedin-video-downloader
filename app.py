from flask import Flask, request, send_file, render_template, jsonify
from downloader import LinkedInVideoDownloader
import os
import time

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")
    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        downloader = LinkedInVideoDownloader(url)
        output_dir = downloader.download_video()

        files = sorted(
            [os.path.join(output_dir, f) for f in os.listdir(output_dir)],
            key=os.path.getmtime,
            reverse=True
        )
        latest_file = files[0] if files else None

        if latest_file:
            return send_file(latest_file, as_attachment=True)
        return jsonify({"error": "No video file found"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 🔹 Serve sitemap.xml
@app.route("/sitemap.xml", methods=["GET"])
def sitemap():
    return send_file("static/sitemap.xml", mimetype="application/xml")

# 🔹 Serve robots.txt
@app.route("/robots.txt", methods=["GET"])
def robots():
    return send_file("static/robots.txt", mimetype="text/plain")

if __name__ == "__main__":
    os.makedirs("downloads", exist_ok=True)
    app.run(debug=True, host="0.0.0.0", port=5000)
