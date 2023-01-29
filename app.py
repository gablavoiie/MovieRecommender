from flask import Flask, render_template, request, jsonify
import json
import openai
app = Flask(__name__)

with open('key.json') as json_file:
    data = json.load(json_file)
    openai.api_key=data["openAIKey"]
user_data = {}
questions = [
"Genre Preferences",

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
question_names = ["genres", "similar_movies", "maturity", "decade", "lenght", "actor-director", "text-box", "number-of-movies"]
#url, text

def getMovie(user_data):
    return "https://meanbusiness.com/wp-content/uploads/2018/04/PuppyEatingBanana.gif", "Fault in Our Stars"
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
        user_data[question_names[question_index]] = result
        print(user_data)

        result_list = result.split(',')

        

        #elif result[0] == "R":
           # prompt = "Feeling steemy, huh ?"

        prompt = "I love" + result_list[0] + "movies"
        if result[0] in ["G", "PG", "PG-13"]:
            prompt = "I love" + result_list[0] + "rated movies for kids"
        if result[0] == "romance":
            prompt = "I love sweet and kind movies"
        if result[0] == "long":
            prompt = "I prefer three hour movies over 1 hour movies"

        completion = "?"
        if question_index <=5:
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
        
        if (len(user_data) >= len(question_names)):
            movieURL, movieText = getMovie(user_data)
        else:
            movieURL = "none"
            movieText = "none"
        question_index+=1
        

        #user_data.append(request.get_data())
    #results = {'processed': 'true'}
    return jsonify({"nextQ": questions[question_index], "chatGPT": completion, "movieURL": movieURL, "movieText":movieText})

if __name__ == "__main__":
  app.run(debug=True)