'''
This works!! Wow.
'''


from EPCPyYes.core.v1_2.CBV import business_steps
from EPCPyYes.core.v1_2 import helpers

#import EPCPyYes.core.v1_2

from datetime import datetime
import requests
right_now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z") # Following ISO-8601


def create_epcs(start=1000, end=1002):
	'''
		Creates a range of sequential SGTIN URN values from:
			- company prefix
			- indicator index
			- item ref. number
 	'''

	company_prefix = '880002693'
	indicator_index = '1'
	ref_number = '555'

	# create a range for the number generation
	nums = range(start, end)
	# generate some URNS by passing in the company prefix, indicator, item refernce
	# number and a range of sequetial serial numbers.
	epcs = helpers.gtin_urn_generator(company_prefix, indicator_index, ref_number, nums)
	return epcs


def construct_sgln(location_reference, extension, direction='0'):
	'''
		Creates a sgln from a GLN.

		location_prefix is int and corresponds to bus/line/stop 101/102/103
	    and extension is as follows:

		Bus Line
    		urn:epc:id:sgln:880002693.101.{bus line number + direction}

		Bus Stop
    		urn:epc:id:sgln:880002693.102.{bus stop id}

		Bus Estimation
		    urn:epc:id:gsrn:880002693.103.{bus stop id}

	'''

	#destination_party = helpers.gln13_data_to_sgln_urn(company_prefix='880002693',
	#                                           location_reference='001')
	company_prefix = '880002693'
	extension = extension + direction


	# TODO: Figure out ID:s that work with the length of a sgln.
	if len(company_prefix + location_reference + extension) > 12:
		print(f'''The company prefix, location reference and extension variables
				 must total 12 digits in length when combined''')
		return None


	destination_location = helpers.gln13_data_to_sgln_urn(
												  company_prefix=company_prefix,
	                                              location_reference=location_reference,
	                                              extension=extension)
	#print(destination_party)
	#print(destination_location)
	return destination_location

# Print a constructed id of Bus Line with id 101 and
print(construct_sgln('10','2'))
#response = requests.post(url='http://localhost:8080/epcis/Service/EventCapture', data=xml).text
