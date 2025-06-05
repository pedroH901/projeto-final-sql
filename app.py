from flask import Flask
from cadastro_pet import bp_cadastro_pet

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessário para usar flash

app.register_blueprint(bp_cadastro_pet)

if __name__ == '__main__':
    app.run(debug=True)
