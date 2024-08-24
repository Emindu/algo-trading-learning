import nasdaqdatalink

#nasdaqdatalink.ApiConfig.api_key = "your_api_key"


data = nasdaqdatalink.get("CHRIS/CME_ES1")
print(data)
