from phi.agent import Agent
from phi.model.groq import Groq

from phi.tools.yfinance import YFinanceTools

from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

#web search agent
web_search_agent = Agent(
    name  = "Web Search Agent" ,
    role = "Search the web for the information" ,
    model = Groq(id = "llama-3.3-70b-versatile") ,
    tools = [DuckDuckGo()] ,
    instructions = ["Always Include Sources"] , 
    show_tools_calls = True ,
    markdown = True
)


def get_company_symbol(company :str) -> str:

    symbols = {
        "Phidata" : "MSFT",
        "Infosys" : "INFY", 
        "Tesla"  : "TSLA" ,
        "Apple"   : "AAPL" ,
        "Microsoft" : "MSFT" ,
        "Amazon"   : "AMZN",
    }
    return symbols.get(company, "Unknown")
agent = Agent(
    name  = "Finance AI Agent" ,
    
    model = Groq(id = "llama-3.3-70b-versatile") ,
    tools = [
        YFinanceTools(stock_price=True, analyst_recommendations= True, stock_fundamentals= True, company_news=True), get_company_symbol
    ] ,
    instructions = ["Use tables to display data",
                    "if you dont know the company symbol, please use get_company_symbol tool, even if its not a public company"] , 
    show_tools_calls = True ,
    markdown = True ,
    debug_mode= True
)

#combination

#multi_ai_agent = Agent(
#    team = [web_search_agent, finance_agent] ,
#    instructions = ["Always Include Sources", "Use tables to display data"] , 
#    show_tools_calls = True ,
#    markdown = True
#)

agent.print_response("Summarize and compare analyst recommendation and fundamentals for TSLA and Phidata", stream = True)