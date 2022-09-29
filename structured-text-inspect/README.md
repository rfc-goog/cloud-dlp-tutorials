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
2. Make sure your [Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials)
are set correctly