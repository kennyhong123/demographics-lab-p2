from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

def get_state_options():
    op = reques.args['option']
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    for c in counties:
        return op += Markup("<option value=\"" + c["State"] + "\">" + c["State"] + "</option>")
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
