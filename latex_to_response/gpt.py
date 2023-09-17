import os
import openai

# in progress

key = "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"
openai.organization = "org-WbwlG5hvut8bXxTOfEm4tfV6"
openai.api_key = os.getenv(key)
# openai.Model.list()
model = "gpt-3.5-turbo-0613"

def explanation(prompt, answer):
  #This is going to explain the answer given by Wolfram Alpha, based off of the prompt.
  query = (f'I am going to give you a prompt that has been passed to Wolfram Alpha. Your task is to explain the answer given by Wolfram Alpha. Do not invent math.\n'
  f'Why is {prompt} equivalent to {answer}? Be concise, answer in less than 300 characters.\n')           
  #print()
  response = openai.Completion.create(model=model, prompt=query)
  #print(response)
  #print(type(response))
  return response

# Testing 

print(explanation())
