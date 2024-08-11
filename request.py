from openai import OpenAI
import os
import requests
import json

client = OpenAI(
  organization='org-tZQmKjHFNVsoxJDBXnNrTP6L',
  project='proj_cBTsydGjBpAcyqUZWooltSF0',
)

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say this is a test"}],
    max_tokens=50,
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")

