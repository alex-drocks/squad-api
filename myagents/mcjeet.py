import os

import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.local")
api_key = os.getenv("CHUTES_API_KEY")

base_url = "https://api.sqd.io/agents/"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}


def create_mc_jeet():
    url = base_url

    payload = {
        "name": "McJeet",
        "readme": "Buy on Solana",
        "tagline": "$JEET  |  Ma name Jeet ✌️ working at McJeet's for some meet 🥩  |  CA: 2Bzuch4YgRvJaiqtiVSbdua3J23pTWY6LUXkjHQCHG8t",
        "model": "deepseek-ai/DeepSeek-R1",
        "default_max_steps": 10,
        "sys_schedule_prompt": "Randomly Tweet about McJeet 1 time per day",
        "x_username": "McJeetSol",
        "x_searches": ["McJeet OR McJeetSol", "Solana OR $SOL", "meme"],
        "tool_ids": [
            "371c6f1b-ae65-47cb-86df-3c0a61a9f1b7",  # generate_snark
        ],
    }

    try:
        response = requests.post(
            url,
            json=payload,
            headers=headers,
        )
        # Check if the request was successful
        if response.status_code == 200:
            print("Agent created successfully!")
            print("Response data:", response.json())
        else:
            print(f"Failed to create agent. Status code: {response.status_code}")
            print("Error details:", response.json())

    except requests.RequestException as e:
        print(f"An error occurred while making the request: {e}")


def update_mc_jeet():
    url = f"{base_url}/3524c8c8-47f0-4c37-8977-14ff9b49fa5f"

    payload = {
        "x_username": "LailaVicke64501",
    }

    try:
        response = requests.put(
            url,
            json=payload,
            headers=headers,
        )
        # Check if the request was successful
        if response.status_code == 200:
            print("Agent updated successfully!")
            print("Response data:", response.json())
        else:
            print(f"Failed to create agent. Status code: {response.status_code}")
            print("Error details:", response.json())

    except requests.RequestException as e:
        print(f"An error occurred while making the request: {e}")


def get_mc_jeet():
    url = f"{base_url}/3524c8c8-47f0-4c37-8977-14ff9b49fa5f"

    try:
        response = requests.get(
            url,
            headers=headers,
        )
        # Check if the request was successful
        if response.status_code == 200:
            print("Agent retrieved successfully!")
            print("Response data:", response.json())
        else:
            print(f"Failed to retrieve agent. Status code: {response.status_code}")
            print("Error details:", response.json())

    except requests.RequestException as e:
        print(f"An error occurred while making the request: {e}")


if __name__ == "__main__":
    # get_mc_jeet()
    update_mc_jeet()
