from hugchat import hugchat
from hugchat.login import Login

def commit_msg(file_name):
    sign = Login("mudassiria", "3012D@z@!")
    cookies = sign.login()

    cookie_path_dir = "./cookies_snapshot"
    sign.saveCookiesToDir(cookie_path_dir)

    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    # file_path = "test.py"  # Specify the path to your file
    file_path = file_name  # Specify the path to your file

    try:
        with open(file_path, "r") as file:
            file_data = file.read()  # Read the entire file into a string

    except FileNotFoundError:
        return f"The file '{file_path}' was not found."

    except Exception as e:
        return f"An error occurred: {e}"

    str1 = (
        f"generate a commit message in 100 characters for the following code: {file_data}"
    )
    # str1 = f"what is your LLM?"
    output = str(chatbot.chat(str1))
    final = output.split("\n")[0].lstrip().split("(")[0]

    return final
