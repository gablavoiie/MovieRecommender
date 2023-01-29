from flask import Flask, render_template, request, jsonify
import json
import openai
app = Flask(__name__)

with open('key.json') as json_file:
    data = json.load(json_file)
    openai.api_key=data["openAIKey"]
user_data = []
questions = [

"Think hard about the kind of movie you want to watch. Are there any movies that match the vibe?",

"What’s the audience for tonight? Choose a rating from the following: G, PG, PG-13, R.",

"How far are we going back? Pick a decade.",

"How much time do we have on our hands? Do you want to watch a short, medium or long movie?",

"Feeling starstruck? Any actors or directors you wish to see?",

"Anything else we should consider? The floor is yours. Think emotions, settings, tropes, plots, etc.",

"If you want more than one movie recommended, how many?",

"I’ll stay silent for a minute now. Stay still, I’m off to bake you the movie of your dreams. ",

"The movie is fresh out of the oven! No need to thank me, it’s the yeast I could do. ",

"I hope you love it as much as I loved talking to you. Here are my individualised, tailored recommendations.",

"This is it for me. Take care, ok? "
]
question_index = 0
question_names = ["similar_movies", "maturity", "genres", "decade", "lenght", "actor-director", "text-box", "number-of-movies"]
#url, text
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/output_process", methods=["GET","POST"])
def output_process():
    global question_index
    if (request.method == "POST"):
        result = request.get_json()
        print("RETURNING")
        print("RESULT" + result)
        
        result_list = result.split(',')

        if result[0] in ["G", "PG", "PG-13"]:
            prompt = "I love" + result_list[0] + "rated movies for kids"
        #elif result[0] == "R":
           # prompt = "Feeling steemy, huh ?"

        prompt = "I love" + result_list[0] + "movies"
        completion = "?"
        if question_index <=4:
            while(("?" in completion)):
                completions = openai.Completion.create(prompt=prompt,
                                           engine="text-davinci-002",
                                           max_tokens=100)
                completion = completions.choices[0].text
            pos = 0
            for i in range(len(completion)):
                if completion[i].isupper():
                    pos = i
                    break
            completion = completion[pos:]
        else:
            completion = "none"
        question_index+=1
        

        #user_data.append(request.get_data())
    #results = {'processed': 'true'}
    return jsonify({"nextQ": questions[question_index], "chatGPT": completion})

if __name__ == "__main__":
  app.run(debug=True)