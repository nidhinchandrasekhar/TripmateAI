from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights    


#res=tavily_search("Best places to visit in Europe")

res=search_flights("Plan a 7 day Nepal trip from Bangladesh")
print(res)