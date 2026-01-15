import json
import sys

def validate_todo_report(filepath="todo_report.json"):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: File not found - {filepath}")
        sys.exit(1)

    if not isinstance(data, list):
        print("Error: Root element must be a JSON array.")
        sys.exit(1)

    print(f"Found {len(data)} TODO items.")

    required_fields = {
        "title": str,
        "description": str,
        "deepLink": str,
        "filePath": str,
        "lineNumber": int,
        "confidence": int,
        "rationale": str,
        "context": str,
        "language": str
    }

    for idx, item in enumerate(data):
        for field, expected_type in required_fields.items():
            if field not in item:
                print(f"Error: Item {idx} missing required field '{field}'.")
                sys.exit(1)
            if not isinstance(item[field], expected_type):
                print(f"Error: Item {idx} field '{field}' has wrong type. Expected {expected_type}, got {type(item[field])}.")
                sys.exit(1)

        if not (1 <= item["confidence"] <= 3):
            print(f"Error: Item {idx} confidence score must be between 1 and 3. Got {item['confidence']}.")
            sys.exit(1)

    print("Validation successful!")

if __name__ == "__main__":
    validate_todo_report()
