from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from app.torch_utils import transform_image, get_prediction

def create_app():
    app = Flask(__name__)
    CORS(app)

    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

    def allowed_file(filename):
        return "." in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @app.route('/predict', methods=['POST'])
    @cross_origin()
    def predict():
        if request.method == 'POST':
            file = request.files.get('file')
            if file is None or file.filename == "":
                return jsonify({'error': 'no file'})
            if not allowed_file(file.filename):
                return jsonify({'error': 'format not supported'})

            img_bytes = file.read()
            tensor = transform_image(img_bytes)
            prediction = get_prediction(tensor)
            data = {'prediction': prediction.item(), 'class_name': str(prediction.item())}
            return jsonify(data)

        return jsonify({'result': 1})

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
