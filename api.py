from flask import Flask, request
import subprocess, os

app = Flask(__name__)

@app.route('/onlines', methods=['GET', 'POST'])
def onlines():
    return subprocess.Popen("response=$(ps -x | grep sshd | grep -v root | grep priv | wc -l) && echo $response", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)