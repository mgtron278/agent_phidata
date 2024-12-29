from phi.agent import Agent
from phi.model.groq import Groq

from phi.tools.yfinance import YFinanceTools
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

#web search agent
web_search_agent = Agent(
    name  = "Web Search Agent" ,
    role = "Search the web for the information" ,
    model = OpenAIChat(id = "gpt-4o") ,
    tools = [DuckDuckGo()] ,
    instructions = ["Always Include Sources"] , 
    show_tools_calls = True ,
    markdown = True
)

#finance agent
finance_agent = Agent(
    name  = "Finance AI Agent" ,
    
    model = OpenAIChat(id = "gpt-4o") ,
    tools = [
        YFinanceTools(stock_price=True, analyst_recommendations= True, stock_fundamentals= True, company_news=True)
    ] ,
    instructions = ["Use tables to display data"] , 
    show_tools_calls = True ,
    markdown = True ,
    debug_mode= True
)

#Team leader

multi_ai_agent = Agent(
    team = [web_search_agent, finance_agent] ,
    instructions = ["Always Include Sources", "Use tables to display data"] , 
    show_tools_calls = True ,
    markdown = True
)

multi_ai_agent.print_response("Summarize analyst recommendation and share latest news on NVDA", stream = True)