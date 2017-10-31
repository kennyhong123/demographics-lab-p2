from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

def get_state_options:
    option = request.args['option']
    option = Markup("<option value="memes">"+ "memes" + "</option>")

@app.route("/")
def render_main():
    get_state_options()
    return render_template('home.html')
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
