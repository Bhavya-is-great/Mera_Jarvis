import openai

openai.api_key = "Openai_Api"


def ai_response(query):
    response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": query
    }
  ],
  temperature=1,
  max_tokens=1000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
    reply = response.choices[0].message.content
    return reply

while True:
    query = input("Enter your query:")
    if query == 'quit' or query == 'q':
       break
    elif query == "none":
        print("Continue")
    else:
       reply = ai_response(query)
       print(reply)