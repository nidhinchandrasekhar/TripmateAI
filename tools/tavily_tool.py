from tavily import TavilyClient
import os
from dotenv import load_dotenv


load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY")
                      )

def tavily_search(query: str):
    response = client.search(query=query,
                             max_results=5
                             )
    results=[]
    response_results = response.get("results") if isinstance(response, dict) else getattr(response, "results", [])

    for i,r in enumerate(response_results,1):
        title=r.get("title", "Unknown")
        url=r.get("url", "")
        snippet=r.get("snippet", "").strip()
        #keep only first 300 characters of snippet
        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ",1)[0] + "..."
        results.append(f"{i}.**{title}**\nURL: {url}\nSnippet: {snippet}\n")
    return "\n\n".join(results)

