from openai import OpenAI

def review(file_name):
    file_path = file_name
    # file_path = "test.py"

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
                "content": "You are a code review assistant, skilled in explaining complex programming concepts, refactoring code to optimize it and also check for logical and syntactical errors",
            },
            {
                "role": "user",
                "content": f"State all the potential issues possible from the following code, if not state the time complexity: \n{file_data}",
            },
        ],
    )

    return completion.choices[0].message.content
