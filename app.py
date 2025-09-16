from flask import Flask, render_template, request, jsonify
from datetime import datetime
import pyotp

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=current_time)

@app.route('/generate_totp', methods=['POST'])
def generate_totp():
    try:
        secret_key = request.json.get('secret_key', '').strip()
        if not secret_key:
            return jsonify({'error': 'Secret key is required'}), 400

        totp = pyotp.TOTP(secret_key)
        code = totp.now()

        return jsonify({'code': code})
    except Exception as e:
        return jsonify({'error': f'Invalid secret key: {str(e)}'}), 400

if __name__ == '__main__':
    app.run(debug=True)