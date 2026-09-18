"""
Fake truth is the unsaid help, when I walk the wrong way.
Path validation as sovereign feedback.
"""


def validate_path(current_path: str, forbidden_paths: list) -> bool:
    return current_path not in forbidden_paths


def get_help_message(current_path: str, forbidden_paths: list) -> str:
    if not validate_path(current_path, forbidden_paths):
        return "Fake truth detected: You are walking the wrong way. The unsaid help is available."
    return "Path is clear."


if __name__ == "__main__":
    forbidden = ["/dark_alley", "/wrong_turn", "/dead_end"]
    my_path = "/wrong_turn"
    print(get_help_message(my_path, forbidden))
