# import openai
# from openai import OpenAI
# import os
# from config import apikey
# openai.api_key = apikey
#
#
# response = openai.completions.create(
#   model="gpt-3.5-turbo-1106",
#   messages=[
#     {
#       "role": "user",
#       "content": [
#         {
#           "type": "text",
#           "text": "write an apology letter to my girl friend \n"
#         }
#       ]
#     }
#   ],
#   temperature=1,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )

# from openai import OpenAI
# client = OpenAI()
# from config import apikey
# openapi.api_key = apikey
#
#
# response = client.chat.completions.create(
#   model="gpt-3.5-turbo-1106",
#   messages=[
#     {
#       "role": "user",
#       "content": [
#         {
#           "type": "text",
#           "text": "write an email to my boss for resignation"
#         }
#       ]
#     }
#   ],
#   temperature=1,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )

# import openai
# from config import apikey
#
# openai.api_key = apikey
# response=openai.Completion.create(
#     model="text-davinci-003",
#     prompt="write an email to my boss for resignation . ",
#     max_tokens=1024,
#     top_p=1,
#     temperature=0.5,
#     frequency_penalty=0,
#     presence_penalty=0
# )

# from openai import OpenAI
# from config import apikey
# client = OpenAI()
# openai.api_key = apikey
#
# response = client.chat.completions.create(
#   model="gpt-3.5-turbo-1106",
#   messages=[
#     {
#       "role": "user",
#       "content": [
#         {
#           "type": "text",
#           "text": "write an email to my boss for resignation"
#         }
#       ]
#     }
#   ],
#   temperature=1,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )

# import openai
# from config import apikey
#
# openai.api_key = apikey
# client = openai.OpenAI()
#
# response = client.chat.completions.create(
#   model="gpt-3.5-turbo-1106",
#   messages=[
#     {
#       "role": "user",
#       "content": [
#         {
#           "type": "text",
#           "text": "write an email to my boss for resignation"
#         }
#       ]
#     }
#   ],
#   temperature=1,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )

import openai
from config import apikey

openai.api_key = apikey

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {
      "role": "user",
      "content": "write an email to my boss for resignation"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)