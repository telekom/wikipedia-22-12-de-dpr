# Wikipedia 22-12 DE DPR

The goal of this project is to provide a German dataset for training DPR models.
Based on this dataset, German document retrieval models can be trained.

The source of our data is the [German Wikipedia](https://de.wikipedia.org/)
or, to be more precise, the data set
[Cohere/wikipedia-22-12-de-embeddings](https://huggingface.co/datasets/Cohere/wikipedia-22-12-de-embeddings)
from [Cohere](https://cohere.com/).

## Creator

This data set is compiled and open sourced by [Philip May](https://may.la/)
of [Deutsche Telekom](https://www.telekom.de/).

## Dataset Details

### Context Passages

The dataset contains 134,591 context passages.
While we generte the context passages we limit the length of them.
The length is measured with the tokenizer of [`deepset/gbert-base`](https://huggingface.co/deepset/gbert-base).
We limit the maximum token count to 270.
A histogram of the token counts can be found below:

![Histogram of token counts](https://raw.githubusercontent.com/telekom/wikipedia-22-12-de-dpr/main/img/context_token_count_histogram.png)

### Questions

It has a total of 786,353 questions.
That is an average of 5.84 questions per context.
We have a maximum of 6 questions per context.

### Imperative Questions

The dataset also contains 793,143 imperative questions.
An imperative question is a type of question that is phrased as a command or an instruction.
That is an average of 5.89 imperative questions per context.
We have a maximum of 6 imperative questions per context.


### Data Files

- training data (129,591 context passages): `data/wikipedia-22-12-de-train-data.json.gz`
- test data (5,000 context passages): `data/wikipedia-22-12-de-test-data.json.gz`

## Prompts

### Questions

This prompt was executed with GPT-4 and GPT-3.5-turbo.

```text
Create a list of 6 questions in German language. \
It must be possible to answer the questions based on the given text. \
The question must not contain the word "and" (German "und").

The given text in German language:

{context}

The list of 6 different questions in German language without the word "and" (German "und"):
```

### Imperative Question

This prompt was executed with GPT-4.

```text
Create a list of 6 short questions in imperative form. \
An imperative question is a type of question that is phrased as a command or an instruction. \
It must be possible to answer the imperative questions based on the given text. \
The imperative question must not contain the word "and" (German "und").

The given text in German language:

{context}

The list of 6 short questions in imperative form and German language:
```

## Licensing

### The Code and Documentation

Copyright (c) 2023-2024 [Philip May](https://may.la/)

Licensed under the **MIT License** (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License by reviewing the file
[LICENSE](https://github.com/telekom/mltb2/blob/main/LICENSE) in the repository.

### The Wikipedia Texts, Questions and Imperative Questions

The Wikipedia texts are licensed under [CC BY-SA 4.0 Deed](https://creativecommons.org/licenses/by-sa/4.0/deed)
by the corresponding authors of the [German Wikipedia](https://de.wikipedia.org/).
Indication of changes:

- data source is the [Cohere/wikipedia-22-12-de-embeddings](https://huggingface.co/datasets/Cohere/wikipedia-22-12-de-embeddings) dataset on Hugging Face Hub
- we took `wiki_id`, `title` and `text`
- did some normalization and filtering
- and merged the texts to an appropriate token count
- details can be found in the respective notebooks
