from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/get-env', methods=['GET'])
def get_env_var():
    # Replace 'YOUR_ENV_VARIABLE' with the name of your environment variable
    env_var_name = 'xyz'
    env_var_value = os.getenv(env_var_name, 'Environment variable not found')
    
    return jsonify({
        "Env_Var_Value": env_var_value,
        "Env_var_name": env_var_name
    })


@app.route('/', methods=['GET'])
def get_path_val():
    healthy = 'OK'
    return jsonify({"Status": healthy})

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
