from flask import Flask, request

app = Flask(__name__)

# Get map HTML from file and store as string.
#with open('/groups/AmazonFires/flaskapp/map.html') as map_html_doc:
#    map_html = map_html_doc.read()
map_html = '<html><body><font color="red"><h1>MAP</h1></font></body></html>'

# HTML for header and sidenav.
def get_top(title):
    return """<html>
        <head>
        <title>""" + str(title) + """</title>
            <style>
            body {
            font-family: 1em sans-serif, Arial, Geneva, Helvetica
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
    <h2>Amazon Fire Prediction<br>By: Steven Hewitt, Chang Liu, Fernando Roriz, Jose Torres</h2>
	<h2> <br>Motivation</h2>
	<p> There are thousands of fires in the Amazon Rainforest that pose a threat to millions of animals and hundreds of indegenous tribes that depend on the Amazon to survive. 
	Lula (President Elect of Brazil) during his campaign promised to fight deforestation, grant protected status to 500,000 square Kilometers of the Amazon, subsidize sustainable farming, and reform the tax code to usher a greener economy. 
	Brazil vowed to halt deforestation by 2030 but in June of 2022 the number of fires in the Amazon hit a 15 year high. 
	The destruction of tropical forests is responsible for approximately 9% of human caused carbon dioxide emissions. Brazil is crucial for discussions on climate change. 
	Its size and the fact that most of the Amazon is Brazilian territory puts Brazil in the spotlight.<br> 
	<br> Our project focuses on the Brazilian state of Para and aims to answer 2 questions. 
	<br> <strong>Question 1: </strong><em>Given a recently deforested area can we predict if a fire will occur there later in the same year?</em>
	<br> <strong>Question 2:</strong> <em>Once a fire begins anywhere in the rainforest can we predict how it will spread?</em> </p>
    """
    
    main_html = get_top(title) + main_html + get_bottom()
    return main_html


@app.route("/data")
def data_page():
    title = "Amazon Rainforest Fire Forecasting: Data & Pipeline"
    data_html = """
    <h2> <br>Data </h2>
	<p> We used the same datasets for both models and questions.
	Our data on forest fires comes form NASA Earth VIIRS (Visible Infrared Imaging Radiometer Suite) which takes in active fire data.
	VIIRS captures thermal anomalies and active fire data from Suomi National Polar-orbiting Parnership and NOAA-20 satellites.
	Our data on deforestation and shapefiles for Brazil comes form Terrabrasilis Deforestation Data.
	Some of the key features include lon, lat, state, date, polygon shape, satellite, deforestation, and classification.
	The goal with this data set is to see how many forest fire instances took place in deforestation areas based on geological informaion.
	</p>
    """
    
    data_html = get_top(title) + data_html + get_bottom()
    return data_html


@app.route("/classify")
def classify_page():
    title = "Amazon Rainforest Fire Forecasting: Classification Model"
    classify_html = """
    <h2> <br>Model 1 </h2> 
	<p>
	This first model corresponds to question 1.
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
    <iframe src="https://apps-fall22.ischool.berkeley.edu/AmazonFires/map" width="800" height="450" frameBorder="0"></iframe>
    """
    
    classify_html = get_top(title) + classify_html + get_bottom()
    return classify_html

@app.route("/forecast")
def forecast_page():
    title = "Amazon Rainforest Fire Forecasting: Forecasting Model"
    forecast_html = """
    <h2> <br>Model 2 </h2>
	<p> 
	Our second model uses a convolutional LSTM model. 
	It combines recurrent connection of an LSTM with the convolutional kernel of a CNN.
	This was originally developed in 2015 on precipitaion nowcasting. 
	For our model our input is one frame per day and one output frame per prediction. 
	We attempted to map a multichannel input to a single channel output. 
	Our final model utilized a transfer learning approach. 
	Our primary metric that we used was Mean Squared Error or MSE. 
	The supporting metrics we used were Structural similarity  or SSIM and Peak Signal-to-Noise Ratio or PSNR.
	SSIM is the perceived similarity of images and uses luminance, contrast and structure.
	SSIM ranges from -1 to 1 with 1 being perfect.
	PSNR is designed to grade image compression
	It ranges from 0 to 100 with 100 being perfect.
	<br>Image with results goes here<br>
	The best early model results used for and deforestation data as inputs.
	WBCE loss helped with the class imbalance.
	We used 2017-2019 data to train our model and evaluated it against the 2020 dataset.
	We then broadened the scope  of the data set from September data to include October, November and parts of August.
	We reduced the number of model parameters by removing one ConvLSTM layer and decreasing the number of filters.
	Another adjustment we made to the model was incorporating transfer learning.
	Pretrained on moving MNIST and provided 90,000 clean 11 frame examples for our model to learn to encode, decode and predict motion.
	The VIIRS data was fine tuned and the deforestation data was dropped for transfer learning to work properly.
	Our models were evaluated on the 2021 test set.
	Transfer learning approach massively improved all metrics.</p>
	<br> insert image with final results here <br>
    """
    
    forecast_html = get_top(title) + forecast_html + get_bottom()
    return forecast_html

@app.route("/team")
def team_page():
    title = "Amazon Rainforest Fire Forecasting: Project Team"
    team_html = """
    <h2> <br>Team</h2>
	<br> <a href="https://www.linkedin.com/in/stevenhewitt/" target="_blank">Steven Hewitt</a>
	<br> Chang Liu
	<br> <a href="https://www.linkedin.com/in/fernando-roriz-75607b79/" target="_blank">Fernando Roriz</a>
	<br> <a href="https://www.linkedin.com/in/torres-jose/" target="blank">Jose Torres</a>
    """
    
    team_html = get_top(title) + team_html + get_bottom()
    return team_html

@app.route("/map")
def map_page():
    # Special case designed to be used inside an iFrame.
    map_page_html = map_html
    return map_page_html

if __name__ == "__main__":
    app.run()