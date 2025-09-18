from flask import Flask, request, render_template, send_file, redirect, url_for
from azure.storage.blob import BlobServiceClient
import os
from io import BytesIO

app = Flask(__name__)

# ==== CONFIG ====
CONN_STR = "DefaultEndpointsProtocol=https;AccountName=studentfiles123;AccountKey=oecUWlYczLMTDZH4RbsBSdKRzNWw9oSxIlC6QUimWCkRKEkdyJdhvitPBcHEKeLGK8C73JbIwc/Y+AStJo3N/g==;EndpointSuffix=core.windows.net"  # Copy from Azure Access Keys
CONTAINER = "studentfiles"

blob_service = BlobServiceClient.from_connection_string(CONN_STR)
container_client = blob_service.get_container_client(CONTAINER)

# ==== ROUTES ====
@app.route("/")
def index():
    blobs = [b.name for b in container_client.list_blobs()]
    return render_template("index.html", files=blobs)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    if file:
        container_client.upload_blob(name=file.filename, data=file, overwrite=True)
    return redirect(url_for("index"))

@app.route("/download/<filename>")
def download(filename):
    blob = container_client.download_blob(filename)
    return send_file(BytesIO(blob.readall()), download_name=filename, as_attachment=True)

@app.route("/delete/<filename>")
def delete(filename):
    container_client.delete_blob(filename)
    return redirect(urlc_for("index"))

# This is required for Azure App Service
application = app

if __name__ == "__main__":
    app.run(debug=True)


