from flask import Flask, render_template
from utils.charts import generate_correlation_plot

app = Flask(__name__)

@app.route("/")
def index():
    plot_html = generate_correlation_plot()
    return render_template("index.html", plot_html=plot_html)

if __name__ == "__main__":
    app.run(debug=True)
