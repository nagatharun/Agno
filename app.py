from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.tavily import TavilyTools


import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["TAVILY_SEARCH_API_KEY"] = os.getenv("TAVILY_SEARCH_API_KEY")



agent = Agent(
    #model= OpenAIChat(id="qwen-2.5-32b") # Here "id" is the any Model name ,  

    model= Groq(id="qwen-2.5-32b"), # Here "id" is the any Model name  


    description="Hey, you are Voice Assistant, please give the responses based on the user queries",
    tools = [DuckDuckGoTools()],
    #tools = [TavilyTools(api_key= "provide your TAVILY SEARCH API KEY HERE" )] also try this with your API key of tavily serach,
    markdown=True
)

agent.print_response("please tell me about the cricket, who won the recent CT 2025 Final and also tell me who is the god of cricket",stream=True)


