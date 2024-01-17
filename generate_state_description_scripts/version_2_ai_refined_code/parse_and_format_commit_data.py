import itertools
import re

COMMIT_DATA_KEY = "COMMIT_DATA"
COMMIT_ID_KEY = "COMMIT_ID"
COMMIT_HEADER_TEXT_KEY = "COMMIT_HEADER_TEXT"
COMMIT_STATE_KEY = "COMMIT_STATE"
COMMIT_BRANCH_KEY = "COMMIT_BRANCH"
COMMIT_STATE_DATA_TYPE_KEY = "COMMIT_STATE_DATA_TYPE"

def parse_commit_header(line):
    """
    Parses the commit header from a given line.
    
    Args:
    line (str): A line of text from the input.

    Returns:
    tuple: Commit header text and commit ID.
    """
    if line.startswith('### '):
        # Add commit text
            # This inside a conditional statement that guarantess the line starts with '### '. 
            # - We remove those 4 characters because we dont want them now and we can add them later.
        header_text = line[4:].strip()
        commit_id = line.strip().split(' ')[2]
        return header_text, commit_id
    return None, None

def parse_branch_name(line):
    """
    Parses the branch name from a given line.
    
    Args:
    line (str): A line of text from the input.

    Returns:
    str: The branch name.
    """
    if '**main**' in line:
        return 'main'
    elif '**staging**' in line:
        return 'staging'
    return None

def parse_branch_state(line):
    """
    Parses the branch state information from a given line.
    
    Args:
    line (str): A line of text from the input.

    Returns:
    tuple: Branch data type and state.
    """
    if 'History:' in line or 'Data:' in line:
        branch_data_type, state_type = line.strip().split(':')
        state = state_type.strip().strip('`').strip('_').strip('`')
        return branch_data_type.strip('- '), state
    return None, None

def update_commit_data(commit_data, header_text=None, commit_id=None, branch_name=None, branch_state=None):
    """
    Updates the commit data dictionary with new values.
    
    Args:
    commit_data (dict): Current commit data dictionary.
    header_text (str): Commit header text.
    commit_id (str): Commit ID.
    branch_name (str): Branch name.
    branch_state (tuple): Branch data type and state.

    Returns:
    dict: Updated commit data dictionary.
    """
    if header_text and commit_id:
        commit_data[COMMIT_HEADER_TEXT_KEY] = header_text
        commit_data[COMMIT_ID_KEY] = commit_id
    if branch_name:
        commit_data[branch_name] = commit_data.get(branch_name, {})
        if branch_state:
            branch_data_type, state = branch_state
            commit_data[branch_name][branch_data_type] = state
    return commit_data

def parse_and_format_commit_data(lines):
    """
    Parses and formats commit data from a given list of lines.

    This function processes a list of strings, where each string represents a line of commit data. 
    It extracts important information such as the commit header, commit ID, branch name, and branch state.
    The function relies on helper functions to parse specific parts of the data. The extracted data 
    is accumulated and structured into a list of dictionaries, where each dictionary represents 
    a single commit's data.

    Args:
    lines (list of str): A list of strings, where each string is a line from the commit data.

    Returns:
    list of dict: A list where each element is a dictionary containing data of a single commit. 
    Each dictionary includes the commit header, commit ID, and branch-specific data, if available.

    Example of returned data structure:
    [
        {
            'COMMIT_HEADER_TEXT_KEY': 'Commit D (on staging)',
            'COMMIT_ID_KEY': 'D',
            'main': {
                'History': 'A',
                'Data': 'A'
            },
            'staging': {
                'History': 'A, B, C, D',
                'Data': 'A, C, D'
            }
        },
        ...
    ]

    Note:
    The function uses the following helper functions:
    - parse_commit_header: Extracts the commit header and ID.
    - parse_branch_name: Determines the branch name ('main' or 'staging').
    - parse_branch_state: Extracts branch-specific state information.
    - update_commit_data: Updates the current commit's data dictionary with new information.
    """
    repo_states_by_commit = []
    current_commit_data = {}
    current_branch_name = ""
    current_commit_header_text = ""

    for line in lines:
        if line.startswith('### '):
            if current_commit_data:
                repo_states_by_commit.append(current_commit_data)
                current_commit_data = {}

            current_commit_header_text, current_commit_id = parse_commit_header(line)
            update_commit_data(commit_data=current_commit_data, header_text=current_commit_header_text, commit_id=current_commit_id)

        if '**main**' in line or '**staging**' in line:
            current_branch_name = parse_branch_name(line)
        elif 'History:' in line or 'Data:' in line:
            update_commit_data(commit_data=current_commit_data, branch_name=current_branch_name, branch_state=parse_branch_state(line))

    if current_commit_data:        
        repo_states_by_commit.append(current_commit_data)

    return repo_states_by_commit




import re

def extract_state_and_context(state_string):
    """
    Extracts state letters and their context from a given state string.

    This function processes a state string to find all uppercase letters, optionally followed by 
    context information in parentheses. It returns two lists: one for the letters and another for the 
    corresponding context, if available.

    Args:
    state_string (str): A string containing state information, potentially with context.

    Returns:
    tuple: Two lists, one containing letters and the other containing contexts.
    """
    # Removing content in parentheses and subsequent characters
    state_string_fixed = state_string.split("(")[0]
    
    # Regular expression to find uppercase letters and optional context
    pattern = r'([A-Z])(?: \(([^)]+)\))?'
    matches = re.findall(pattern, state_string_fixed)

    letters = [match[0] for match in matches]
    context = [match[1] for match in matches if match[1]]

    return letters, context


def expand_letter_list_with_spaces(letter_list_in):
    """
    Expands a list of letters with spaces up to a certain letter in the alphabet.

    This function takes a list of uppercase letters and expands it by inserting spaces where letters 
    are missing in the alphabetical sequence, up to the highest value letter in the input list.

    Args:
    letter_list_in (list of str): A list of uppercase letters.

    Returns:
    list of str: The expanded list with spaces inserted.

    Example:
    Input: ['A', 'D', 'E', 'G']
    Output: ['A', ' ', ' ', 'D', 'E', ' ', 'G']
    """
    letter_list_expanded = []
    letters_found = 0

    for letter_code in range(ord('A'), ord('P')):
        letter = chr(letter_code)
        letter_list_expanded.append(letter if letter in letter_list_in else " ")
        if letter in letter_list_in:
            letters_found += 1
            if letters_found == len(letter_list_in):
                break
    
    return [] if letters_found == 0 else letter_list_expanded



def generate_branch_interaction_data(commit_id, staging_data, main_history):
    """
    Generates branch interaction data based on commit ID and branch histories.

    This function uses the commit ID, staging data, and main history to determine the 
    interaction data structure, which is represented as a list of characters.

    Args:
    commit_id (str): The commit ID.
    staging_data (list): List representing staging data.
    main_history (list): List representing main branch history.

    Returns:
    list of str: A list representing the branch interaction data.
    """
    if not staging_data:
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
    """
    Formats and prints repository states.

    Iterates over a list of repository states, each represented as a dictionary, and processes them
    for printing. This includes extracting and formatting data for the 'main' and 'staging' branches 
    and handling the branch interaction data. The final output is printed in a specified format.

    Args:
    repo_states (list of dict): A list of dictionaries, each containing data for a commit.
    """
    last_valid_commit_id = 'A'

    for commit_data in repo_states:
        # Extracting commit ID, using the last valid if current is not a single character
        commit_id = commit_data.get(COMMIT_ID_KEY, "Unknown Commit")
        commit_id = commit_id if len(commit_id) == 1 else last_valid_commit_id
        last_valid_commit_id = commit_id

        # Extracting commit header text
        commit_header_text = commit_data.get(COMMIT_HEADER_TEXT_KEY, "")

        # Extracting and formatting for 'main' branch
        main_data = commit_data['main']['Data']
        main_history = commit_data['main']['History']
        main_data_letters, main_data_context = extract_state_and_context(main_data)
        main_history_letters, main_history_context = extract_state_and_context(main_history)

        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # | ^^^ | TODO LOOK AT THE DATA WE ARE GETTING IN  [main_data_context] and [main_history_context] | ^^^ |
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

        # Extracting and formatting for 'staging' branch
        staging_data = commit_data['staging']['Data']
        staging_history = commit_data['staging']['History']
        staging_data_letters, staging_data_context = extract_state_and_context(staging_data)
        staging_history_letters, staging_history_context = extract_state_and_context(staging_history)

        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # | ^^^ | TODO LOOK AT THE DATA WE ARE GETTING IN  [staging_data_context] and [staging_history_context] | ^^^ |
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

        # Expanding letter lists with spaces
        main_data_letters_expanded = expand_letter_list_with_spaces(main_data_letters)
        main_history_letters_expanded = expand_letter_list_with_spaces(main_history_letters)
        staging_history_letters_expanded = expand_letter_list_with_spaces(staging_history_letters)
        staging_data_letters_expanded = expand_letter_list_with_spaces(staging_data_letters)

        # Generating branch interaction data
        branch_interaction_data = generate_branch_interaction_data(commit_id, staging_data_letters_expanded, main_data_letters_expanded)

        # Printing the formatted data
        test_printing_controller(commit_header_text, main_data_letters_expanded, main_history_letters_expanded, staging_history_letters_expanded, staging_data_letters_expanded, branch_interaction_data)


def format_data_state_list_string(input_list):
    output_list = [' | '.join(g) if k else '   '.join(g) for k, g in itertools.groupby(input_list, key=lambda x: x != ' ')]
    return ' | '.join(output_list)

def test_printing_controller(commit_header_text, main_data, main_history, staging_history, staging_data, branch_interaction_data):
    """
    Controls the printing of commit data in various formats.

    This function takes the processed commit data and prints it using a specific printing function.
    The printing function can be changed for different output formats.

    Args:
    commit_header_text (str): The text of the commit header.
    main_data (list): Processed data for the 'main' branch.
    main_history (list): History data for the 'main' branch.
    staging_history (list): History data for the 'staging' branch.
    staging_data (list): Processed data for the 'staging' branch.
    branch_interaction_data (list): Data representing branch interaction.
    """
    print_readme_md_formatted(commit_header_text, main_data, main_history, staging_history, staging_data, branch_interaction_data)
    # Additional printing functions can be used for different formats

def print_basic(commit_header_text, main_data, main_history, staging_history, staging_data, branch_interaction_data):    
    """
    Prints the commit data in a basic format suitable for console output.

    Args:
    commit_header_text (str): The text of the commit header.
    main_data (list): Processed data for the 'main' branch.
    main_history (list): History data for the 'main' branch.
    staging_history (list): History data for the 'staging' branch.
    staging_data (list): Processed data for the 'staging' branch.
    branch_interaction_data (list): Data representing branch interaction.
    """
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
    """
    Prints the commit data in a Markdown format suitable for README files.

    Args:
    commit_header_text (str): The text of the commit header.
    main_data (list): Processed data for the 'main' branch.
    main_history (list): History data for the 'main' branch.
    staging_history (list): History data for the 'staging' branch.
    staging_data (list): Processed data for the 'staging' branch.
    branch_interaction_data (list): Data representing branch interaction.
    """
    print("<details>")
    print(f"<summary>{commit_header_text}</summary>\n")

    splitter_arr = ["-" for _ in staging_history]

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
    print("\n</details>\n")

def format_data_state_list_string(input_list):
    """
    Formats a list of data states into a string for printing.

    Args:
    input_list (list of str): A list of data states.

    Returns:
    str: Formatted string representation of the data states.
    """
    output_list = [' | '.join(g) if k else '   '.join(g) for k, g in itertools.groupby(input_list, key=lambda x: x != ' ')]
    return ' | '.join(output_list)


def print_only_header(commit_header_text, main_data, main_history, staging_history, staging_data, branch_interaction_data):
    """
    Prints only the commit_header_text value. Handy for displaying the commit history flow without diving further. Simple entry point! 

    Args:
    commit_header_text (str): The text of the commit header.
    main_data (list): Processed data for the 'main' branch.
    main_history (list): History data for the 'main' branch.
    staging_history (list): History data for the 'staging' branch.
    staging_data (list): Processed data for the 'staging' branch.
    branch_interaction_data (list): Data representing branch interaction.
    """
    print(commit_header_text)

if __name__ == "__main__":
    # Read lines from the input file
    lines = []
    with open('raw_data/CommitStateChangeA2O.v2.md', 'r') as file:
        lines = file.readlines()

    # Parsing and formatting the commit data from the file
    # This step transforms the raw data into a structured format (list of dictionaries),
    # where each dictionary contains data related to a specific commit.
    repo_states = parse_and_format_commit_data(lines)

    # Formatting and printing the repository states
    # This function processes each commit's data and prints it in the desired format.
    # It includes extracting and formatting data for 'main' and 'staging' branches
    # and handling branch interaction data.
    format_repo_states(repo_states)
