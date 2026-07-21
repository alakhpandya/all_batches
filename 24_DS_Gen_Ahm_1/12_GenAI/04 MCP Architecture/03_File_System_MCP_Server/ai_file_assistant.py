# New, more production-ready architecture
"""
               User
                │
                ▼
        Conversation Manager
                │
                ▼
        Prompt Constructor
                │
                ▼
            OpenRouter
                │
                ▼
        Tool Orchastrator
                │
      ┌─────────┴──────────┐
      ▼                    ▼
MCP Server              Cache Memory
      │                    │
      └─────────┬──────────┘
                ▼
        Final Response
"""


import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from openai import OpenAI
from dotenv import load_dotenv
import json
import os
from pprint import pprint

# ---------------- LLM Client ---------------- 

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)
