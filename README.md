# Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo

## Project Description

This project utilizes a context-free grammar (CFG) ruleset implemented with the Natural Language Toolkit (NLTK) to break down the structure of sentences and extract noun chunks. 
By defining grammar rules that capture the syntactic patterns of noun phrases, the project enables the identification and extraction of noun chunks from natural language text, 
facilitating deeper linguistic analysis and information extraction.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies](#technologies)
- [Credit](#credit)
- [License](#license)

## Installation

You'll need to have Python and pip3 installed. You can download them from the [official Python website](https://www.python.org/downloads/).

1. Clone the repository:

```bash
git clone https://github.com/ColinDao/buffalo.git
```

2. Navigate to the project directory:

```bash
cd buffalo
```

3. Install the required dependencies:

```bash
pip3 install -r requirements.txt
```

## Usage

To execute the parser, run the following command:

```bash
python parser.py [1.txt]
```

Watch as the parser is able to deconstruct and visualize the text as well as pull out key noun phrases!

## Features

**CFG Definition**: Define a set of context-free grammar rules that describe the syntactic structure of noun phrases, 
including rules for determiners, adjectives, nouns, and more. <br />
<br />
**Tokenization**: Using regular expressions, gather all of the elements of the sentence. <br />
<br />
**Parsing Algorithm**: Implement a parsing algorithm using NLTK to parse sentences according to the defined CFG ruleset, 
identifying and extracting noun chunks using depth-first search based on the parsed syntactic structure.<br />
<br />

## Credit

This project was completed as a part of [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/2024/). Go check them out!

## Technologies
**Language**: Python <br />
**Libraries**: NLTK, Sys, RE

## License

MIT License

Copyright (c) 2024 Colin Dao

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
