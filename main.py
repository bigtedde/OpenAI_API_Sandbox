# Ted Lawson 2/19/23

import os
import openai

with open('api_key.txt', 'r') as file:
    openai.api_key = file.read()

def main():
    prompt = "You: " + input("Start by typing in a question for your new friend...\n") + "\nFriend: "

    # Need a better exit clause. Works for now.
    while True:
        computer_response = reply(prompt)["choices"][0]["text"]
        print(f"Friend: {computer_response}")
        user_response = input("You: ")
        if user_response == "quit":
            exit()
        prompt += f"{computer_response}\nYou: {user_response}\nFriend: "

def reply(prompt: str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"You: {prompt}\n",
        temperature=.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"]
    )
    return response


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
