# Forecast Visualization Data (V2)

New directory structure
```
weekly-summaries/
├── covid19-forecast-hub/
│   ├── <YYYY-MM-DD>/
│   │   ├── YYYY-MM-DD_covid_map_data.csv
│   │   ├── YYYY-MM-DD_covid_forecasts_data.csv
│   │   ├── YYYY-MM-DD_covid_target_data.csv
│   │   └── YYYY-MM-DD_covid_webtext.md
│   └── ...
├── rsv-forecast-hub/
│   ├── <YYYY-MM-DD>/
│   │   ├── YYYY-MM-DD_rsv_map_data.csv
│   │   ├── YYYY-MM-DD_rsv_forecasts_data.csv
│   │   ├── YYYY-MM-DD_rsv_target_data.csv
│   │   └── YYYY-MM-DD_rsv_webtext.md
│   └── ...
└── README.md
```


The following data

* are generated partially from [COVID](https://github.com/CDCgov/covid19-forecast-hub/tree/main/model-output) and [RSV](https://github.com/CDCgov/rsv-forecast-hub/tree/main/model-output) Hub submission.
* are generated partially from [NHSN hospital respiratory data](https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html) and [NSSP Emergency Department Visits data](https://data.cdc.gov/Public-Health-Surveillance/NSSP-Emergency-Department-Visit-Trajectories-by-St/rdmq-nq56/about_data).
* are used for public forecast visualization.
* follows a particular schema, outlined below.

__Map Component__ (`YYYY-MM-DD_{disease}_map_data.csv`)

_Contains data from the ensemble COVID or RSV forecast for all states (including US, DC and Puerto Rico) and for 7 and 14 day forecast targets_


* `location_name` (string): state name column. Note: US is spelled out in this version (Ex: Alabama, United States)
* `model` (string): the ensemble model name (Ex: CovidHub-ensemble)
* `quantile_0.025_per100k` (numeric): 0.025 quantile forecast value as a rate per 100k, not calculated for proportion ED visits target (Ex: 1.12777351608532, NA)
* `quantile_0.5_per100k` (numeric): 0.5 quantile forecast value as a rate per 100k, not calculated for proportion ED visits target
* `quantile_0.975_per100k` (numeric): 0.975 quantile forecast value as a rate per 100k, not calculated for proportion ED visits target
* `quantile_0.025` (numeric): 0.025 quantile forecast value (Ex: 3754.07763671875)
* `quantile_0.5` (numeric): 0.5 quantile forecast value
* `quantile_0.975` (numeric): 0.975 quantile forecast value
* `quantile_0.025_per100k_rounded` (numeric): forecasted value as a rate per 100k, rounded to 2 places (Ex: 3.57). Not calculated for proportion ED visits target
* `quantile_0.5_per100k_rounded` (numeric): forecasted value as a rate per 100k, rounded to 2 places. Not calculated for proportion ED visits target
* `quantile_0.975_per100k_rounded` (numeric): forecasted value as a rate per 100k, rounded to 2 places. Not calculated for proportion ED visits target
* `quantile_0.025_rounded` (numeric): 0.025 quantile forecast value, rounded up to the nearest integer for counts and rounded to 4 decimal places for proportion (Ex: 3755)
* `quantile_0.5_rounded` (numeric): 0.5 quantile forecast value, rounded up to the nearest integer for counts and rounded to 4 decimal places for proportion
* `quantile_0.975_rounded` (numeric): 0.975 quantile forecast value, rounded up to the nearest integer for counts and rounded to 4 decimal places for proportion
* `target` (string): description of forecast target date (Ex: wk inc covid/rsv hosp, or wk inc covid/rsv prop ed visits)
* `target_end_date` (date): target date for the forecast (Ex: 2024-11-30)
* `reference_date` (date): date that the forecast was generated (Ex: 2024-11-23)
* `target_end_date_formatted` (string): target date for the forecast, prettily re-formatted as a string (Ex: “November 30, 2024”)
* `reference_date_formatted` (string): date that the forecast was generated, prettily re-formatted as a string (Ex: “November 23, 2024”)

__Timeseries Component__ (`YYYY-MM-DD_{disease}_forecasts_data.csv`):

_Contains all the available COVID or RSV models submitted in a given week for all states (including US, DC and Puerto Rico)._

* `location_name` (string): full state name for the forecast. Note: US is spelled out in this version (Ex: Alabama, United States)
* `abbreviation` (string): abbreviated state name (Ex: AL)
* `horizon` (numeric): time horizon for the forecast. Currently using time horizons 0, 1, 2, 3 (Ex: 2)
* `forecast_date` (date): date that forecast was generated (Ex: 2024-11-23)
* `target_end_date` (date): target date for forecast (Ex: 2024-11-30)
* `target` (string): description of forecast target  (Ex: wk inc covid/rsv hosp, or wk inc covid/rsv prop ed visits)
* `model` (string): name of the model, pulled from the folder names in the model-output section of the forecast repos (Ex: FluSight-ensemble, CEPH-Rtrend_fluH)
* `quantile_0.025` (numeric): 0.025 quantile forecast value (Ex: 922.475)
* `quantile_0.25` (numeric): 0.25 quantile forecast value
* `quantile_0.5` (numeric): 0.5 quantile forecast value
* `quantile_0.75` (numeric): 0.75 quantile forecast value
* `quantile_0.975` (numeric): 0.975 quantile forecast value
* `quantile_0.025_rounded` (numeric): 0.025 quantile forecast value, rounded up to the nearest integer for counts and rounded to 4 decimal places for proportion (Ex: 923)
* `quantile_0.25_rounded` (numeric): 0.25 quantile forecast value, rounded up to the nearest integer for counts and rounded to 4 decimal places for proportion
* `quantile_0.5_rounded` (numeric): 0.5 quantile forecast value, rounded up to the nearest integer for counts and rounded to 4 decimal places for proportion
* `quantile_0.75_rounded` (numeric): 0.75 quantile forecast value, rounded up to the nearest integer for counts and rounded to 4 decimal places for proportion
* `quantile_0.975_rounded` (numeric): 0.975 quantile forecast value, rounded up to the nearest integer for counts and rounded to 4 decimal places for proportion
* `forecast_teams` (string): name of the team that generated the model; pulled from model metadata (Ex: CEPH Lab at Indiana University)
* `forecast_fullnames` (string): full name of the model; pulled from model metadata (Ex: Rtrend COVID)

__Truth Data__ (`YYYY-MM-DD_{disease}_target_data.csv`)

_Contains the most recent observed COVID or RSV hospitalization and proportion of ED visits data for all states (including US, DC and Puerto Rico) but not including the remainder of the territories._

* `week_ending_date` (date): week ending date of observed data per row (Ex: 2024-11-16)
* `location` (string): two-digit FIPS code associated with each state (Ex: 06)
* `location_name` (string): spelled out state name (note: US is spelled out) (Ex: California, United States)
* `target` (string): description of the truth data target (Ex: "wk inc disease hosp")
* `value` (numeric): number of hospital admissions or proportion of ED visits; Hospital admissions should be an integer (Ex: 3); proportion of ED visits should be of form 0.**

__Webtext data__ (`YYYY-MM-DD_{disease}_webtext.md`)

_Contains texts populating the public forecast pages._

## Hospital Admissions

- The {`hub_name`} ensemble's one-week-ahead forecast predicts that the number of new weekly laboratory-confirmed {`disease`} hospital admissions will be approximately {`number of US hospitalizations from ensemble model, time horizon 2`} nationally, with {`lower 95% CI prediction for ensemble model`} to {`upper 95% CI prediction for ensemble model`} laboratory confirmed {`disease`} hospital admissions likely reported in the week ending {`week ending date for horizon 2 forecasts`}.

- This is compared to the {`last reported hospitalizations`} admissions reported for the week ending {`last reported target date`}, the most recent week of reporting from U.S. hospitals.

- Reported and forecasted new {`disease`} hospital admissions as of {`forecast_due_date`}.

- The figure shows the number of new laboratory-confirmed {`disease`} hospital admissions reported in the United States each week from {`first_hospital_target_data_date`} through {`last_hoapital_target_data_date`} and forecasted new {`disease`} hospital admissions per week for this week and the next 2 weeks through {`target_end_date_2wk_ahead`}.

- Reporting rate flag (only for hospital admissions target).

-	Contributing teams and models:
{`list of teams and models contributing hospital admission forecasts as hyperlinks to the sites provided in the metadata`}


## ED Visits

- The {`hub_name`} ensemble's one-week-ahead forecast predicts that the percentage of new weekly {`disease`} emergency department visits will be approximately {`percent of US ed visits from ensemble model, time horizon 2`} nationally, with {`lower 95% CI prediction for ensemble model`} to {`upper 95% CI prediction for ensemble model`} laboratory confirmed {`disease`} emergency department visits likely reported in the week ending {`week ending date for horizon 2 forecasts`}.

- This is compared to the {`last reported % ed visits`} visits reported for the week ending {`last reported target date`}, the most recent week of reporting from U.S. hospitals.

- Reported and forecasted new {`disease`} emergency department visits as of {`forecast_due_date`}.

- The figure shows the number of new laboratory-confirmed {`disease`} emergency department visits reported in the United States each week from {`first_ed_visits_target_data_date`} through {`last_ed_visits_target_data_date`} and forecasted new {`disease`} emergency department visits per week for this week and the next 2 weeks through {`target_end_date_2wk_ahead`}.

-	Contributing teams and models:
{`list of teams and models contributing emergency department visits forecasts as hyperlinks to the sites provided in the metadata`}
