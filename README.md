# Basic Mathematical Application using Flask

## Introduction

This repository is a simple web application built with Flask that performs basic mathematical operations. It combines HTML, JavaScript, and Python to create a functional web interface for math calculations.

## Table of Contents

- [Introduction](#introduction)
- [Prerequirements](#prerequirements)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Prerequirements

- ![Python 3.7](https://img.shields.io/badge/Python-3.7-blue) or above: [Download here](https://www.python.org/downloads)

## Project Structure

```
Basic-Math-App/
├── Maths/
│   ├── __init__.py
│   └── mathematics.py
├── .gitignore
├── static/
│   └── script.js
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Features

- Simple Flask web application for basic math
- Basic routing
- Basic HTML, JavaScript and Bootstrap

## Installation

To install this project, open your Terminal and follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/arthurtran04/Basic-Math-App.git
    ```

2. Run the `cd` command to change the directory to `Basic-Math-App`:

    ```bash
    cd "$(find . -type d -name "Basic-Math-App")"
    ```
    
3. Create a Python virtual environment `venv` and install the required dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate 
    pip install -r requirements.txt
    ```

## Usage

To start the Flask application, run the `app.py` file:

   ```bash
   python app.py
   ```

This application will run locally at `http://127.0.0.1:5000`:

<img width="600rem" alt="Terminal" src="https://github.com/user-attachments/assets/e8160f1e-e853-4e60-adba-91c44555ae25" />

The UI:

<img width="600rem" alt="Webpage" src="https://github.com/user-attachments/assets/2b614832-3549-4e72-8c93-5468c182121f" />

On the webpage, there are 5 basic arithmetic operations you can try like `Add`, `Subtract`, `Multiply`, `Divide` and `Modulo`:

<img width="600rem" alt="Example" src="https://github.com/user-attachments/assets/2e95ab54-9dbb-494e-b25d-2f1dda7f5ec8" />

Additionally, you can use different routes, including `/sum`, `/sub`, `/mul`, `/div`, and `/mod`.
You need to asign a value to two parameters `num1` and `num2` into the URL to calculate, example `http://127.0.0.1:5000/div?num1=2.1&num2=3.2` (`num1 = 2.1`, `num2 = 3.2`)

<img width="600rem" alt="Example" src="https://github.com/user-attachments/assets/d2b03b25-ca64-460e-bea3-c01e4dc6140b" />

To stop the application, use `Ctrl + C` in the Terminal

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
