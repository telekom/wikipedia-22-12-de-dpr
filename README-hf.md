# Wikipedia 22-12 DE DPR

For details about this dataset please see
[telekom/wikipedia-22-12-de-dpr](https://github.com/telekom/wikipedia-22-12-de-dpr)
on GitHub.

## Creator

This data set is compiled and open sourced by [Philip May](https://may.la/)
of [Deutsche Telekom](https://www.telekom.de/).

## Licensing

### The Code and Documentation

Copyright (c) 2023-2024 [Philip May](https://may.la/), [Deutsche Telekom AG](https://www.telekom.de/)

Licensed under the **MIT License** (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License by reviewing the file
[LICENSE](https://github.com/telekom/mltb2/blob/main/LICENSE) in the repository.

### The Wikipedia Texts, Questions and Imperative Questions

The Wikipedia texts are licensed under [CC BY-SA 4.0 Deed](https://creativecommons.org/licenses/by-sa/4.0/deed)
by the corresponding authors of the [German Wikipedia](https://de.wikipedia.org/). The questions and
imperative questions are copyright ([CC BY-SA 4.0 Deed](https://creativecommons.org/licenses/by-sa/4.0/deed)) by
[Philip May](https://may.la/), [Deutsche Telekom AG](https://www.telekom.de/).
Indication of changes:

- data source is the [Cohere/wikipedia-22-12-de-embeddings](https://huggingface.co/datasets/Cohere/wikipedia-22-12-de-embeddings) dataset on Hugging Face Hub
- we took `wiki_id`, `title` and `text`
- did some normalization and filtering
- and merged the texts to an appropriate token count
- details can be found in the respective notebooks
