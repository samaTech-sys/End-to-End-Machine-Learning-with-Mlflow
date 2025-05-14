from flask import Flask, render_template, request
import os
import numpy as np
from mlProject.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    prediction = None
    if request.method == 'POST':
        try:
            # Validate and convert all inputs
            data = [
                float(request.form.get('fixed_acidity', 0)),
                float(request.form.get('volatile_acidity', 0)),
                float(request.form.get('citric_acid', 0)),
                float(request.form.get('residual_sugar', 0)),
                float(request.form.get('chlorides', 0)),
                float(request.form.get('free_sulfur_dioxide', 0)),
                float(request.form.get('total_sulfur_dioxide', 0)),
                float(request.form.get('density', 0)),
                float(request.form.get('pH', 0)),
                float(request.form.get('sulphates', 0)),
                float(request.form.get('alcohol', 0))  # Note: Match this with your form field name
            ]
            
            data = np.array(data).reshape(1, -1)
            obj = PredictionPipeline()
            prediction = obj.predict(data)
            
            # Return to the same page with prediction
            return render_template('index.html', 
                                prediction=str(prediction),
                                form_data=request.form)  # Pass form data back to repopulate fields
            
        except ValueError as e:
            prediction = f"Invalid input: {str(e)}"
        except Exception as e:
            prediction = f"Prediction error: {str(e)}"
    
    return render_template("index.html", prediction=prediction)

@app.route('/train', methods=['GET'])
def training():
    try:
        os.system("python main.py")
        return "Training Successful"
    except Exception as e:
        return f"Training failed: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)