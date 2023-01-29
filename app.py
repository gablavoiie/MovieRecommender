from flask import Flask, render_template, request, jsonify
import spacy
from profanity_filter import ProfanityFilter
import json
import openai
import cinema
import image
#from image import *
app = Flask(__name__)

with open('key.json') as json_file:
    data = json.load(json_file)
    openai.api_key=data["openAIKey"]
user_data = {}
questions = [
"Genre Preferences",

"Think hard about the kind of movie you want to watch \N{thinking face}. Are there any movies that match the vibe?",

"What’s the audience for tonight? \N{movie camera} Choose a rating from the following: G, PG, PG-13, R.",

"How far are we going back? \N{eyes} Pick a decade.",

"How much time do we have on our hands? \N{watch} Do you want to watch a short, medium, or long movie?",

"Feeling starstruck? \N{glowing star} Any actors or directors you knead to see?",

"Anything else we should consider? The floor is yours. \N{man dancing} Think emotions, settings, tropes, plots, etc.",

"I'll now begin the movie baking process. \N{face without mouth} Stay put, I’m off to bake the perfect movie for you. \N{clapper board} Are you excited?",

"The movie is fresh out of the oven! \N{bread} Here is my personalized recommendation. No need to thank me, it’s the yeast I can do. \N{winking face}",

"I hope you love it as much as I loved talking to you. Here are my individualised, tailored recommendations.",

"This is it for me. Take care, ok?"
]
question_index = 0
question_names = ["genres", "similar_movies", "maturity", "decade", "length", "actor-director", "textbox"]
#url, text
nlp = spacy.load("en_core_web_sm")
profanity_filter = ProfanityFilter(nlps={'en': nlp})  # reuse spacy Language (optional)
nlp.add_pipe(profanity_filter.spacy_component, last=True)

def getMovie(user_data):
    title = cinema.take_input(user_data)
    url = image.image_url(title)
    return url, title
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
            #while(("?" in completion)):
            completions = openai.Completion.create(prompt=prompt,engine="text-davinci-002", max_tokens=100)
            for i in range(len(completions.choices)):
                completion = completions.choices[i].text
                gpt_text = nlp(completion)
                if ((not "?" in completion) and (gpt_text._.is_profane)):
                    break

            pos = 0
            for i in range(len(completion)):
                if completion[i].isupper():
                    pos = i
                    break
            completion = completion[pos:]
        else:
            completion = "none"
        if result_list[0].lower() == "no":
            completion = "It's okay! I'm undecisive too sometimes \N{relieved face}"
        
        if (len(user_data) == len(question_names)):
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