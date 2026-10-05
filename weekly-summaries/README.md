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
* `horizon` (numeric): time horizon for the forecast (Ex: 2)
* `model` (string): the ensemble model name (Ex: CovidHub-ensemble)
* `rate_quantile_0.025` (numeric): 0.025 quantile forecast value as a rate per 100k, not calculated for proportion ED visits target (Ex: 1.12777351608532, NA)
* `rate_quantile_0.5` (numeric): 0.5 quantile forecast value as a rate per 100k, not calculated for proportion ED visits target
* `rate_quantile_0.975` (numeric): 0.975 quantile forecast value as a rate per 100k, not calculated for proportion ED visits target
* `count_quantile_0.025` (numeric): 0.025 quantile forecast value (Ex: 3754.07763671875)
* `count_quantile_0.5` (numeric): 0.5 quantile forecast value
* `count_quantile_0.975` (numeric): 0.975 quantile forecast value
* `rate_quantile_0.025_rounded` (numeric): forecasted value as a rate per 100k, rounded to 2 places (Ex: 3.57). Not calculated for proportion ED visits target
* `rate_quantile_0.5_rounded` (numeric): forecasted value as a rate per 100k, rounded to 2 places. Not calculated for proportion ED visits target
* `rate_quantile_0.975_rounded` (numeric): forecasted value as a rate per 100k, rounded to 2 places. Not calculated for proportion ED visits target
* `count_quantile_0.025_rounded` (numeric): Rounded 0.025 quantile forecast value (see [Rounding Rules](#rounding-rules) for details)
* `count_quantile_0.5_rounded` (numeric): Rounded 0.5 quantile forecast value (see [Rounding Rules](#rounding-rules) for details)
* `count_quantile_0.975_rounded` (numeric): Rounded 0.975 quantile forecast value (see [Rounding Rules](#rounding-rules) for details)
* `target` (string): description of forecast target date (Ex: wk inc covid/rsv hosp, or wk inc covid/rsv prop ed visits)
* `target_data_type` (string): type of target (Ex: `hosp` (Hospital admissions) or `prop_ed` (Proportion of Emergency department visits) without the disease string)
* `target_end_date` (date): target date for the forecast (Ex: 2024-11-30)
* `reference_date` (date): date that the forecast was generated (Ex: 2024-11-23)
* `forecast_due_date` (date): date forecasts were due for this reference date (Ex: 2024-11-20)
* `target_end_date_formatted` (string): target date for the forecast, prettily re-formatted as a string (Ex: “November 30, 2024”)
* `forecast_due_date_formatted` (string): forecast due date, prettily re-formatted as a string (Ex: “November 20, 2024”)
* `reference_date_formatted` (string): date that the forecast was generated, prettily re-formatted as a string (Ex: “November 23, 2024”)

__Timeseries Component__ (`YYYY-MM-DD_{disease}_forecasts_data.csv`):

_Contains all the available COVID or RSV models submitted in a given week for all states (including US, DC and Puerto Rico)._

* `location_name` (string): full state name for the forecast. Note: US is spelled out in this version (Ex: Alabama, United States)
* `abbreviation` (string): abbreviated state name (Ex: AL)
* `horizon` (numeric): time horizon for the forecast. Currently using time horizons 0, 1, 2, 3 (Ex: 2)
* `forecast_date` (date): date that forecast was generated (Ex: 2024-11-23)
* `target_end_date` (date): target date for forecast (Ex: 2024-11-30)
* `target` (string): description of forecast target  (Ex: wk inc covid/rsv hosp, or wk inc covid/rsv prop ed visits)
* `target_data_type` (string): type of target (Ex: `hosp` (Hospital admissions) or `prop_ed` (Proportion of Emergency department visits) without the disease string)
* `model` (string): name of the model, pulled from the folder names in the model-output section of the forecast repos (Ex: FluSight-ensemble, CEPH-Rtrend_fluH)
* `count_quantile_0.025` (numeric): 0.025 quantile forecast value (Ex: 922.475)
* `count_quantile_0.10` (numeric): 0.10 quantile forecast value
* `count_quantile_0.25` (numeric): 0.25 quantile forecast value
* `count_quantile_0.5` (numeric): 0.5 quantile forecast value
* `count_quantile_0.75` (numeric): 0.75 quantile forecast value
* `count_quantile_0.90` (numeric): 0.90 quantile forecast value
* `count_quantile_0.975` (numeric): 0.975 quantile forecast value
* `count_quantile_0.025_rounded` (numeric): Rounded 0.025 quantile forecast value (see [Rounding Rules](#rounding-rules) for details)
* `count_quantile_0.10_rounded` (numeric): Rounded 0.10 quantile forecast value
* `count_quantile_0.25_rounded` (numeric): Rounded 0.25 quantile forecast value (see [Rounding Rules](#rounding-rules) for details)
* `count_quantile_0.5_rounded` (numeric): Rounded 0.5 quantile forecast value (see [Rounding Rules](#rounding-rules) for details)
* `count_quantile_0.75_rounded` (numeric): Rounded 0.75 quantile forecast value (see [Rounding Rules](#rounding-rules) for details)
* `count_quantile_0.90_rounded` (numeric): Rounded 0.90 quantile forecast value
* `count_quantile_0.975_rounded` (numeric): Rounded 0.975 quantile forecast value (see [Rounding Rules](#rounding-rules) for details)
* `rate_quantile_0.025` (numeric): 0.025 quantile forecast value as a rate per 100k, not calculated for proportion ED visits target (Ex: 0.27632, NA)
* `rate_quantile_0.10` (numeric): 0.10 quantile forecast value as a rate per 100k, not calculated for proportion ED visits target
* `rate_quantile_0.25` (numeric): 0.25 quantile forecast value as a rate per 100k, not calculated for proportion ED visits target
* `rate_quantile_0.5` (numeric): 0.5 quantile forecast value as a rate per 100k, not calculated for proportion ED visits target
* `rate_quantile_0.75` (numeric): 0.75 quantile forecast value as a rate per 100k, not calculated for proportion ED visits target
* `rate_quantile_0.90` (numeric): 0.90 quantile forecast value as a rate per 100k, not calculated for proportion ED visits target
* `rate_quantile_0.975` (numeric): 0.975 quantile forecast value as a rate per 100k, not calculated for proportion ED visits target
* `rate_quantile_0.025_rounded` (numeric): Rounded 0.025 quantile rate per 100k (see [Rounding Rules](#rounding-rules) for details). Not calculated for proportion ED visits target
* `rate_quantile_0.10_rounded` (numeric): Rounded 0.10 quantile rate per 100k. Not calculated for proportion ED visits target
* `rate_quantile_0.25_rounded` (numeric): Rounded 0.25 quantile rate per 100k. Not calculated for proportion ED visits target
* `rate_quantile_0.5_rounded` (numeric): Rounded 0.5 quantile rate per 100k. Not calculated for proportion ED visits target
* `rate_quantile_0.75_rounded` (numeric): Rounded 0.75 quantile rate per 100k. Not calculated for proportion ED visits target
* `rate_quantile_0.90_rounded` (numeric): Rounded 0.90 quantile rate per 100k. Not calculated for proportion ED visits target
* `rate_quantile_0.975_rounded` (numeric): Rounded 0.975 quantile rate per 100k. Not calculated for proportion ED visits target
* `designated_model` (bool): True if model is included in the hub ensemble
* `ensemble_of_hub_models` (bool):  True if the model is an ensemble of models submitted to the hub
* `forecast_team` (string): name of the team that generated the model; pulled from model metadata (Ex: CEPH Lab at Indiana University)
* `forecast_due_date` (date): date forecasts were due for this reference date (Ex: 2024-11-20)
* `model_full_name` (string): full name of the model; pulled from model metadata (Ex: Rtrend COVID)

__Truth Data__ (`YYYY-MM-DD_{disease}_target_data.csv`)

_Contains the most recent observed COVID or RSV hospitalization and proportion of ED visits data for all states (including US, DC and Puerto Rico) but not including the remainder of the territories._

* `week_ending_date` (date): week ending date of observed data per row (Ex: 2024-11-16)
* `location` (string): two-digit FIPS code associated with each state (Ex: 06)
* `location_name` (string): spelled out state name (note: US is spelled out) (Ex: California, United States)
* `target` (string): description of the truth data target (Ex: "wk inc disease hosp")
* `target_data_type` (string): type of target (Ex: `hosp` (Hospital admissions) or `prop_ed` (Proportion of Emergency department visits) without the disease string)
* `value` (numeric): number of hospital admissions or proportion of ED visits; Hospital admissions should be an integer (Ex: 3); proportion of ED visits should be of form 0.**


## Quantile Column Units

Quantile columns are prefixed by the units they carry:

- `count_*`: the forecast value as submitted to the hub.
- `rate_*`: the same forecast expressed per 100,000 population.

`rate_*` is computed as `count_* / population * 100000`, using 2023 census population estimates (`hubhelpr::population_data`). Please use these columns rather than recomputing rates, so that displayed values reconcile with the map component.

N.B.:

- For `prop_ed` (proportion of ED visits) targets, `count_*` holds a proportion, not a count (Ex: 0.00193). The `count_` prefix is used for schema consistency across targets; `target_data_type` is the indicator of units.
- `rate_*` is `NA` for `prop_ed` targets, which have no per-100k interpretation.

## Rounding Rules

For `count_**_rounded` values, different rounding rules apply based on data type and value:

- **Hospital count data**:
  - values > 1000: rounded to nearest hundreds
  - 10 < values < 1000: rounded to nearest tens
  - values < 10: rounded to nearest integer
- **ED visits proportion data**: rounded to 2 significant figures

For `rate_**_rounded` values:

- **Hospital rate data**: rounded to 2 decimal places
- **ED visits proportion data**: not calculated (`NA`)
