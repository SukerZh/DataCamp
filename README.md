# RAMP starting-kit Engineering Machinery economic forecast based on machinery data Data File Description

Authors: Shun Ye CHEN, Wenbo DUAN, Louis NEL, Baoyue ZHANG

## Input Data Structure
### Data Source
  Scope: The input dataset contains data for three primary types of engineering machinery:
    Roller
    Crane
    Excavator
### Data Content
  Metric: For each machinery type, the data represents the total work hours index.
    Granularity: The data is collected at the city level across various cities in China.
    Time Period: 01/01/2020 to 31/08/2023.
    Usage: These metrics are used to assess the operational intensity and performance of each type of machinery over time across different urban areas.
### File Structure
  Columns/Values:
    Province: The name or identifier of the province.
    City: The name or identifier of the city.
    Date: Daily timestamps ranging from January 2020 to August 2023.
    Work_Hours_Index: Total work hours index for machinery.
  Format: 
    Data is expected to be organized in a tabular format where each row represents a unique city and date combination.

## Output Data
###  Data Source
The output dataset provides economic indicators aggregated at the provincial level, which allows for a broader macroeconomic analysis compared to the city-level input data.

### Data Content
  IndustrialVA_YonY
    Description: This field contains the month-over-month year-on-year data for industrial added value.
    Time Period: Covers the period from 2020 to 2023.
    Granularity: Province-level data.
    Usage: Helps in tracking the industrial growth and performance on a month-to-month basis, comparing the same month across different years.
    
  ConstructionTotalValueOutput
    Description: Represents the added value in the construction industry.
    Time Period: Data spans from the first quarter (Q1) of 2020 to the fourth quarter (Q4) of 2023.
    Granularity: Province-level data.
    Usage: Used to evaluate the performance and growth trends within the construction sector over quarterly intervals.
  
  GrossDomesticProduct
    Description: Contains the quarterly GDP data.
    Time Period: From Q1 2020 to Q4 2023.
    Granularity: Province-level data.
    Usage: Provides a broad measure of economic performance, reflecting overall economic health at the provincial level.

## Integration and Usage
  Data Mapping: The engineering machinery input data (city-level) can be aggregated to analyze correlations with the provincial-level economic indicators in the output data.
  Analytical Purpose: This integrated dataset is designed to facilitate analyses such as:
    Evaluating the impact of machinery utilization on regional economic performance.
    Comparing industrial and construction growth trends across provinces.
    Assessing the overall contribution of engineering activities to the provincial GDP.


### File Structure
  Columns/Fields:
    Province: The name or identifier of the province.
    Time Period: Monthly (for IndustrialVA_YonY) and Quarterly (for ConstructionTotalValueOutput and GrossDomesticProduct) time stamps.

## Data Quality Considerations
  Time Alignment: Ensure proper alignment of dates when aggregating city-level input data to match the monthly or quarterly output data.
  Data Consistency: Validate consistency in city-to-province mappings and ensure that economic indicators accurately reflect the corresponding provinces.
  Missing Data: Identify and address any gaps in the time series to maintain the integrity of longitudinal analyses.

## Getting started

### Install

To run a submission and the notebook you will need the dependencies listed
in `requirements.txt`. You can install install the dependencies with the
following command-line:

```bash
pip install -U -r requirements.txt
```

If you are using `conda`, we provide an `environment.yml` file for similar
usage.

### Challenge description

Get started on this RAMP with the
[dedicated notebook](template_starting_kit.ipynb).

### Test a submission

The submissions need to be located in the `submissions` folder. For instance
for `my_submission`, it should be located in `submissions/my_submission`.

To run a specific submission, you can use the `ramp-test` command line:

```bash
ramp-test --submission my_submission
```

You can get more information regarding this command line:

```bash
ramp-test --help
```

### To go further

You can find more information regarding `ramp-workflow` in the
[dedicated documentation](https://paris-saclay-cds.github.io/ramp-docs/ramp-workflow/stable/using_kits.html)



