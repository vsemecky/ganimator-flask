import sys
import flask
from flask_ngrok import run_with_ngrok
import project
from vojtovo import *

if len(sys.argv) < 2:
    exit("Missing project dir.\n\nUsage:\n\tpython web.py \"/path/to/my project\"")

project_dir = sys.argv[1]  # The first command line argument
project = project.Project(project_dir)
app = flask.Flask(__name__, static_url_path='', static_folder=project_dir)


# Homepage
@app.route("/")
def main():
    return flask.render_template('index.html', title="Homepage")


# Referenční obrázky
@app.route("/images")
def images():
    return flask.render_template('seeds.html', type="images", seeds=project.image_seeds, title="Images")


# Stylovací obrázky
@app.route("/styles")
def styles():
    return flask.render_template('seeds.html', type="styles", seeds=project.style_seeds, title="Styles")


if __name__ == "__main__":
    try:
        import google.colab
        print("Colab: YES")
        run_with_ngrok(app)  # In Google Colab run with Ngrok
    except:
        print("Colab: No")

    app.run()
