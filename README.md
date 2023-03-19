
# Python Code Refactoring, Testing, and Documentation with ChatGPT4

![](https://raw.githubusercontent.com/aaronroman/gpt-coding-test/main/images/header.png)

## Motivation

GPT, a powerful AI model, has the potential to assist software development processes, particularly in tedious and time-consuming tasks such as documentation, unit testing, and refactoring. By conducting simple experiments, we can understand its capabilities and how much time and effort it can save us. While GPT cannot replace human developers, it can certainly streamline certain aspects of software development and help us achieve higher efficiency and quality.

## Example 1

Our first experiment will involve providing GPT-4 with a low-quality spaghetti code example. While simple in nature, this example will be sufficient to gauge whether GPT-4 can effectively perform a refactor by creating modules and comprehending the various parts of the script

Prompt: 
> Convert this Python code into modular code by separating different parts into reusable classes, adding comments to methods. It is important to comment on each part of the code so that they can be separated into different files later. Please also use data models using the dataclasses library. Finally, do not use functions to generate car data. Instead, create instances of the dataclass directly.
>
> ```code here```


## Example 2
In the following example, we will test the creation of unit tests for the modules that have been refactored. We will provide GPT-4 with the entirety of the generated code and await the results.

Prompt:
> Generate unit tests for this code
>
> ```code here```

## Example 3
Finally, let us examine how well GPT-4 can generate documentation. The process will be similar to the previous example, except that we will specify the type of documentation we require (markdown) and its intended use
Prompt:

> Write  documentation in Markdown for this code, we will use it in the future to remember how this script works and to be able to reuse the classes in other programs if possible.
>
> ```code here```



## Conclusions
We have found that with very little effort and at least in scripts of moderate or low difficulty, GPT4 is capable of refactoring the code in a more than satisfactory manner. It is true that the request must be fine-tuned, but it is perfectly usable for training tasks or doubts in junior developers or students, for example.

Regarding the generation of documentation and unit tests, I believe it is perfectly usable. The prompt is very straightforward and the result is more than sufficient. Considering that many companies do not generate unit tests or documentation, it is viable to at least have simple documentation and simple tests rather than having nothing, and GPT-4 seems more than sufficient for this purpose.
