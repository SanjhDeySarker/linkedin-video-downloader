from flask import Flask, request, send_file, jsonify
from downloader import LinkedInVideoDownloader
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return """
    <h2>LinkedIn Video Downloader</h2>
    <form action="/download" method="post">
        <input type="text" name="url" placeholder="Paste LinkedIn post URL" style="width:400px;">
        <button type="submit">Download</button>
    </form>
    """

@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url") or request.json.get("url")
    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        downloader = LinkedInVideoDownloader(url)
        filepath = downloader.run()
        return send_file(filepath, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    os.makedirs("downloads", exist_ok=True)
    app.run(debug=True)
