# Copyright (c) 2024 Philip May
# This software is distributed under the terms of the MIT license
# which is available at https://opensource.org/licenses/MIT

# python 10_generate_informal_imperative.py --arango-conf config_arangodb_imperative_informal.env --openai-conf config_openai_azure.yaml

"""Generate questions for context with OpenAI LLMs."""

from argparse import ArgumentParser
from dataclasses import asdict
from datetime import datetime
from functools import partial
from typing import Sequence

import backoff
from mltb2.arangodb import ArangoBatchDataManager
from mltb2.db import BatchDataProcessor
from mltb2.openai import OpenAiAzureChat, OpenAiChatResult

PROMPT = """\
Gegeben ist ein Satz im Imperativ. \
Dieser Satz benutzt die formelle Anrede "Sie". \
Wandle den Satz um, sodass er die informelle Anrede ohne "Sie" beinhaltet. \
Erkläre nichts weiter und gib nichts Zusätzliches aus.

Der Satz: Geben Sie das Geburtsjahr von Karl Heinz an.
Der Satz ohne das "Sie": Gebe das Geburtsjahr von Karl Heinz an.

Der Satz: Sagen Sie, welches Modell das iPhone 11 abgelöst hat.
Der Satz ohne das "Sie": Sage, welches Modell das iPhone 11 abgelöst hat.

Der Satz: {sentence}
Der Satz ohne das "Sie":"""


def meta_data_factory():
    """Create meta data for the result."""
    return {
        "script_name": "10_generate_informal_imperative.py",
        "script_version": "1",
        "time": datetime.now().astimezone().isoformat(timespec="seconds"),
    }


def generate(batch: Sequence, open_ai_client) -> Sequence:
    """Generate informal imperative questions."""
    results = []
    for doc in batch:
        llm_response: OpenAiChatResult = open_ai_client(
            prompt=PROMPT.format(sentence=doc["imperative_formal"]),
            completion_kwargs={"temperature": 0.0, "max_tokens": 300},
        )
        result = {
            "_key": doc["_key"],
            "meta_data_informal": meta_data_factory(),
            "llm_response": asdict(llm_response),
        }
        results.append(result)
        print(result)
        print("---")
        print(llm_response.content)
        print()
    return results


@backoff.on_exception(backoff.constant, Exception, max_tries=100, interval=60, jitter=None)
def main() -> None:
    """Main function."""
    # read command line arguments
    argument_parser = ArgumentParser()
    argument_parser.add_argument("--arango-conf", type=str, required=True)
    argument_parser.add_argument("--openai-conf", type=str, required=True)
    args = argument_parser.parse_args()

    # create openai client
    open_ai_azure_chat = OpenAiAzureChat.from_yaml(args.openai_conf)

    # add prompt_type and open_ai_client to generate_normal_questions as partial
    generate_partial = partial(generate, open_ai_client=open_ai_azure_chat)

    # create arango client
    arango_batch_data_manager = ArangoBatchDataManager.from_config_file(
        args.arango_conf,
        aql_overwrite="FOR doc IN @@coll FILTER !HAS(doc, @attribute) SORT RAND() LIMIT @batch_size RETURN doc",
    )
    batch_data_processor = BatchDataProcessor(
        data_manager=arango_batch_data_manager,
        process_batch_callback=generate_partial,
    )
    batch_data_processor.run()


if __name__ == "__main__":
    main()
