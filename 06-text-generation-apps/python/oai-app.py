import re
from openai import OpenAI
import openai
import os
from dotenv import load_dotenv
from loguru import logger

# load environment variables from .env file
load_dotenv()

# configure OpenAI service client 
client = OpenAI()
# deployment = "gpt-3.5-turbo"
deployment = "deepseek-chat"

# add your completion code
no_recipes = input("菜谱数量(例如:5):")
ingredients = input("食材列表(例如，鸡肉、土豆、胡萝卜):")
filter = input("是否过滤掉某些食材(例如，鸡肉、 胡萝卜):")
prompt = f"向我展示用以下食材做一道菜的{no_recipes}个食谱：{ingredients}。每个食谱列出所有使用的材料。如果过滤条件'{filter}'不是空的, 确保食谱中不包含过滤条件中的食材。"
messages = [{"role": "user", "content": prompt}]  

logger.info(f"Prompt: {prompt}")
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)

recipes = completion.choices[0].message.content

logger.info(f"Recipes: {recipes}")

prompt_shopping = f"{recipes}\n为以上生成的食谱制作一个购物清单，请不要包括我已经拥有的材料。"
messages = [{"role": "user", "content": prompt_shopping}]

logger.info(f"Prompt: {prompt_shopping}")
completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=1200)

shopping_list = completion.choices[0].message.content

logger.info(f"Shopping List: {shopping_list}")
#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.
