from openai import OpenAI

def optimize(file_name):
# file_path = "test.py"
    file_path = file_name

    try:
        with open(file_path, "r") as file:
            file_data = file.read()  # Read the entire file into a string

    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")

    except Exception as e:
        print(f"An error occurred: {e}")


    client = OpenAI()


    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a code assistant, skilled with complex programming concepts, analyze and optimize the code and give ONLY the new version of the optimized code",
            },
            {
                "role": "user",
                "content": f"write an optimized code with suitable and professional comments for the given file: \n{file_data}",
            },
        ],
    )

    return completion.choices[0].message.content
