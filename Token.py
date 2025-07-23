from enum import Enum
from typing import Any


class TokenType(Enum):
    #special tokens 
    EOF = "EOF"
    ILLEGAL = "ILLEGAL"

    #data types

    INT = "INT"
    FLOAT = "FLOAT"

    #arithmitic

    PLUS = 'PLUS' 
    MINUS = 'MINUS'
    MULTIP = 'MULTIP'
    DIVID = 'DIVID'
    POW = 'POW'
    MODULUS = 'MODULUS'

    #symbols
    SEMICOLON = 'SEMICOLON'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN' 

class Token:
    def __init__(self , type :TokenType , literal : Any , line_no : int , position : int ) -> None :

        self.type = type
        self.literal = literal
        self.line_no = line_no
        self.position = position



    def __str__(self)-> str :
        return f"Token[{self.type} : {self.literal} : Line {self.line_no} : Position {self.position}] "
    
    def __repr__(self):
        return str(self)