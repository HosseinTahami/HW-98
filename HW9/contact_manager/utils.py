import re

def get_input(prompt, retry=True, target_type=str, pattern=None):
    """
    Get and Return user inputs after validating them
    """
    assert callable(target_type)


    try:
        user_input = input(prompt)  # if Ctrl+C -> raise KeyboardInterrupt
        user_input = target_type(user_input)
        if pattern is not None:
            assert re.fullmatch(pattern, user_input)
    except KeyboardInterrupt:
        print("\nForce Exit...")
        exit(0)
    except Exception as err:
        if retry:
            print("Invalid input, try again")
            return get_input(prompt, retry, target_type)
        else:
            raise TypeError("Invalid input, try again") from err  # NewException -> err
    return user_input