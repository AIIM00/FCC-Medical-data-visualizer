from flask import Flask, send_file
import medical_data_visualizer

app = Flask(__name__)

@app.route('/')
def home():
    # Run your visualizer functions (they will save plots)
    medical_data_visualizer.draw_cat_plot()
    medical_data_visualizer.draw_heat_map()
    return '''
        <h1>Medical Data Visualizer</h1>
        <p>Below are the generated plots:</p>
        <img src="/cat-plot" alt="Cat Plot" width="600"><br><br>
        <img src="/heat-map" alt="Heat Map" width="600">
    '''

@app.route('/cat-plot')
def cat_plot():
    return send_file('catplot.png', mimetype='image/png')

@app.route('/heat-map')
def heat_map():
    return send_file('heatmap.png', mimetype='image/png')

if __name__ == '__main__':
  import os
  port = int(os.environ.get("PORT", 10000))
  app.run(host='0.0.0.0', port=port)
