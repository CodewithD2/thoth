# Thoth Programming Language

![GitHub contributors](https://img.shields.io/github/contributors/CodewithD2/thoth)
![GitHub last commit](https://img.shields.io/github/last-commit/CodewithD2/thoth)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/CodewithD2/thoth)

Thoth is a programming language created for educational and exploration purposes, named after the Egyptian deity of knowledge and writing. It is written in Python and utilizes `llvmlite` for LLVM bindings to compile code to efficient machine code. This project uses `miniconda` to manage the development environment and dependencies.

## Key Features

- **Educational Focus**: Designed to be a simple and easy-to-understand language for learning about interpreters and compilers.
- **Python-based**: Implemented in Python for clarity and ease of development.
- **LLVM Integration**: Uses `llvmlite` to compile to efficient machine code.

## Technology Stack

- **Language**: Python 3.10
- **Compiler Backend**: LLVM (via `llvmlite`)
- **Environment Management**: Miniconda

## Getting Started

To get started with Thoth, you'll need to set up the environment and install the dependencies.

### Prerequisites

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/CodewithD2/thoth.git
    cd thoth
    ```
2.  **Set up the conda environment:**
    ```bash
    conda create -n thoth python=3.10
    conda activate thoth
    ```
3.  **Install dependencies:**
    ```bash
    pip install llvmlite
    ```

## Usage

To run the lexer, execute the `main.py` script:

```bash
python main.py
```

This will read the contents of `tests/lexer.th`, tokenize it, and display the resulting tokens.

## Core Components

The project is structured into the following key files:

- **`Token.py`**: Defines the `Token` class and `TokenType` enumeration, which represent the basic units of the language.
- **`Lexer.py`**: Contains the `Lexer` class, which is responsible for lexical analysis (converting source code into a stream of tokens).
- **`main.py`**: The main entry point for the interpreter.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.