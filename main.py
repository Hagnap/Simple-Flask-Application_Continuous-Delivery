# Imports
from flask import Flask
from flask import jsonify
import pandas as pd
import wikipedia

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

# Routes
# Basic route
@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello, this is my project!'

# Json route
@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)


# HTML route
@app.route('/html')
def html():
    """Returns some custom HTML"""
    return """
    <title>Cloud Computing - Project1</title>
    <html>
        <h2><i>This project utilizes</i></h2>
            <ul>
                <li>Continuous Delivery</li>
                <li>A Build Trigger</li>
                <li>A Build Trigger</li>
            </ul>
            <h2><i>Routes</i></h2>
            <ul>
                <li>"/"</li>
                <li>"/name/<value>"</li>
            </ul>
        <h2><i>Requirements</i></h2>
        <ul>
            <li>Flask==1.1.1</li>
            <li>pytest</li>
            <li>pylint</li>
            <li>wikipedia</li>
            <li>google-cloud-language</li>
        </ul>
        <h2><i>Makefile Commands</i></h2>
        <ul>
                <li>install</li>
                <li>lint</li>
                <li>run</li>
                <li>all</li>
        </ul>
        </header>
    </html>
    """


# Pandas route
@app.route('/pandas')
def pandas_sugar():
    df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())


# Wikipedia route
@app.route('/wikipedia/<company>')
def wikipedia_route(company):
    result = wikipedia.summary(company, sentences=10)
    return result


# natural-language-processing route
@app.route('/nlp/<company>')
def nlp_route(company):
    # Imports the Google Cloud client library
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types
    result = wikipedia.summary(company, sentences=10)
    client = language.LanguageServiceClient()
    document = types.Document(
        content=result,
        type=enums.Document.Type.PLAIN_TEXT)
    entities = client.analyze_entities(document).entities
    return str(entities)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)