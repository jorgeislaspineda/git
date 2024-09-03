from newsdataapi import NewsDataApiClient

# API key authorization, Initialize the client with your API key

api = NewsDataApiClient(apikey="pub_51549188c296f31835149e6c98a436e2b6cdb")

# You can pass empty or with request parameters {ex. (country = "mx")}

response = api.news_api(q="judicial", country="mx", category="politics")

print (response)