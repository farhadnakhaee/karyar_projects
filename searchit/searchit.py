import os


def get_query():
    """
    Get user query.
    """
    query = input("Search for ?\n")
    return query


def read_file_names(directory_path):
    """
    Read file with .txt extension in a Directory and return list of them.
    """
    # Iterate over the files in the directory
    filenames = []
    try:
        for filename in os.listdir(directory_path):
            if filename.endswith(".txt"):
                filenames.append(filename)
    except FileNotFoundError:
        print("The system cannot find the directory path")
    else:
        if not filenames:
            print("No files with .txt extension were found!")
        else:
            return filenames


def print_file_names(file_names):
    """
    Function that print file names and its numbers.
    """
    print("Enter number of file names.\nFile names:")
    for i, file_name in enumerate(file_names):
        if i % 4 == 0 and i > 0:
            print()  # print a newline after every 4th element
        print('{:<2}. {:<15}'.format(i+1, file_name), end='')

    if len(file_names) % 4 != 0:
        print()
    print()
    print(str(len(file_names) + 1) + ". All")


def filter_file(file_names):
    """
    Get user selected files in a list
    """
    try:
        index_of_selected_files = [int(i)-1 for i in input("Search in ? (ex: 20 11 2)\n").split()]
    except ValueError:
        print("Just Enter The Numbers :)")
        return filter_file(file_names)
    else:
        index_of_selected_files = [x for x in index_of_selected_files if x in range(len(file_names)+1)]

        # select all files
        if len(file_names) in index_of_selected_files:
            selected_files = file_names
        else:
            selected_files = [file_names[i] for i in index_of_selected_files]
    return selected_files


def search_word_in_file(directory_path, file_name, word, case_sensitive):
    """
      Searches for a given word in a file and returns the lines containing the word, along with the line number.

    Args:
        directory_path (str): Directory path for filename.
        file_name (str): The name of the file to search in.
        word (str): The word to search for.
        case_sensitive (bool): True if the search should be case-sensitive, False otherwise.

    Returns:
        A list of tuples containing the lines and line numbers where the word was found in the file, along with
        the file name. If the word is not found in the file, an empty list is returned.
    """
    result = []
    with open(os.path.join(directory_path, file_name), "r", encoding="UTF-8") as f:
        line_number = 0
        context_window = []
        for line_case in f:
            line_number += 1
            if not case_sensitive:
                line = line_case.lower()
            else:
                line = line_case

            context_window.append(line.strip())

            # Remove the oldest line from the context window if it exceeds the context size
            if len(context_window) > 2:
                context_window.pop(0)
            joined_lines = " ".join(context_window)

            if word in line:
                result.append((line_case, line_number))
            else:
                if word not in context_window[0] and word in joined_lines:
                    lines_result = f" {context_window[0]}\n\t\t{context_window[1]}\n"
                    result.append((lines_result, line_number))

    if result:
        result.append(file_name)
        return result


def search_word_in_files(directory_path, file_names, word, case_sensitive):
    """
    Iterate search word for file in filenames.
    """
    files_result = []
    for file_name in file_names:
        file_result = search_word_in_file(directory_path, file_name, word, case_sensitive)
        if file_result:
            files_result.append(file_result)

    return files_result


def search_phrase_in_file(directory_path, file_name, phrase):
    """
    Searches for a given phrase in a file and returns the lines that contain the most words from the phrase.

    Args:
        directory_path (str): Directory path for filename.
        file_name (str): The name of the file to search in.
        phrase (str): The phrase to search for.

    Returns:
        A list of tuples containing the lines, line numbers, count of phrase words in the line, and the file name.
        The list is sorted by the count of phrase words in the line, in descending order.
        If no lines in the file contain at least 50% of the words in the phrase, None is returned.
    """
    # Split the search phrase into individual words
    phrase_words = phrase.split()

    number_of_displayed_result = 5
    result = [(0, 0, 0, 0)]
    # temp = (0, 0, 0, 0)

    with open(os.path.join(directory_path, file_name), "r", encoding="UTF-8") as f:
        line_number = 0
        for line in f:
            line_number += 1

            # Count the number of times the search words appear in the line
            count = sum(1 for phrase_word in phrase_words if phrase_word in line)

            # if there are about 50 percent of phrase words in line, append line to result
            if count >= len(phrase_words)//2 + 1:
                result.append((line.strip(), line_number, count, file_name))

    if len(result) >= number_of_displayed_result:
        return result
    elif len(result) == 1:
        return None
    else:
        result.pop(0)
        return result


def search_phrase_in_files(directory_path, file_names, phrase):
    """
    Iterate search phrase for file in filenames.
    """
    files_result = []
    for file_name in file_names:
        file_result = search_phrase_in_file(directory_path, file_name, phrase)
        if file_result:
            files_result += file_result
    return files_result


def get_search_type():
    """
    Get search type: "simple" or "advance" or "quit"
    """
    search_type = 0
    while search_type != "1" and search_type != "2" and search_type != "3":
        search_type = input("1. Simple search\n2. Advance search\n3. Quit\nChoose one? (1, 2 or 3) \n")
    if search_type == "1":
        return "simple"
    elif search_type == "2":
        return "advance"
    elif search_type == "3":
        return "quit"


def print_exact_results(directory_path, file_names, query, case_sensitive, count_of_result=5):
    """
    Searches for an exact query in multiple files and prints the lines that exactly match the query.

    Args:
        directory_path (str): Directory path for filename.
        file_names (list): A list of file names to search in.
        query (str): The exact query to search for.
        case_sensitive (bool): True if the search should be case-sensitive, False otherwise.
        count_of_result (int): The maximum number of results to display for each file. Default is 5.

    Returns:
        A tuple containing a boolean value indicating if any exact results were found, and a boolean value indicating
        if there are more results than were displayed.
        If at least one exact result is found, the function prints the file name and the exact match lines for each file
        If there are more exact results than the maximum number of results to display, the function prints a "see more".
        If no exact results are found in any of the files, the function returns False for the first value in the tuple.
    """
    exact_results = search_word_in_files(directory_path, file_names, query, case_sensitive)
    flag = False
    if exact_results:
        exact_results.sort(key=len, reverse=True)
        total_count = sum(len(exact_result)-1 for exact_result in exact_results)
        print("-"*30 + f"\nSIMPLE RESULTS for: '{query}'\n(Founded {total_count} Exact Results)\n" + "-"*30)

        for exact_result in exact_results:
            count = 0
            print(f"\n--<< file name: {exact_result[-1]} / number of results in file: {len(exact_result) - 1} >>--\n")

            for i in range(min(len(exact_result) - 1, count_of_result)):
                count += 1
                print(f"{count}. line {exact_result[i][1]}: {exact_result[i][0].strip()}")

            if len(exact_result)-1 > count_of_result:
                print("--- see more ---")
                flag = True

        return True, flag
    else:
        return False, flag


def print_approximate_results(directory_path, file_names, query, count_of_result=5):
    """
    Searches for an approximate query in multiple files and prints the lines that contain the most words from the query.

    Args:
        directory_path (str): Directory path for filename.
        file_names (list): A list of file names to search in.
        query (str): The approximate query to search for.
        count_of_result (int): The maximum number of results to display. Default is 5.

    Returns:
        A tuple containing a boolean value indicating if any approximate results were found, and a boolean value
        indicating if there are more results than were displayed.
        If at least one approximate result is found, the function prints the file name, the count of phrase words
        founded, and the lines that contain the most words from the query.
        If there are more approximate results than the maximum number of results to display, the function prints
        a "see more" message.
        If no approximate results are found in any of the files, the function returns False for the first value
        in the tuple.
    """
    approximate_results = search_phrase_in_files(directory_path, file_names, query)
    flag = False

    if approximate_results:
        approximate_results.sort(key=lambda x: x[2], reverse=True)
        total_count = len(approximate_results)
        print("-" * 30 + f"\nSIMPLE RESULTS for: '{query}'\n(Founded {total_count} Approximate results)\n" + "-" * 30)
        count = 0

        for i in range(min(len(approximate_results), count_of_result)):
            count += 1
            print(f"\n{count}. file name: {approximate_results[i][3]} / "
                  f"count of phrase word founded:{approximate_results[i][2]}\n"
                  f"   line {approximate_results[i][1]}: {approximate_results[i][0]}")

        if len(approximate_results) > count_of_result:
            print("\n--- see more ---")
            flag = True

        return True, flag
    else:
        return False, flag


def print_menu():
    """
    print menu and return user choice.
    """
    print("\n--- Wellcome to SEARCH IT ---\n1. Search it\n2. History\n3. About\n4. Exit\n")
    user_choice = input("Your Choose? (1, 2, 3 or 4)\n")
    return user_choice


def see_more_result(directory_path, file_names, query, case_sensitive, exact, count_of_result=5):
    """
    Displays additional search results based on user input.

    Args:
        directory_path (str): Directory path for filename.
        file_names (list): A list of file names to search through.
        query (str): The search query.
        case_sensitive (bool): Specifies whether the search is case-sensitive.
        exact (bool): Specifies whether the search should match the query exactly.
        count_of_result (int, optional): The number of search results to display at a time. Defaults to 5.

    Returns:
        None
    """
    user_choice = "y"
    see_more = True
    while user_choice == "y" and see_more:
        user_choice = input("See More? (y/n)\n").lower()
        if user_choice == "y":
            count_of_result += 5
            if exact:
                result_of_print_exact, see_more = print_exact_results(directory_path, file_names, query,
                                                                      case_sensitive, count_of_result)
            else:
                result_of_print_approximate, see_more = print_approximate_results(directory_path, file_names,
                                                                                  query, count_of_result)


def print_all_results(directory_path, file_names, query, case_sensitive=False):
    """
    Prints all search results based on a query, including exact and approximate matches.

    Args:
        directory_path (str): Directory path for filename.
        file_names (list): A list of file names to search through.
        query (str): The search query.
        case_sensitive (bool, optional): Specifies whether the search is case-sensitive. Defaults to False.

    Returns:
        bool: True if at least one result is found, False otherwise.
    """
    result_of_print_exact, see_more = print_exact_results(directory_path, file_names, query, case_sensitive)

    # see more exact results
    if see_more:
        see_more_result(directory_path, file_names, query, case_sensitive, exact=True)

    if not result_of_print_exact:
        result_of_print_approximate, see_more = print_approximate_results(directory_path, file_names, query)

        # see more approximate results
        if see_more:
            see_more_result(directory_path, file_names, query, case_sensitive, exact=False)

        if not result_of_print_approximate:
            print("\nNo items found!\n")
            return False

    return True


def main_search():
    """
    This is a main function.
    """
    directory_path = input("Hello!\nEnter your directory path: (ex: C:/Users/Fari/Desktop/dickens):\n")
    file_names = read_file_names(directory_path)
    if file_names:
        user_name = input("\nWhats your name?\n")
        count = 0
        # main_loop
        while True:
            menu_number = print_menu()

            if menu_number == "1":
                search_again = "y"

                while search_again == "y":
                    query = get_query()
                    search_type = get_search_type()
                    count += 1
                    with open(f"{user_name}.txt", "a") as f:
                        f.write(f"{count}. searched for: {query} / search type: {search_type}\n")

                    # simple search
                    if search_type == "simple":
                        print_all_results(directory_path, file_names, query.lower())
                    # advance search
                    elif search_type == "advance":
                        print_file_names(file_names)
                        selected_file_names = filter_file(file_names)
                        case_sensitive = input("Is the search case sensitive or not? (y/n)")

                        if case_sensitive == "y":
                            print_all_results(directory_path, selected_file_names, query, case_sensitive=True)
                        else:
                            print_all_results(directory_path, selected_file_names, query.lower(), case_sensitive=False)

                    elif search_type == "quit":
                        break

                    search_again = input("-"*50 + "\nSearch again? (y/n)\n").lower()

            elif menu_number == "2":
                username = input("Input your username:\n")
                try:
                    with open(f"{username}.txt", "r") as f:
                        print("-" * 50 + f"\n---<< History for {username} >>---\n")
                        print(f.read())
                        print("-"*50)
                except FileNotFoundError:
                    print("Username is wrong!")

            elif menu_number == "3":
                print("I'm Farhad Nakhaee\nEmail: Nakhaee.Farhad@gmail.com")
            elif menu_number == "4":
                print("bye!")
                break

main_search()
