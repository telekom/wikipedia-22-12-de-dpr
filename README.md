# Wikipedia 22-12 DE DPR

The aim of this project is to provide a German dataset for the training of DPR models.
This way German document retriever models can be trained.

## Prompts

### Short Question

```text
Create a list of 4 very short and simple questions in German language. It must be possible to answer the questions based on the given text.
Each question must have just a few words. The question must not contain the word "and" (German "und").

The given text in German language:

{context}

The list of 4 very short and simple questions in German language:
```

### Normal Questions

```text
Create a list of 4 questions in German language. It must be possible to answer the questions based on the given text. The question must not contain the word "and" (German "und").

The given text in German language:

{context}

The list of 4 questions in German language without the word "and" (German "und"):
```

### Imperative Question

```text
Create a list of 4 very short and simple questions in imperative form. An imperative question is a type of question that is phrased as a command or an instruction. It must be possible to answer the imperative questions based on the given text. Each imperative question must have just a few words. The imperative question must not contain the word "and" (German "und").

The given text in German language:

{context}

The list of 4 very short and simple questions in imperative form and German language:
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
