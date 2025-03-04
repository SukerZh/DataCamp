# Engineering Machinery Data File Description
## Overview
This document describes the structure and contents of an engineering machinery data file that integrates both input and output datasets. The file is designed to capture key metrics related to engineering machinery work hours at the city level and aggregate economic indicators at the province level. The time span covers the period from January 2020 to August 2023 for the input data and from 2020 to 2023 for the output data.

## Input Data
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
