from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

user_data = []
questions = ["Question1", "Question2", "Question3"]
question_index = 0
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/output_process", methods=["GET","POST"])
def output_process():
    if (request.method == "POST"):
        print("RETURNING")
        result = request.get_json()
        print(result)
        #user_data.append(request.get_data())
    #results = {'processed': 'true'}
    return jsonify(questions[1])

if __name__ == "__main__":
  app.run(debug=True)