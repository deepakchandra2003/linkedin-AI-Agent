from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.yfinance import YfinaceTools 
from phi.tools.duckduckgo import DuckDuckGo


web_search_agent=Agent(
    name="Web earch Agent",
    role="Search the web for the information",
    model="
)