# Project Scoping

## Problem and expected results

People are not happy with meteo predictions, so we want to create a better solution that predicts short term temperature evolution with actual and historical meteo data.

## Stakeholders

- The people near the prediction area (users)
- Us: the managers and technical people
- Swiss meteo: the data provider
- The teachers: evaluate our work

## Requirements

Meteo data on a certain location, a prediction model, a UI where users can visualise predictions

## Machine Learning problem

We need a regression model that uses time-series data to make a time-series prediction.

We need to collect data and infer in batches.

To avoid data drift issue, continuously re-train the model with new data. Also track the model performance in production to see how it evolves.

### Input

temperature, pressure, wind, sun, rain in time-series format

### Output

Short term temperature evolution in time-serie format

### Requirements

A cloud to store our data and our model and run the pipeline.
A webpage to see the weather predictions and model performance.

## Development steps

Develop all the project steps with MLOPS in mind.

- Perform an EDA: analyse available data
- Create a first model on a notebook with downloaded historical data
- In parallel, set up the production pipeline: collect data in batches, infer in batches, display predictions, evaluate performance
- Deploy the model inside the pipeline do it automatically with CI/CD
- Implement continuous learning for our production model


