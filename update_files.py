"""
Update the files for the assistant.
"""

import os

from pathlib import Path

from openai import OpenAI

data_path = Path("data")
# Get secrets
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")

# Initialise the OpenAI client, and retrieve the assistant
client = OpenAI(api_key=OPENAI_API_KEY)

vector_store = client.beta.vector_stores.create(
    name="Knowledge Base",
)

file_paths = [file for file in data_path.iterdir(
) if file.suffix == ".txt" and file.stem]
file_streams = [file.open("rb") for file in file_paths]

file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id,
    files=file_streams,
)

print(file_batch.status)
print(file_batch.file_counts)

assistant = client.beta.assistants.update(
    assistant_id=ASSISTANT_ID,
    tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)
