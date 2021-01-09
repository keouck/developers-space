def load_files():
    output = []
    files_to_read = ["reaction_roles.csv","help_text.txt"]
    for i in files_to_read:
        if i == "help_text.txt":
            with open(i) as f:
                output.append(f.read())
        else:
            with open(i) as f:
                output.append(f.read().split(","))

    return output