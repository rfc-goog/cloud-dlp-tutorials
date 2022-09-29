# Cloud DLP - Structured Text Inspection
This script inspects a local CSV file for sensitive data using the
[Cloud DLP `inspect()`](https://cloud.google.com/dlp/docs/reference/rest/v2/projects.content/inspect)
method, as described in the [product documentation](https://cloud.google.com/dlp/docs/inspecting-structured-text#dlp-inspect-table-python).

This is a [_Content method_](https://cloud.google.com/dlp/docs/concepts-method-types#content-methods),
which means data is not persisted in Google Cloud.

## Disclaimer
This is not a Google product. 

This is just a sample intended to illustrate how to use Google Cloud Data 
Loss Prevention. Google won't maintain or support this code in any way. 
Use at your own discretion.



## Instructions

1. Edit [dlp_inspection_conf.py](dlp_inspection_conf.py) to your desired 
configuration. Relevant parameters:
   - Google Cloud project id you want to use 
   - The [Cloud DLP InfoTypes](https://cloud.google.com/dlp/docs/infotypes-reference) 
   you want to include in the inspection
   - Name of the CSV file you want to inspect
2. Install the Python dependencies with `pip install -r requirements.txt`
3. Make sure your [Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials)
are set correctly
4. Run the script with `python struct_content_inspect.py`

## Sample input
```
id,patient_name,patient_date_of_birth,date_of_service,provider_name,provider_location
1,Myles Branford,8/16/1953,9/24/1996,Mano Boggas,6 Westerfield Way
2,Bibby Hischke,2/11/2000,7/6/2011,Carmen Neeves,1 Tennessee Way
3,Corena Pietroni,8/26/1933,3/16/2021,Bradney Lightfoot,4 Comanche Point
4,Lorrie Reilingen,8/16/1995,10/29/2017,Horatia Visick,634 Fremont Crossing
5,Claudetta Cady,3/10/1999,12/7/2005,Burty Farrow,02 Summer Ridge Way
```

## Sample output
```
Quote: Myles Branford
Original column: patient_name
Row index: 0
Info type: PERSON_NAME
Likelihood: LIKELY
...
Quote: 8/16/1953
Original column: patient_date_of_birth
Row index: 0
Info type: DATE_OF_BIRTH
Likelihood: VERY_LIKELY

Quote: 8/16/1953
Original column: patient_date_of_birth
Row index: 0
Info type: DATE
Likelihood: LIKELY
...
Quote: Westerfield Way
Original column: provider_location
Row index: 0
Info type: LOCATION
Likelihood: POSSIBLE
...
Quote: 6 Westerfield Way
Original column: provider_location
Row index: 0
Info type: STREET_ADDRESS
Likelihood: LIKELY
```