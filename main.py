from flask import Flask, request, send_file
from flask_cors import CORS
import io

app = Flask(__name__)
CORS(app)  # ← すべてのドメインからのアクセスを許可（Netlify対応）

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
    app.run(debug=True, host="0.0.0.0")
