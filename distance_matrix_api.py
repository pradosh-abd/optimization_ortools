base_url = "https://api.distancematrix.ai"
api_key = 'Your API here'
mode = 'driving'
traffic_model = 'best_guess'
def api_request(api_key,lat1,long1,lat2,long2,mode,traffic_model):
    url = "https://api.distancematrix.ai/maps/api/distancematrix/json" \
              "?origins={lat1},{long1}" \
              "&destinations={lat2},{long2}" \
              "&mode={mode}" \
              "&traffic_model={traffic_model}" \
              "&key={api_key}".format(base_url=base_url,api_key=api_key,
                lat1=lat1,long1=long1,lat2=lat2,long2=long2,mode=mode,traffic_model=traffic_model)
    result = requests.get(url)
    return result
