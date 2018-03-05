from flask import jsonify
from application import create_app
from config import load_config
config = load_config()
app = create_app()
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'status': '404'})

@app.errorhandler(500)
def page_not_found(error):
    return jsonify({'status': '500'})

app.run(debug=True, port=config.PORT)
