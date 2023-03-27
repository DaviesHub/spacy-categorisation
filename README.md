# Tokenizer and Entity Recognition with SpaCy

## Contents
1. Description
2. Features
3. Package Requirements
4. Installation & Usage
5. Running the Application with Docker
6. Contributions
7. References

## Description
This project provides a small Python script that uses the SpaCy library to tokenize and recognize named entities in a list of sentences. It also includes a Dockerfile that allows you to build a console-based Docker container for running the script.

## Features
The script provided in this project offers the following features:

- Tokenization: The script uses SpaCy to tokenize each sentence in the provided list of sentences. The resulting tokens are stored in a list and printed to the console.

- Entity Recognition: The script also uses SpaCy to recognize named entities in each sentence in the provided list of sentences. The recognized entities and their labels are printed to the console.

- Dockerization: The script is packaged in a Docker container, allowing it to be run in a portable and reproducible environment. This makes it easy to share and deploy the script across different systems and platforms.

## Package Requirements
Package requirements for this app can be seen on the requirements.txt file. Install the required packages by running the
following command on the command line:
'pip install -r requirements.txt'

## Installation & Usage 
To run the script outside of Docker, follow these steps:

1. Install the requirements in the requirements.txt file 
2. Download the 'en_core_web_lg' model for SpaCy: python -m spacy download en_core_web_lg
3. Clone this repository and navigate to the root directory
4. Run the script: garden.py

## Running the Application with Docker
To run the script inside Docker, follow these steps:

1. Install Docker on the machine if it is not already installed.
1. Clone this repository and navigate to the root directory.
2. Build the Docker image: docker build -t <'image name'>.
3. Run the Docker container: docker run <'image name'>.
4. The output of the script will be printed to the console.

## Contributions
Contributions to the project are welcome. Please submit a pull request with your changes.

## References
SpaCy documentation: https://spacy.io/
Docker documentation: https://docs.docker.com/