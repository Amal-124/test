from chatbot import chatbot #loading the chatbot file
from flask import Flask, render_template, request #for get 

#import flask library 
app = Flask(__name__) #main script
app.static_folder = 'static'

@app.route("/") #homepage/ path to the page
def home():
    return render_template("index1.html")

@app.route("/get") #to handle msgs 
def get_bot_response():
    userText = request.args.get('msg') #requests from html 
    return str(chatbot.get_response(userText)) #getting respose if user enters text  and returning answer
    #return string 
    
if __name__ == "__main__": #keep runing
    app.run(debug=True) #refresh without turing off the server

    