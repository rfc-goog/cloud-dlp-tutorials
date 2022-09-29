# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

"""Configuration for Cloud Data Loss Prevention inspection
"""
from google.cloud.dlp_v2 import Likelihood


# Google Cloud project id to use for the calls.
project_id = "<MY_PROJECT_ID>"

# Name of the local CSV file to inspect.
file_name = "sample-data-10lines.csv"

# List of DLP InfoTypes to look for in the inspect job.
infoTypeList = {
    "PERSON_NAME",
    "STREET_ADDRESS",
    "DATE",
    "DATE_OF_BIRTH",
    "LOCATION"
}

# Minimun likelihood to report.
min_likelihood = Likelihood.LIKELIHOOD_UNSPECIFIED

# Maximum number of findings to report (0 = server maximum). Optional.
max_findings = 0

# Whether to include the matching string in the results. Optional.
include_quote = True

