# import openai

# openai.api_key = "key_here"

# def get_response(input):
#     response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt=input
# )
#     return response['choices'][0]['text']

# if __name__ == "__main__":
#         print("Hello, I am Mya, your personal assistant. How can I help you?")
#         while True:
#             user_input = input("user: ")
#             if user_input == "exit":
#                 break
#             response = get_response(user_input)
#             print(response)