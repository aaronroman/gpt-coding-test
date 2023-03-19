
# Testing with Chat-GPT4 to refactor Python code

![](https://raw.githubusercontent.com/aaronroman/gpt-coding-test/main/images/header.png)

## Motivation

GPT, a powerful AI model, has the potential to assist software development processes, particularly in tedious and time-consuming tasks such as documentation, unit testing, and refactoring. By conducting simple experiments, we can understand its capabilities and how much time and effort it can save us. While GPT cannot replace human developers, it can certainly streamline certain aspects of software development and help us achieve higher efficiency and quality.

## Example 1

Our first experiment will involve providing GPT-4 with a low-quality spaghetti code example. While simple in nature, this example will be sufficient to gauge whether GPT-4 can effectively perform a refactor by creating modules and comprehending the various parts of the script

Prompt: 
> Convert this Python code into modular code by separating different parts into reusable classes, adding comments to methods. It is important to comment on each part of the code so that they can be separated into different files later. Please also use data models using the dataclasses library. Finally, do not use functions to generate car data. Instead, create instances of the dataclass directly.


## Example 2
In the following example, we will test the creation of unit tests for the modules that have been refactored. We will provide GPT-4 with the entirety of the generated code and await the results.

Prompt:
> Generate unit tests

## Example 3
Finally, let us examine how well GPT-4 can generate documentation. The process will be similar to the previous example, except that we will specify the type of documentation we require (markdown) and its intended use
Prompt:

> Write  documentation in Markdown for this code, we will use it in the future to remember how this script works and to be able to reuse the classes in other programs if possible.



## Conclusions
We've discovered that GPT-4 can effectively refactor code with minimal effort, especially for scripts of moderate or low difficulty. Fine-tuning the request is necessary, but it's still useful for training junior developers and students.

As for generating documentation and unit tests, GPT-4 is a viable option with a straightforward prompt and satisfactory results. Since some companies do not produce any documentation or tests, it's better to have basic documentation and tests than none at all, and GPT-4 can provide this.
