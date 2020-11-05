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


# System info
@app.route("/sysinfo")
def sysinfo():
    sysinfo = {
        'cpu_cores': 2,
        'cpu_threads': 4,
        'ram': 24,
        'gpu_ram': 16,
        'gpu_name': "V100",
    }
    return flask.render_template('sysinfo.html', sysinfo=sysinfo)


if __name__ == "__main__":
    try:
        import google.colab
        print("Colab: YES")
        run_with_ngrok(app)  # In Google Colab run with Ngrok
    except:
        print("Colab: No")

    app.run()
