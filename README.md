# Wikipedia 22-12 DE DPR

The goal of this project is to provide a German dataset for DPR model training.
DPR (Dense Passage Retrieval) is one of the most important components of RAG applications.
Based on this dataset, German document retrieval models can be trained.

The unique feature of this data set is that it contains not only training data for questions,
but also imperative questions.
An imperative question is a type of question that is phrased as a command or an instruction.
Since there is a formal and informal form of address in German, both cases are included in the case of imperative questions.

The source of our data is the [German Wikipedia](https://de.wikipedia.org/)
or, to be more precise, the data set
[Cohere/wikipedia-22-12-de-embeddings](https://huggingface.co/datasets/Cohere/wikipedia-22-12-de-embeddings)
from [Cohere](https://cohere.com/).

## Creator

This data set is compiled and open sourced by [Philip May](https://may.la/)
of [Deutsche Telekom](https://www.telekom.de/).

## Dataset Details

### Context Passages

The dataset contains 134,591 context passages in total (train + test).
While we select the context passages we limit the length of them.
The length is measured with the tokenizer of [`deepset/gbert-base`](https://huggingface.co/deepset/gbert-base).
We limit the maximum token count to 270.
A histogram of the context token counts can be found below:

![Histogram of token counts](https://raw.githubusercontent.com/telekom/wikipedia-22-12-de-dpr/main/img/context_token_count_histogram.png)

We are aware that there is a tendency to train and publish embedding models with ever increasing context lengths.
However, we are of the opinion that the retrieval performance becomes too poor if the context is too large.
We draw the line at 270 tokens.
More on this topic, especially from [Nils Reimers](https://www.nils-reimers.de/) in the discussion of this
[LinkedIn post](https://www.linkedin.com/posts/davidmezzetti_togethercomputerm2-bert-80m-32k-retrieval-activity-7152332060303491072-utpW).

### Questions

The dataset has a total (train + test) of 786,353 questions.
That is an average of 5.84 questions per context.
We have a maximum of 6 questions per context.

### Formal Imperative Questions

The dataset contains 793,143 formal imperative questions (train + test).
An imperative question is a type of question that is phrased as a command or an instruction.
That is an average of 5.89 formal imperative questions per context.
We have a maximum of 6 formal imperative questions per context.

### Informal Imperative Questions

The dataset contains ??? informal imperative questions (train + test).
An imperative question is a type of question that is phrased as a command or an instruction.
That is an average of ??? informal imperative questions per context.
We have a maximum of 6 formal imperative questions per context.

### Data Files

#### Version 2

- training data (129,591 context passages): `data/wikipedia-22-12-de-train-data-v2.json.gz`
- test data (5,000 context passages): `data/wikipedia-22-12-de-test-data-v2.json.gz`

#### Version 1 (outdated)

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

### Convert formal Imperative Question to informal Form

```text
Gegeben ist ein Satz im Imperativ. \
Dieser Satz benutzt die formelle Anrede "Sie". \
Wandle den Satz um, sodass er die informelle Anrede ohne "Sie" beinhaltet. \
Erkläre nichts weiter und gib nichts Zusätzliches aus.

Der Satz: Geben Sie das Geburtsjahr von Karl Heinz an.
Der Satz ohne das "Sie": Gebe das Geburtsjahr von Karl Heinz an.

Der Satz: Sagen Sie, welches Modell das iPhone 11 abgelöst hat.
Der Satz ohne das "Sie": Sage, welches Modell das iPhone 11 abgelöst hat.

Der Satz: {sentence}
Der Satz ohne das "Sie":
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
