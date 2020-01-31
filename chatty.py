from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Simplebot and I'm a chatbot",]
    ],
    [
        r"how are you?",
        ["I'm doing good\nHow about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's ok, never mind",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program man\nSeriously I don't age",]
    ],
    [
        r"quit",
        ["Bye take care.", "It was nice talking to you, see you soon :)"]
    ]
]

def chatty():
    print("Hi, I'm Simplebot and I like to chat \nPlease type lowercase English to start a conversation. Type quit to leave")

    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatty()