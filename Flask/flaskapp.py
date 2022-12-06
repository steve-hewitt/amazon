from flask import Flask, request

app = Flask(__name__)

# Get map HTML from file and store as string.
with open('/groups/AmazonFires/flaskapp/map.html') as map_html_doc:
    map_html = map_html_doc.read()
#map_html = '<img src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/static/firemap.jpg" width="800" height="450">'

# HTML for header and sidenav.
def get_top(title):
    return """<html>
        <head>
        <title>""" + str(title) + """</title>
            <style>
            body {
            font-family: sans-serif, Arial, Geneva, Helvetica
            }

            /* sidebar menu */
            .sidenav {
                height: 100%;
                width: 200px;
                position: fixed;
                z-index: 1;
                top: 0;
                left: 0;
                background-color: #F7F3F3;
                overflow-x: hidden;
                padding-top: 50px;
            }
            /* nav menu links */
            .sidenav a {
                padding: 6px 8px 6px 20px;
                text-decoration: none;
                font-size: 18px;
                color: #030303;
                display: block;
            }
            /* link hover effect */
            .sidenav a:hover {
                color: #AC0A0A;
            }
            .sidenav img {
                padding: 6px 8px 6px 20px;
            }
            .main {
                margin-left: 200px;
                padding: 0px 10px;
            }
            </style>
        </head>
        <body>
            <div class="sidenav">
                <img src="https://www.ischool.berkeley.edu/sites/default/files/berkeleyischool-logo-modified-blue.svg" width="120" height="68" padding/>
                <br>
                <br>
                <a href="https://apps-fall22.ischool.berkeley.edu/AmazonFires/">Project Overview</a>
                <a href="https://apps-fall22.ischool.berkeley.edu/AmazonFires/data">Data & Pipeline</a>
                <a href="https://apps-fall22.ischool.berkeley.edu/AmazonFires/classify">Classification Model</a>
                <a href="https://apps-fall22.ischool.berkeley.edu/AmazonFires/forecast">Forecasting Model</a>
                <a href="https://apps-fall22.ischool.berkeley.edu/AmazonFires/team">Project Team</a>
		    <a href="https://apps-fall22.ischool.berkeley.edu/AmazonFires/references">Reference Materials</a>
            </div>

            <div class="main">
    """
# Close out HTML tags at the end.
def get_bottom():
    return """            </div>
        </body>
    </html>
    """

@app.route("/")
def main_page():
    title = "Amazon Rainforest Fire Forecasting: Project Overview"
    main_html = """
    <br><center><h1 style="font-size: 3rem">Amazon Fire Prediction</h1><br><h2>By: Steven Hewitt, Chang Liu, Fernando Roriz, Jose Torres</h2></center><br>
	<h1>Motivation</h1>
	<p> There are thousands of fires in the Amazon Rainforest that pose a threat to millions of animals and hundreds of indegenous tribes that depend on the Amazon to survive. 
	Lula (President Elect of Brazil) during his campaign promised to fight deforestation, grant protected status to 500,000 square Kilometers of the Amazon, subsidize sustainable farming, and reform the tax code to usher a greener economy. 
	Brazil vowed to halt deforestation by 2030 but in June of 2022 the number of fires in the Amazon hit a 15 year high. 
	The destruction of tropical forests is responsible for approximately 9% of human caused carbon dioxide emissions. Brazil is crucial for discussions on climate change. 
	Its size and the fact that most of the Amazon is Brazilian territory puts Brazil in the spotlight.<br> 
	<br> Our project aims to answer 2 questions, focusing on the Brazilian state of Par&#225;:<br><br>
	<table cellspacing="0" cellpadding="0">
	<tr><td><img src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/static/map_para.jpg"></td>
	<td><img src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/static/multi_q.jpg"></td></tr></table>
    """
    
    main_html = get_top(title) + main_html + get_bottom()
    return main_html


@app.route("/data")
def data_page():
    title = "Amazon Rainforest Fire Forecasting: Data & Pipeline"
    data_html = """
    <center><h1><br>Data </h1></center>
	<p> We used the same datasets for both models and questions.
	Our data on forest fires comes form NASA Earth VIIRS (Visible Infrared Imaging Radiometer Suite) which takes in active fire data.
	VIIRS captures thermal anomalies and active fire data from Suomi National Polar-orbiting Parnership and NOAA-20 satellites.
	Our data on deforestation and shapefiles for Brazil comes form Terrabrasilis Deforestation Data.
	Some of the key features include lon, lat, state, date, polygon shape, satellite, deforestation, and classification.
	The goal with this data set is to see how many forest fire instances took place in deforestation areas based on geological informaion.
	</p>
    <br> <center><img src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/static/Nasa.PNG"> <img src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/static/TerraBrasilis.PNG"></center>
    <br> <center> <h1> Data Pipeline </h1> </center>
    <br> <center><img src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/static/TargetedFiltering.PNG"></center>
    <br> <center><img src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/static/FireResample.PNG"></center>
    <br> <center><img src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/static/DeforestationResample.PNG"></center>
    <br> <center><img src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/static/PredictionTask.PNG"></center>
    """
    
    data_html = get_top(title) + data_html + get_bottom()
    return data_html


@app.route("/classify")
def classify_page():
    title = "Amazon Rainforest Fire Forecasting: Classification Model"
    classify_html = """
    <center><h1><br>Classification Model</h1></center> 
	<p>
	<center><img src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/static/q1.jpg"></center>
	<br>
	<br>
	This model is a KNN model with 10 neighbors.
	We used KNN because it is able to capture clusters which is an important feature to our problem.
	For this model the variables used were: Deforested Area, Perimiter of the deforested area, Latitude, Longitude, and Distance to closest road. 
	The positive predictive value of this model is 65%.
	For every year there are clusters of fires  after the satellites capture deforestation. 
	There are also areas where we see deforestation but very few fires.
	There are generally areas where the areas of deforestation are smaller and degradation in these areas occur gradually. 
	Areas with legal protected status are essential to controlling deforestation and ultimately forest fires. 
	In those protected areas there are national parks, indigenous reserves and extractive reserves. 
	Areas on the map that seem to be untouched for the most part are areas with legal protection status. 
	</p>
	<table cellspacing="0" cellpadding="0"><tr><td>
    	<iframe src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/map" width="880" height="600" frameBorder="0"></iframe>
	</td><td><img src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/static/legend.jpg"></td></tr></table>
        <br><br> <center><img src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/static/FireClusters.PNG">
        <br><br><img src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/static/DeforestationNoFire.PNG">
        <br><br><img src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/static/LegalProtectionArea.PNG"></center>
    """
    
    classify_html = get_top(title) + classify_html + get_bottom()
    return classify_html

@app.route("/forecast")
def forecast_page():
    title = "Amazon Rainforest Fire Forecasting: Forecasting Model"
    forecast_html = """
    <center><h1><br>Forecasting Model</h1></center>
	<p> 
	<center><img src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/static/q2.jpg"></center>
	<br><br>
	Our forecasting model is built using the Keras implementation of Convolutional LSTMs.
	These layers, originally developed in a 2015 paper on precipitaion nowcasting, combine the recurrent connection of an LSTM with the convolutional kernel of a CNN.
	We chain multiple ConvLSTM layers together in sequence to treat our problem as a next frame video prediction task.
	The model input is a 10 frame video, with one frame per day representing the location of fires/deforestation in the area of interest, and the output is a prediction of fire locations for the next day.
	The primary metric that we used to measure success was Mean Squared Error (MSE), which ranges from 0 to 1 for our model.
	The supporting metrics we used were Structural Similarity Index Measure (SSIM) and Peak Signal-to-Noise Ratio (PSNR).
	SSIM is the perceived similarity of images using a composite measure of luminance, contrast, and structure. SSIM ranges from -1 to 1, with 1 being perfect.
	PSNR was originally designed to grade output fidelity from using different image compression algorithms. It ranges from 0 to 100, with 100 being perfect.
	We used 2017-2019 data to train our baseline model and evaluated it against the 2020 dataset.
	Utilizing WBCE loss helped with the severe class imbalance in our target prediction labels.</p>
	<u>Baseline Results</u>
	<table border="1" cellpadding="0" cellspacing="0"><tr><td><b>Model Version</b></td><td><b>MSE</b></td><td><b>SSIM</b></td><td><b>PSNR</b></td></tr>
	<tr><td>Baseline</td><td>0.050</td><td>0.373</td><td>15.44</td></tr></table>
	
	<p>To improve on our baseline model, we made various changes to our procedure.
	We broadened the scope  of the dataset from just September data to also include October, November and parts of August.
	We used 4-fold cross validation, with each year from 2017-2020 as a different fold.
	We reduced the number of model parameters by removing one ConvLSTM layer and decreasing the number of filters in some other layers.
	Another key adjustment we made was incorporating transfer learning.
	Pretraining on moving MNIST provided 90,000 clean 11 frame examples for our model to learn to encode, decode and predict motion.
	After 48 hours of pretraining on moving MNIST, our model was fine-tuned on the VIIRS fire dataset.
	Deforestation data had to be dropped for our transfer learning apprach to work properly.</p>
	
	<img src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/static/mnist.gif" width="128" height="128">

	<p>Once training was complete, both the baseline and the new transfer learning model were evaluated on the 2021 test set.
	The transfer learning approach massively improved performance across all metrics.</p>
	<u>Final Results</u>
	<table border="1" cellpadding="0" cellspacing="0"><tr><td><b>Model Version</b></td><td><b>MSE</b></td><td><b>SSIM</b></td><td><b>PSNR</b></td></tr>
	<tr><td>Baseline</td><td>0.042</td><td>0.334</td><td>16.09</td></tr>
	<tr><td>Transfer Learning</td><td>0.015</td><td>0.746</td><td>45.57</td></tr>
	<tr><td><i>Change</i></td><td>-0.027</td><td>0.412</td><td>29.48</td></tr>
	<tr><td><i>Change (%)</i></td><td>-64.5%</td><td>123.4%</td><td>183.3%</td></tr></table>
    """
    
    forecast_html = get_top(title) + forecast_html + get_bottom()
    return forecast_html

@app.route("/team")
def team_page():
    title = "Amazon Rainforest Fire Forecasting: Project Team"
    team_html = """
    <center><h1> <br><strong>Team</strong></h1>
    <img src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/static/Steven.jpeg" style="width:332px;height:332px;"><br>
        <a href="https://www.linkedin.com/in/stevenhewitt/" target="_blank"><h4>Steven Hewitt</h4></a><br>
        <img src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/static/Chang.png" style="width:332px;height:332px;"><br>
	<a href="https://www.linkedin.com/in/changliu0829/" target="_blank"><h4>Chang Liu</h4></a><br> 
        <img src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/static/Fernando.jpeg"> <br>
	<a href="https://www.linkedin.com/in/fernando-roriz-75607b79/" target="_blank"><h4>Fernando Roriz</h4></a><br> 
        <img src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/static/Jose.png" style="width:332px;height:332px;"><br>
	<a href="https://www.linkedin.com/in/torres-jose/" target="blank"><h4>Jose Torres</h4></a><br></center> 
    """
    
    team_html = get_top(title) + team_html + get_bottom()
    return team_html

@app.route("/references")
def references_page():
    title = "Amazon Rainforest Fire Forecasting: Reference Materials"
    references_html = """
    <h1><br>References</h1>
	<a href="https://www.earthdata.nasa.gov/learn/find-data/near-real-time/firms/viirs-i-band-375-m-active-fire-data">NASA VIIRS 375 m Active Fire Product</a><br>
	<a href="http://terrabrasilis.dpi.inpe.br/en/home-page/">TerraBrasilis - Source for Deforestation Data</a><br>
      <a href="https://cnr.ncsu.edu/news/2019/09/amazon-rainforest-fires-everything-you-need-to-know/">Amazon Rainforest Fires: Everything you need to know - Source for Motivation and background</a><br>
	<a href="https://arxiv.org/pdf/1506.04214v1.pdf">Convolutional LSTM Network: A Machine Learning Approach for Precipitation Nowcasting</a><br>
	<a href="https://www.reuters.com/business/cop/brazils-lula-put-climate-center-first-post-election-speech-abroad-2022-11-16/">COP27: Greeted like a rock star, Brazil's Lula promises to protect Amazon</a><br>
	<a href="https://www.bbc.com/news/science-environment-63625698">COP27: Brazil is back on the world stage, Lula tells climate summit</a><br>
      <a href="https://www.lemonde.fr/en/international/article/2022/11/16/cop27-lula-promises-to-protect-the-amazon_6004551_4.html">COP27: Lula promises to protect the Amazon</a><br>
	<a href="https://www.ft.com/content/b0985574-3342-41ca-a27e-5db9d0459069">Lula promises COP27 that ‘Brazil is back’ in climate change fight</a><br>
    """
    
    references_html = get_top(title) + references_html + get_bottom()
    return references_html

@app.route("/map")
def map_page():
    # Special case designed to be used inside an iFrame.
    map_page_html = map_html
    return map_page_html

if __name__ == "__main__":
    app.run()
