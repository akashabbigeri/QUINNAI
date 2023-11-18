import google.generativeai as palm
import os
from gtts import gTTS
import shutil
from tkinter import *
import tkinter.messagebox as tkmb

#palm api
palm.configure(api_key="AIzaSyAjwoJfLz3Co045-6Lfyn_p7gj1NDgLPc4")

#GUI window for getting user input
root = Tk()
root.title("Quinn")

# Create the chatbot's text area
text_area = Text(root, bg="white", width=50, height=20)
text_area.pack()

# Create the user's input field
input_field = Entry(root, width=50)
input_field.pack()

# Create the send button
send_button = Button(root, text="Send", command=lambda: send_message())
send_button.pack()

def send_message():
  # Get the user's input
  user_input = input_field.get()

  # Clear the input field
  input_field.delete(0, END)
  
  defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":1},{"category":"HARM_CATEGORY_TOXICITY","threshold":1},{"category":"HARM_CATEGORY_VIOLENCE","threshold":2},{"category":"HARM_CATEGORY_SEXUAL","threshold":2},{"category":"HARM_CATEGORY_MEDICAL","threshold":2},{"category":"HARM_CATEGORY_DANGEROUS","threshold":2}],
}
  
  prompt = user_input                                                    #User Input
  response = palm.generate_text(
  **defaults,
  prompt=prompt)
  
  #Speech Engine(Text to Speech)/VUI
  speech = gTTS(text= response.result, lang= 'en', slow= False, tld= "co.uk")
  speech.save("PALM_result.mp3")
  shutil.move("PALM_result.mp3", r'D:\Speech_Results\PALM_result.mp3')
  os.system(r'D:\Speech_Results\PALM_result.mp3')
  
  # Display the response in the chatbot's text area
  text_area.insert(END, f"User: {user_input}\n")
  text_area.insert(END, f"Quinn: {response.result}\n")

root.mainloop()

#Flask for Webapplication
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
  user_input = request.form["user_input"]
  response = response.result(user_input)
  return render_template("index.html", response=response.result)

@app.errorhandler(500)
def internal_server_error(error):
    return 'Internal Server Error: {}'.format(error), 500

from logging import FileHandler, WARNING

file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

app = Flask(__name__)
app.logger.addHandler(file_handler)


if __name__ == "__main__":
  app.run()