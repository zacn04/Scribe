import os
import openai

<<<<<<< HEAD
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("OPENAI_KEY")

#  ̶i̶n̶ ̶p̶r̶o̶g̶r̶e̶s̶s̶ complete!
#openai.organization = "org-WbwlG5hvut8bXxTOfEm4tfV6"
openai.api_key = key
# openai.Model.list()
model = "gpt-3.5-turbo-0613"

def explanation(prompt : str, answer : str) -> str:
  #This is going to explain the answer given by Wolfram Alpha, based off of the prompt.
  query = (f'I am going to give you a prompt that has been passed to Wolfram Alpha.\n'
           f'Your task is to explain the answer given by Wolfram Alpha, in followable steps, in natural language.\n'
            f'Do not invent math. Do not restate the answer without explanation of how to get there.\n'
  f'Why is {prompt} equivalent to {answer}? Be detailed, answer in less than 300 characters.\n')           
  #print()
  messages = [{'role': 'user', 'content' : query}]
  response = openai.ChatCompletion.create(model=model, messages=messages)
  #print(response)
  #print(type(response))
  return response["choices"][0]["message"]["content"]

# Testing 
if __name__ == "__main__":
  print(explanation('\\( \\int_{\\pi / 4}^{\\pi / 2} \\sin x d x \\)','1/sqrt(2)≈0.70711'))
  '''
  To find the exact value of the integral \( \int_{\pi / 4}^{\pi / 2} \sin x \, dx \), we need to evaluate the definite integral. Here are the detailed steps:

  Step 1: Start with the definite integral \( \int_{\pi / 4}^{\pi / 2} \sin x \, dx \).

  Step 2: Integrate \(\sin x\) with respect to \(x\). The antiderivative of \(\sin x\) is \(-\cos x\), so we have \(-\cos x\) as the indefinite integral.

  Step 3: Evaluate the definite integral by subtracting the antiderivative at the upper bound (\(\pi / 2\)) from the antiderivative at the lower bound (\(\pi / 4\)). 

  Step 4: Plugging in the values, we get \(-\cos(\pi / 2) - (-\cos(\pi / 4))\).

  Step 5: Simplify further. The cosine of \(\pi / 2\) is 0, and the cosine of \(\pi / 4\) is \(\sqrt{2}/2\). Therefore, we have \(0 - (-\sqrt{2}/2)\).

  Step 6: Simplify to obtain \(\sqrt{2}/2\).

  Step 7: Since \(\sqrt{2}/2\) is an irrational number, we can approximate it as \(0.70711\) using decimal notation.

  Therefore, the value of the integral \( \int_{\pi / 4}^{\pi / 2} \sin x \, dx \) is approximately equal to \(1/\sqrt{2} \approx 0.70711\).
  '''
=======
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
>>>>>>> 9125d73 (tys first commit)
