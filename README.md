# CardGen
  
CardGen is a straightforward and easy-to-use Flask-based web API, crafted as a simple project to explore the capabilities of Flask. It offers a user-friendly way to generate random cards from a standard deck, allowing users to specify the number of cards they want or to retrieve a random card from a chosen suit. Designed for simplicity and ease of use, CardGen is perfect for those looking to see Flask in action.
## Features

-   **Get Random Cards:** Retrieve a specified number of random cards from a full deck.
-   **Get Card by Suit:** Obtain a random card from a specific suit.
## Getting Started
### Prerequisites


-   Python 3.6 or later
-   Flask
-   An AWS account for deploying to AWS Elastic Beanstalk (optional)

### Installing

1. Clone the repository: 
```git clone https://```
2. Navigate to the project directory:
```cd cardgen```
3. Install the required packages:
```pip install -r requirements.txt```
4. Start the Flask dev server:
```python application.py```

The API should now be running on `http://localhost:5000/`.
## Usage

### Get Random Cards

**Request:**
``GET /cards/?quantity=5``
```[  {"suit":  "Hearts",  "value":  "2"}, ... ]```

### Get a Card by Suit
**Request:**
``GET /card/Hearts``
```{"suit": "Hearts", "value": "Ace"}```
## Running the Tests
```pytest```

## License

This project is licensed under the MIT License
