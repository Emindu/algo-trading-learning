import nasdaqdatalink
'''
#1.return numpy data
data = nasdaqdatalink.get("CHRIS/CME_ES1", returns="numpy")

#2.define start and end date
data = nasdaqdatalink.get(
    "CHRIS/CME_ES1",
    start_date="2001-12-31",
    end_date="2005-12-31"
)

#3.define start and end date specific column
data = nasdaqdatalink.get(
    "CHRIS/CME_ES1.8",
    start_date="2001-12-31",
    end_date="2005-12-31"
)

#4.resampling data
data = nasdaqdatalink.get("CHRIS/CME_ES1",collapse="monthly")

print(data)
'''
#5.getting data from multiple contracts
contracts = ["CHRIS/CME_ES1.6",
             "CHRIS/CME_ES2.6",
             "CHRIS/CME_ES3.6",
             "CHRIS/CME_ES4.6"]
data = nasdaqdatalink.get(
        contracts,start_date="2015-01-01",
        end_date="2015-12-31"
)

data.iloc[0].plot(title=f"ES on {data.index[0]}")

