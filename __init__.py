from flask import render_template, url_for, request, jsonify, redirect
import flask_excel as excel
from werkzeug import secure_filename
from app import app
import json
import os

excel.init_excel(app)

@app.route('/upload')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect('/upload')


@app.route('/')
def homepage():

    title = "Epic Tutorials"
    paragraph = ["wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!","wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!wow I am learning so much great stuff!"]

    try:
        return render_template("index.html", title = title, paragraph=paragraph)
    except Exception as e:
        return str(e)

@app.route('/about')
def aboutpage():

    title = "About this site"
    paragraph = ["blah blah blah memememememmeme blah blah memememe"]

    pageType = 'about'

    return render_template("about.html", title=title, paragraph=paragraph, pageType=pageType)

@app.route('/data')
def send():
    return "<a href={}>file</a>".format(url_for('static', filename='data.json'))

@app.route('/about/contact')
def contactPage():

    title = "About this site"
    paragraph = ["blah blah blah memememememmeme blah blah memememe"]

    pageType = 'about'

    return render_template("index.html", title=title, paragraph=paragraph, pageType=pageType)


def read_json():
    with app.open_resource('static/data.json') as json_file:
        json_data = json.load(json_file)
    print(json_data)
    return json_data

@app.route('/graph')
def graph(chartID1 = 'chart_ID1', chartID2 = 'chart_ID2', chart_type1 = 'pie', chart_type2= 'pie', chart_height = 500):

    json_data = read_json()
    print(json_data)
    ls = list()
    for item in json_data:
        ls.append({"name": item['Token'], "y": item['Amount']})
    chart1 = {"renderTo": chartID1, "type": chart_type1, "height": chart_height, }
    plotOptions1 = {"pie": {"allowPointSelect": 'true', "showInLegend": 'true'}}
    series1 = [{"name": 'token', "colorByPoint": 'true', "data":ls}]
    title1 = {"text": 'Token Allocation'}
    tooltip1 = {"pointFormat": '{series.name}: <b>{point.percentage:.1f}%</b>'}

    chart2 = {"renderTo": chartID2, "type": chart_type2, "height": chart_height, }
    plotOptions2 = {"pie": {"allowPointSelect": 'true', "showInLegend": 'true'}}
    series2 = [{"name": 'token', "colorByPoint": 'true', "data": ls}]
    title2 = {"text": 'Token Allocation'}
    tooltip2 = {"pointFormat": '{series.name}: <b>{point.percentage:.1f}%</b>'}

    return render_template('graph.html', chartID1=chartID1, chart1=chart1, series1=series1, title1=title1, tooltip1=tooltip1, plotOptions1=plotOptions1,
                           chartID2=chartID2, chart2=chart2, series2=series2, title2=title2, tooltip2=tooltip2,
                           plotOptions2=plotOptions2)
 

@app.route('/graph2')
def graph2(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height, }
    series = [{"name": 'Label1', "data": [1,2,3]}, {"name": 'Label2', "data": [4, 5, 6]}]
    title = {"text": 'My Title'}
    xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
    yAxis = {"title": {"text": 'yAxis Label'}}

    return render_template('graph.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
