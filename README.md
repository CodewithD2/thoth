# Thoth Programming Language

Thoth is a programming language created for educational and exploration purposes, named after the Egyptian deity of knowledge and writing. It is written in Python and utilizes `llvmlite` for LLVM bindings to compile code to efficient machine code. This project uses `miniconda` to manage the development environment and dependencies.

## Overview

The Thoth interpreter is built in Python and currently consists of a lexer that performs lexical analysis on the source code. The lexer's role is to read the input code and break it down into a sequence of tokens, which are the smallest meaningful units of the language (e.g., numbers, operators, symbols).

## Core Components

The project is structured into the following key files:

### `Token.py`

This file defines the fundamental building blocks for the lexer.

#### `class TokenType(Enum)`

An enumeration that defines all possible types of tokens that can be recognized by the lexer. This includes:
- **Special Tokens**: `EOF` (End of File), `ILLEGAL` (unrecognized character).
- **Data Types**: `INT` (Integer), `FLOAT` (Floating-point number).
- **Arithmetic Operators**: `PLUS`, `MINUS`, `MULTIP`, `DIVID`, `POW`, `MODULUS`.
- **Symbols**: `SEMICOLON`, `LPAREN` (Left Parenthesis), `RPAREN` (Right Parenthesis).

#### `class Token`

Represents a single token identified by the lexer. Each token has:
- `type`: The `TokenType` of the token.
- `literal`: The actual value of the token from the source code (e.g., "123", "+").
- `line_no`: The line number where the token appears.
- `position`: The character position on the line where the token starts.

### `Lexer.py`

This is the heart of the lexical analysis phase.

#### `class Lexer`

The `Lexer` class is responsible for taking the source code as a string and converting it into a stream of `Token` objects.

##### `__init__(self, source: str)`
The constructor initializes the lexer with the source code string. It sets up internal state variables like the current position, read position, and line number.

##### `__read_char(self)`
A private helper method that reads the next character from the source code and advances the lexer's position.

##### `__skip_whitespace(self)`
A private helper method that consumes and ignores any whitespace characters (spaces, tabs, newlines).

##### `__new_token(self, tt: TokenType, literal: Any) -> Token`
A factory method for creating a new `Token` object with the given type and literal value, automatically capturing the current line number and position.

##### `__is_digit(self, ch: str) -> bool`
A utility method to check if a given character is a digit (0-9).

##### `__read_number(self) -> Token`
This method is responsible for parsing numbers from the source code. It can handle both integers and floating-point numbers. If it encounters more than one decimal point in a number, it flags it as an `ILLEGAL` token.

##### `next_token(self) -> Token`
This is the main public method of the `Lexer`. Each time it's called, it reads the source code and returns the next `Token` it finds. It uses a `match` statement to handle single-character tokens and calls `__read_number` for numeric literals.

### `main.py`

This is the main script to run the lexer.

It reads the source code from a file named `tests/lexer.th`, creates an instance of the `Lexer`, and then iteratively calls `next_token()` to get each token until the end of the file is reached. Each token is then printed to the console.

## How to Run

To run the lexer, you will first need to set up the environment using miniconda and install the necessary dependencies.

1.  **Set up the conda environment:**
    ```bash
    conda create -n thoth python=3.10
    conda activate thoth
    ```
2.  **Install dependencies:**
    ```bash
    pip install llvmlite
    ```
3.  **Run the lexer:**
    ```bash
    python main.py
    ```

This will read the contents of `tests/lexer.th`, tokenize it, and display the resulting tokens.
