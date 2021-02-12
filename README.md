# Language processor of a modified version of JS
## Description of the proyect
The goal of this proyect is to create a languaje processor for a modified version of the JS languaje, which you can find more about [here.](https://dlsiisv.fi.upm.es/procesadores/IntroJavaScript.html)
For the development of the languaje processor we needed a base languaje in which all the different components of the processor could be done. So we needed a languaje capable of working with OOP, easy to use and stable. We didn't pursue a fast processor as this proyect wasn't going to be used commercially.
Therefore, we chose Python as a base languaje because it fullfilled all the requirements above and has a great community support.

## What is exactly a languaje processor?
As you probably already know, computers need to work in binary. However, humans aren't able to write code in binary as it is extremely difficult. So in order to overcome this issue people began working on compilers.
A compiler is a piece of software which translates from human readable code to binary. Therefore, enabling humans to write complex pieces of software with less difficulty. You can check out more about them [here](https://en.wikipedia.org/wiki/Compiler).
In a compiler there are two main parts, the languaje processor and the languaje translator. The first one is the one being developed in this proyect. We have chosen this specific part as it is the most versatile part. Its aplications vary from compilers to data processing.

The languaje processor has three main modules:
1. The lexer module
2. The syntax module
3. The semantic module

## The lexer module.
As its name suggests, this module receives de raw data, processes it and generate tokens according to the content of the raw input. It generates a token only when asked for by the syntax module.

## The syntax module.
This module checks if the syntax of the data introduced is correct by reading the output values of the lexer module. It asks for a token to the lexer module to build up the syntax tree. In this proyect we chose to build the parser using a bottom up mode. This allowed us to use [sly](https://sly.readthedocs.io/en/latest/sly.html) a library to help us build the parser in a robust and neat way.
We are not going to further explain the syntax module as most of it is detailled in the sly documentation.

## The semantic module.
The semantinc module was built up using a syntax-directed translation which you can find out more [here](https://en.wikipedia.org/wiki/Syntax-directed_translation). That is why in the proyect you will only find lexer module and syntax module as the semantic module is embedded in the syntax module.
The goal of this module is to check whether the syntax correct trees are semantically correct. I.E: there are no breaks outside of loops or returns outside of functions.

## Dependencies:
In order to develop all three modules as efficiently as we can we chose to use a well documented library in which we could build on top. The one selected was [sly](https://sly.readthedocs.io/en/latest/sly.html).

## Documentation
Our code is documented and detailed. We pursue code not just well written, but also understandable for everyone outside of the proyect. We believe that way it can help us mantain it and improve it along the years at minimal cost, while encouraging outsiders to join this venture.

## Suggestions
If you see mistakes in the code or parts that could be better, please fix or improve them.
Hope you find usefull and like the proyect!

## Acknowledgment
This proyect was built by Daniel Tomás, Aarón Cabero and Alejandro Cuadrón.



