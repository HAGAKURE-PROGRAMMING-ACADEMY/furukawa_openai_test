import os
import openai


openai.api_key = os.environ["openai_key"]

def openai_response(text):
  response = openai.Completion.create(
    engine="davinci",
    prompt=text,
    temperature=0.7,
    max_tokens=64,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return response["choices"][0]["text"]

if __name__ == '__main__':
  test_text = "葉隠れとはなにか？"
  print(openai_response(test_text))