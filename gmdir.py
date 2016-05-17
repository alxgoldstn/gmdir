import googlemaps, sys
from datetime import datetime

def parse_dir(dir_req): #Takes in the result of gmaps directions() request, parses. Returns [start_address, end_address, dist, depart_time, direction_steps[] ]. (Check gm_request_sample.json to see datastructure).
    dir_dict = dir_req[0]["legs"][0]   #Now dir_dict points to 'routes-->legs-->{dict}` (as seen in gm_request_sample.json)
    
    # Get Start/End Address, Distance, Travel Time, Start Time
    start_addr = dir_dict["start_address"]
    end_addr = dir_dict["end_address"]
    total_dist = dir_dict["distance"]["text"]
    total_travel_time = dir_dict["duration"]["text"]
    start_time = dir_dict["departure_time"]["text"]

    # Get Directions.
    steps = []
    for step in dir_dict["steps"]: #Iterate over each dict in [steps]
        #LEFT OFF HERE. NEED TO ACCOUNT FOR VARIATION IN TRANSIT JSON DATA.
        steps.append( { "distance" : step["distance"]["text"],
                        "duration" : step["duration"]["text"],
                        "instruction" : step["html_instructions"],
                        "travel_mode" : step["travel_mode"] })
    return [start_addr,end_addr,total_dist,total_travel_time,start_time, steps]


gmdat = open("gmdir.dat", 'r') #gmdir.dat contains variable info for program to run

api_key = gmdat.readline()
start_addr = gmdat.readline()

api_key = api_key[:len(api_key)-1] #remove \n char at end
start_addr = start_addr[:len(start_addr)-1] #same

print("Starting Transit Direction!")
print("Testing readfile apikey and initial address:")
print("\t",api_key)
print("\t",start_addr)

dest_addr = "23439 Calvert Street, Woodland Hills, CA" #need to allow ui eventually

gmaps = googlemaps.Client(key=api_key)

# Get directions from gmaps client. Returns a lot of nested info.
dir_req = gmaps.directions(start_addr, dest_addr, mode="transit")
#dir_normalized = parse_dir(dir_req)


import pprint
pp = pprint.PrettyPrinter()
pp.pprint(dir_req)
