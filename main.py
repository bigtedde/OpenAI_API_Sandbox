# Ted Lawson 2/19/23

import openai
import FriendChat

with open('api_key.txt', 'r') as file:
    openai.api_key = file.read()

def main():
    # Begins a chat between you and an AI friend
    # Pass in 'your name' and 'friend name' for a little personalization.
    FriendChat.FriendChat().start_chat()


if __name__ == '__main__':
    main()

