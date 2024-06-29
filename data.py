from tkinter import messagebox

import requests
from options import OptionsInterface
import html

# Added class here !!
category_dict = {
  "trivia_categories": [
    {
      "id": 9, "name": "General Knowledge"
    },
    {
      "id": 10, "name": "Entertainment: Books"
    },
    {
      "id": 11, "name": "Entertainment: Film"
    },
    {
      "id": 12, "name": "Entertainment: Music"
    },
    {
      "id": 13, "name": "Entertainment: Musicals & Theatres"
    },
    {
      "id": 14, "name": "Entertainment: Television"
    },
    {
      "id": 15, "name": "Entertainment: Video Games"
    },
    {
      "id": 16, "name": "Entertainment: Board Games"
    },
    {
      "id": 17, "name": "Science & Nature"
    },
    {
      "id": 18, "name": "Science: Computers"
    },
    {
      "id": 19, "name": "Science: Mathematics"
    },
    {
      "id": 20, "name": "Mythology"
    },
    {
      "id": 21, "name": "Sports"
    },
    {
      "id": 22, "name": "Geography"
    },
    {
      "id": 23, "name": "History"
    },
    {
      "id": 24, "name": "Politics"
    },
    {
      "id": 25, "name": "Art"
    },
    {
      "id": 26, "name": "Celebrities"
    },
    {
      "id": 27, "name": "Animals"
    },
    {
      "id": 28, "name": "Vehicles"
    },
    {
      "id": 29, "name": "Entertainment: Comics"
    },
    {
      "id": 30, "name": "Science: Gadgets"
    },
    {
      "id": 31, "name": "Entertainment: Japanese Anime & Manga"
    },
    {
      "id": 32, "name": "Entertainment: Cartoon & Animations"
    }
  ]
}


class Data:

    # maybe possible to pass class OptionsInterface
    # as argument to have access to get methods
    # instead of doing it in the main !!

    def __init__(self, category, difficulty, number):

        if category == "Any Category" and difficulty == "Any Difficulty":
            parameters = {
                "amount": number,
                "type": "boolean"
            }
        elif category == "Any Category":
            parameters = {
              "amount": number,
              "difficulty": difficulty,
              "type": "boolean"
            }
        elif difficulty == "Any Difficulty":
            category_data = {category['name']: category['id'] for category in category_dict['trivia_categories']}
            category_id = category_data[category]
            parameters = {
                "amount": number,
                "category": category_id,
                "type": "boolean"
            }
        else:
            category_data = {category['name']: category['id'] for category in category_dict['trivia_categories']}
            category_id = category_data[category]
            parameters = {
                "amount": number,
                "category": category_id,
                "difficulty": difficulty,
                "type": "boolean"
            }
        print("Parameters for API request: ", parameters)

        request = requests.get(url=f"https://opentdb.com/api.php", params=parameters)

        request.raise_for_status()
        data = request.json()

        if data['response_code'] == 1:
            messagebox.showwarning(title="Error", message="Not enough questions for these settings!")

        self.question_data = data["results"]

