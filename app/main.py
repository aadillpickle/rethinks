import os
import openai
from dotenv import load_dotenv
from flask import render_template, flash, redirect, url_for, Flask
from forms import LoginForm

load_dotenv()
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index():
   form = LoginForm()
   if form.validate_on_submit():
     prompt = ("The following is a list of negative thoughts which are then reframed with in a more positive, hopeful way:" + "\n\nNegative: this will never work out\nPositive: I'm having trouble right now, but it's not a big deal if this doesn't work out."
     + "\nPositive: I'm having some trouble right now, but I'm making plans to solve those problems."
     + "\n\nNegative: why do i suck at this\nPositive: I have learned a lot about this topic. I want to keep learning more about it so I'll keep up the effort.\nPositive: I know what I need to improve."
     + "\n\nNegative: " + form.thought.data)
      
     response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content":prompt}],
        max_tokens=256,
    )

     messages = str(response["choices"][0]["text"]).split("Positive:")
     if len(messages) >= 2:
          flash("Here's another way to think about that: " + messages[1])
     else:
          flash("Our robots seem to be overly negative right now. Please try again.")

   return render_template('index.html',  title='Input Form', form=form)

if __name__ == "__main__":
  app.run(debug=False, host='0.0.0.0', port=int(os.environ.get("PORT")))

