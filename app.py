import subprocess
import sys

from commiter import commit_msg
from optimizer import optimize
from reviewer import review


def git_commit(file_name):
    try:
        if file_name == ".":
            subprocess.run(["git", "add", "."], check=True)
        else:
            subprocess.run(["git", "add", file_name], check=True)
        
        message = commit_msg(file_name)
        subprocess.run(["git", "commit", "-m", message], check=True)
        print("Git commit successful.")

        choice = input("Do you want to commit changes? (y/n)")
        new_file = open()

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Git commit failed.")


# def git_push():
#     try:
#         subprocess.run(["git", "push"], check=True)
#         print("Git Push Successfull.")
#     except subprocess.CalledProcessError as e:
#         print(f"Error: {e}")
#         print("Git commit failed.")


def main():
    filename = sys.argv[1]

    if '-r' in sys.argv:
        print(review(filename))

    if '-o' in sys.argv:
        print(optimize(filename))
    
    if '-c' in sys.argv:
        git_commit(filename)

    else:
        print('No Arguments added! Try Again!')


    # git_commit(filename)
    # print(optimize(filename))

if __name__ == "__main__":
    main()