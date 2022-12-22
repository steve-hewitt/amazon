# Amazon Rainforest Fire Forecasting

UC Berkeley School of Information<br>
Capstone Project<br>

<p>An examination of deforestation-linked fires in the Brazilian state of Pará. Using satellite fire detections and supplementary governmental data we aim to predict which deforested areas will experience fires, and once fires start we forecast how they will spread.</p>

<section><b>Project Team:</b>
<ul><li>Steven Hewitt</li>
<li>Chang Liu</li>
<li>Fernando Roriz</li>
<li>Jose Torres</li></ul></section>

<b>Website:</b> https://apps-fall22.ischool.berkeley.edu/AmazonFires/ <br>

### Repo Contents
    ├── EDA
        ├── BDQueimadasEDA.ipynb                                    <- Exploration of fire data from BDQueimadas.
        └── Pixel_Filter_and_EDA.ipynb                              <- Exploration of fire data from VIIRS.
    ├── Flask
        └── flaskapp.py                                             <- Code that powers the team website.
    ├── Roriz
        ├── Exploratory_Geopandas_Terra_Brasilis_Data.ipynb         <- Experimentation with deforestation data.
        ├── Union_Within_Geopandas_BDQueimadas_Deforestation.ipynb  <- GeoPandas merge experiments.
        └── get_BDqueimadas_data.ipynb                              <- Code to merge BDqueimadas files.
    ├── pipeline
        ├── Deforestation_cuDF.ipynb                                <- GPU-powered point-in-polygon filtering.
        └── VIIRS_Para_Filter_cuDF.ipynb                            <- GPU-powered point-in-polygon filtering.
    ├── wind_data
        ├── wind_20210101.nc4                                       <- Sample data for testing wind filtering.
        ├── wind_20210102.nc4                                       <- Sample data for testing wind filtering.
        ├── wind_20210103.nc4                                       <- Sample data for testing wind filtering.
        ├── wind_20210104.nc4                                       <- Sample data for testing wind filtering.
        └── wind_20210105.nc4                                       <- Sample data for testing wind filtering.
    ├── Amazon Fires - Presentation.pptx              <- Presentation explaining project.
    ├── CLSTM_Baseline.ipynb                          <- Baseline forecasting model.
    ├── Conv_LSTM_MNIST.ipynb                         <- Final forecasting model.
    ├── Dataset_Constructor_v3.ipynb                  <- Pipeline for baseline forecasting model.
    ├── Dataset_Constructor_vF.ipynb                  <- Pipeline for final forecasting model.
    ├── Deforestation_Fire_Models_Final.ipynb         <- Final classification model.
    ├── Model_Evaluator.ipynb                         <- Evaluation code for forecasting models.
    ├── README.md                                     <- Overview of repo contents.
    ├── W210_forestfire_precip_data_cleaning.ipynb    <- Code for precipiation data preprocessing.
    ├── W210_forestfire_wind_cleaning.ipynb           <- Original code for wind data preprocessing.
    └── W210_forestfire_wind_data_cleaning_v2.ipynb   <- Final code for wind data preprocessing.
