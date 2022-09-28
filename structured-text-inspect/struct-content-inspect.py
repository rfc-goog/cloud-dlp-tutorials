### https://cloud.google.com/dlp/docs/inspecting-structured-text#dlp-inspect-table-python
# Import the client library
from cgi import test
import google.cloud.dlp
import csv
import dlp_inspection_conf as config

# Replace with the correct Google Cloud project id
project_id = "rubenfc-sandbox"
# Read sample data from CSV
file_name = "sample-data-10lines.csv"

with open(file_name, newline='') as csvfile:
	file_content = csv.reader(csvfile, delimiter=',', quotechar='"')
	csv_header = next(file_content)
	csv_rows = list(file_content)
	print("Header: {}".format(csv_header))
	print("CSV rows:") 
	for row in csv_rows:
		print(', '.join(row))
# Instantiate a client.
dlp_client = google.cloud.dlp_v2.DlpServiceClient()
# Build table content
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
min_likelihood = google.cloud.dlp_v2.Likelihood.LIKELIHOOD_UNSPECIFIED
# The maximum number of findings to report (0 = server maximum). Optional.
max_findings = 0
# Whether to include the matching string in the results. Optional.
include_quote = True
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
			print("Quote: {}".format(finding.quote))
		except AttributeError:
			pass
		for location in finding.location.content_locations:
			print("Original column: {}".format(location.record_location.field_id.name))
			print("Row index: {}".format(location.record_location.table_location.row_index))
		print("Info type: {}".format(finding.info_type.name))
		# Convert likelihood value to string respresentation.
		likelihood = finding.likelihood.name
		print("Likelihood: {}\n".format(likelihood))
else:
	print("No findings.")
#print(response)
