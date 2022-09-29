# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

"""Cloud Data Loss Prevention inspection for tabular data

This script invokes Cloud DLP's inspection on structured data read from a CSV
file, as described in
https://cloud.google.com/dlp/docs/inspecting-structured-text#dlp-inspect-table-python

Usage: Before running this script:
1. Edit file dlp_inspection_conf with the desired configuration values.
2. Make sure your default application credentials are set correctly, e.g.
by running `gcloud auth application-default login`.
"""

import google.cloud.dlp
import csv
# Local config file.
import dlp_inspection_conf as config

# Replace with the correct Google Cloud project id.
project_id = config.project_id

# Read sample data from CSV.
file_name = config.file_name
with open(file_name, encoding="utf-8", newline="") as csvfile:
  file_content = csv.reader(csvfile, delimiter=",", quotechar='"')
  csv_header = next(file_content)
  csv_rows = list(file_content)

  print(f"Header: {csv_header}")
  print("CSV rows:")
  for row in csv_rows:
    print(", ".join(row))

# Instantiate a client.
dlp_client = google.cloud.dlp_v2.DlpServiceClient()
# Build table content.
headers = [{"name": val} for val in csv_header]
rows = []
for row in csv_rows:
  rows.append({"values": [{"string_value": cell_val} for cell_val in row]})

table = {}
table["headers"] = headers
table["rows"] = rows
item = {"table": table}

# The info types to search for in the content. Required.
info_types = [{"name": type} for type in config.infoTypeList]
# info_types = [
# 	{"name": "PERSON_NAME"},
# 	{"name": "STREET_ADDRESS"},
# 	{"name": "DATE"},
# 	{"name": "DATE_OF_BIRTH"}
# ]

# The minimum likelihood to constitute a match. Optional.
min_likelihood = config.min_likelihood
# The maximum number of findings to report (0 = server maximum). Optional.
max_findings = config.max_findings
# Whether to include the matching string in the results. Optional.
include_quote = config.include_quote

# Convert the project id into a full resource id.
parent = f"projects/{project_id}"
# Construct the configuration dictionary. Keys which are None may
# optionally be omitted entirely.
inspect_config = {
	"info_types": info_types,
	"min_likelihood": min_likelihood,
	"include_quote": include_quote,
	"limits": {"max_findings_per_request": max_findings},
}

# Call the API.
response = dlp_client.inspect_content(
	request={"parent": parent, "inspect_config": inspect_config, "item": item}
)
# Print out the results.
if response.result.findings:
  for finding in response.result.findings:
    try:
      print(f"Quote: {finding.quote}")
    except AttributeError:
      pass
    for location in finding.location.content_locations:
      print(f"Original column: {location.record_location.field_id.name}")
      print(f"Row index: {location.record_location.table_location.row_index}")

    print(f"Info type: {finding.info_type.name}")
		# Convert likelihood value to string respresentation.
    likelihood = finding.likelihood.name
    print(f"Likelihood: {likelihood}\n")
else:
  print("No findings.")
