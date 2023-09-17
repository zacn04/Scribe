import os
import openai

# in progress

key = "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"
openai.organization = "org-WbwlG5hvut8bXxTOfEm4tfV6"
openai.api_key = os.getenv(key)
# openai.Model.list()
model = "gpt-3.5-turbo-0613"
query = "I'm so"

print()
response = openai.Completion.create(model=model, prompt=query)
print(response)
print(type(response))