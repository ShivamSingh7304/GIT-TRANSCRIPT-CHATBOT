from rag import ask_question


def main():

    print("Youtube Transcript Chatbot")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("Ask: ")

        if question.lower() == "exit":
            break

        print()
        print(ask_question(question))
        print()


if __name__ == "__main__":
    main()


