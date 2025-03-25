import os
from flask import Flask, request, send_file
import io

app = Flask(__name__)

@app.route("/ust", methods=["POST"])
def convert_to_shiftjis():
    data = request.get_data(as_text=True)
    encoded = data.encode("shift_jis", errors="replace")
    return send_file(
        io.BytesIO(encoded),
        mimetype="text/plain",
        as_attachment=True,
        download_name="ust_export_shiftjis.ust"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) 
    app.run(debug=True, host="0.0.0.0", port=port)