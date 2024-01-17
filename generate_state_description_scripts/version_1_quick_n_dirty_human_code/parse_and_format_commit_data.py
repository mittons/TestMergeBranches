import itertools

COMMIT_DATA_KEY = "COMMIT_DATA"
COMMIT_ID_KEY = "COMMIT_ID"
COMMIT_HEADER_TEXT_KEY = "COMMIT_HEADER_TEXT"
COMMIT_STATE_KEY = "COMMIT_STATE"
COMMIT_BRANCH_KEY = "COMMIT_BRANCH"
COMMIT_STATE_DATA_TYPE_KEY = "COMMIT_STATE_DATA_TYPE"

def parse_and_format_commit_data(lines):
    repo_states_by_commit = []
    current_commit_data = {}
    init = True
    current_branch_name = ""
    current_commit_header_text = ""

    for line in lines:
        if line.startswith('### '):
            # Extracting commit identifier
            if(init == True):
                init = False
            else:
                repo_states_by_commit.append(current_commit_data)
                current_commit_data = {}

            # Add commit text
                # This inside a conditional statement that guarantess the line starts with '### '. 
                # - We remove those 4 characters because we dont want them now and we can add them later
            current_commit_header_text = line[4:].strip()

            # Add commit id
            current_commit_id = line.strip().split(' ')[2]

        if '**main**' in line:
            # Extracting branch name ('main' or 'staging')
            current_branch_name = 'main'
        elif '**staging**' in line:
            # Extracting branch name ('main' or 'staging')
            current_branch_name = 'staging'
        elif 'History:' in line or 'Data:' in line:
            # Extracting branch state information
            branch_data_type, state_type = line.strip().split(':')
            state = state_type.strip().strip('`').strip('_').strip('`')

            # Further refining branch_data_type
            branch_data_type = f"{branch_data_type.strip('- ')}"


            current_commit_data[COMMIT_HEADER_TEXT_KEY] = current_commit_header_text
            current_commit_data[COMMIT_ID_KEY] = current_commit_id

            if (not current_branch_name in current_commit_data):
                current_commit_data[current_branch_name] = {}

            current_commit_data[current_branch_name][branch_data_type] = ""
            current_commit_data[current_branch_name][branch_data_type] = state
            

    repo_states_by_commit.append(current_commit_data)

    #print("\n".join(map(str, repo_states_by_commit)))
    return repo_states_by_commit


import re

def extract_state_and_context(state_string):
    # Remove any occurents of parenthesis opening any everytihng after that.
    state_string_fixed = state_string.split("(")[0]
    
    # Regular expression to find uppercase letters and optional context in parentheses
    pattern = r'([A-Z])(?: \(([^)]+)\))?'
    matches = re.findall(pattern, state_string_fixed)

    letters = [match[0] for match in matches]
    context = [match[1] for match in matches if match[1]]

    return letters, context



# Expand lists to have be alphabetically sorted (ASCENDING) and
#   have a single " " whitesipce element in the location of every 
#        missing uppercase alphabet character from A up until the higest value letter in the input list.
#   Input example01
#       ['A', 'D', 'E', 'G']
#   Output example01
#       ['A', ' ', ' ', 'D', 'E', ' ', 'G']
def expand_letter_list_with_spaces(letter_list_in):
    letter_list_expanded = []
    letters_found = 0
    for letter_code in range(ord('A'), ord('P')):
        letter = chr(letter_code)
        letter_list_expanded.append(letter if letter in letter_list_in else " ")
        if letter in letter_list_in:
            letters_found += 1
            if letters_found == len(letter_list_in):
                break
    
    if (letters_found == 0):
        return []

    return letter_list_expanded


def shitty_generate_branch_interaction_data(commit_id, staging_data, main_history):
    # print(main_history)
    # print(commit_id)
    # print(len(staging_data))
    if (len(staging_data) == 0):
        return []
    if ord(commit_id) <= ord('G') and 'G' not in main_history:
        return ["|"]
    elif ord(commit_id) <= ord('N') and 'N' not in main_history:
        return ["|", " ", " ", " ", " ", " ", "|"]
    elif ord(commit_id) <= ord('O') and 'O' not in main_history:
        return ["|", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", "|"]
    else:
        return ["|", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", " ", " ", "|", "|"]


def format_repo_states(repo_states):

    last_valid_commit_id = 'A'

    for commit_data in repo_states:
        commit_id = commit_data.get(COMMIT_ID_KEY, "Unknown Commit")
        if len(commit_id) != 1:
            commit_id = last_valid_commit_id
        else:
            last_valid_commit_id = commit_id

        commit_header_text = commit_data.get(COMMIT_HEADER_TEXT_KEY, "")



        # Extracting and formatting for 'main' branch
        main_data = commit_data['main']['Data']
        main_history = commit_data['main']['History']
        main_data_letters, main_data_context = extract_state_and_context(main_data)
        main_history_letters, main_history_context = extract_state_and_context(main_history)


        # Extracting and formatting for 'staging' branch
        staging_data = commit_data['staging']['Data']
        staging_history = commit_data['staging']['History']
        staging_data_letters, staging_data_context = extract_state_and_context(staging_data)
        staging_history_letters, staging_history_context = extract_state_and_context(staging_history)

        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # | ^^^ | TODO LOOK AT THE DATA WE ARE GETTING IN  [staging_data_context] and [staging_history_context] | ^^^ |
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

        # Expand lists to have be alphabetically sorted (ASCENDING) and
        #   have a single " " whitesipce element in the location of every 
        #        missing uppercase alphabet character from A up until the higest value letter in the input list.
        #   Input example01
        #       ['A', 'D', 'E', 'G']
        #   Output example01
        #       ['A', ' ', ' ', 'D', 'E', ' ', 'G']
        main_data_letters_expanded = expand_letter_list_with_spaces(main_data_letters)
        main_history_letters_expanded = expand_letter_list_with_spaces(main_history_letters)
        staging_history_letters_expanded = expand_letter_list_with_spaces(staging_history_letters)
        staging_data_letters_expanded = expand_letter_list_with_spaces(staging_data_letters)


        branch_interaction_data = shitty_generate_branch_interaction_data(commit_id, staging_data_letters_expanded, main_data_letters_expanded)

        test_printing_cotroller(commit_header_text, main_data_letters_expanded, main_history_letters_expanded, staging_history_letters_expanded, staging_data_letters_expanded, branch_interaction_data)


def format_data_state_list_string(input_list):
    output_list = [' | '.join(g) if k else '   '.join(g) for k, g in itertools.groupby(input_list, key=lambda x: x != ' ')]
    return ' | '.join(output_list)

def test_printing_cotroller(commit_header_text, main_data, main_history, staging_history, staging_data, branch_interaction_data):
    print_readme_md_formatted(commit_header_text, main_data, main_history, staging_history, staging_data, branch_interaction_data)
    #print_only_header(commit_header_text, main_data, main_history, staging_history, staging_data, branch_interaction_data)

def print_basic(commit_header_text, main_data, main_history, staging_history, staging_data, branch_interaction_data):
    print(commit_header_text)

    splitter_arr = ["-" for c in staging_history]

    print(f"main    (Data):    ", format_data_state_list_string(main_data))
    print(f"------------------", '-' + '---'.join(splitter_arr))
    print(f"main    (History): ", '   '.join(main_history))

    print(f"                   ", '   '.join(branch_interaction_data))
    if len(staging_data) > 0:
        if (len(staging_history)) > 0:
            staging_history[0] = "\\"
        else:
            staging_history.append("\\")
    print(f"staging (History): ", ' - '.join(staging_history))
    print(f"------------------", '-' + '---'.join(splitter_arr))
    print(f"staging (Data):    ", format_data_state_list_string(staging_data))

    print()

def print_readme_md_formatted(commit_header_text, main_data, main_history, staging_history, staging_data, branch_interaction_data):
    print("<details>")
    print(f"<summary>{commit_header_text}</summary>")

    splitter_arr = ["-" for c in staging_history]


    print()

    print("```")
    print(f"main    (Data):    ", format_data_state_list_string(main_data))
    print(f"------------------", '-' + '---'.join(splitter_arr))
    print(f"main    (History): ", '   '.join(main_history))

    print(f"                   ", '   '.join(branch_interaction_data))
    if len(staging_data) > 0:
        if (len(staging_history)) > 0:
            staging_history[0] = "\\"
        else:
            staging_history.append("\\")
    print(f"staging (History): ", ' - '.join(staging_history))
    print(f"------------------", '-' + '---'.join(splitter_arr))
    print(f"staging (Data):    ", format_data_state_list_string(staging_data))

    print("```")

    print()

    print("</details>")

    print()


def print_only_header(commit_header_text, main_data, main_history, staging_history, staging_data, branch_interaction_data):
    print(commit_header_text)

if __name__ == "__main__":
    lines = []
    with open('raw_data/CommitStateChangeA2O.v2.md', 'r') as file:
        lines = file.readlines()

    # Parsing and formatting the data    
    repo_states = parse_and_format_commit_data(lines)
    format_repo_states(repo_states)
