import zmq

PORT = 5556

def send_request(socket, test, request):
    """Send one test request to the Prompts Microservice."""

    print(f"\n--- {test} ---")
    print("Request:")
    print(request)

    socket.send_json(request)
    response = socket.recv_json()

    print("Response:")
    if response["success"]:
        print("\nGenerated Prompt:")
        print(response["prompt"])
    else:
        print("\nError:")
        print(response["error"])


def main():
    """Run test cases for the Prompts Microservice."""

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://127.0.0.1:{PORT}")

    test_cases = [
    {
        "name": "Test 1",
        "request": {
            "request": "Generate a story prompt for this character and world.",
            "details": {
                "character_name": "Aric",
                "character_class": "Warrior",
                "attributes": ["Brave", "Loyal", "Strong"],
                "world_name": "Eldoria",
                "world_type": "Fantasy",
                "world_features": [
                    "Ancient Ruins",
                    "Magic Forest",
                    "Dragon Lairs",
                    "Floating Islands",
                    "Crystal Caves"
                ]
            }
        }
    },
    {
        "name": "Test 2",
        "request": {
            "request": "Generate a motivational fitness prompt.",
            "details": {
                "goal": "increase consistency",
                "workout_type": "strength training",
                "difficulty": "beginner"
            }
        }
    },
    {
        "name": "Test 3",
        "request": {
            "request": "Generate a productivity prompt to help prioritize tasks.",
            "details": {
                "tasks": ["finish homework", "review code", "prepare team update"],
                "priority": "school assignments",
                "time_available": "2 hours"
            }
        }
    },
    {
        "name": "Test 4",
        "request": {
            "details": {
                "goal": "stay consistent"
            }
        }
    },
    {
        "name": "Test 5",
        "request": {
            "request": ""
        }
    },
    {
        "name": "Test 6",
        "request": {
            "request": 12345
        }
    }
]

    for test_case in test_cases:
        send_request(socket, test_case["name"], test_case["request"])


if __name__ == "__main__":
    main()