""" This file is for testing llama indices."""

from llama_index.core import Settings
from llama_index.embeddings.llamafile import LlamafileEmbedding
from llama_index.llms.llamafile import Llamafile
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import SimpleDirectoryReader
from llama_index.core import StorageContext, load_index_from_storage

Settings.embed_model = LlamafileEmbedding(base_url="http://1.1.1.1:8080", request_timeout=8000)

Settings.llm = Llamafile(
    base_url="http://1.1.1.1:8080",
    temperature=0,
    seed=0
)

# Also set up a sentence splitter to ensure texts are broken into semantically-meaningful
# chunks (sentences) that don't take up the model's entire context window (2048 tokens).
# Since these chunks will be added to LLM prompts as part of the RAG process, we want to
# leave plenty of space for both the system prompt and the user's actual question.
Settings.transformations = [
    SentenceSplitter(
        chunk_size=256,
        chunk_overlap=5
    )
]

# Load local data
local_doc_reader = SimpleDirectoryReader(input_dir='./data')
docs = local_doc_reader.load_data(show_progress=True)

# # We'll load some Wikipedia pages as well
# from llama_index.readers.web import SimpleWebPageReader
# urls = [
#     'https://en.wikipedia.org/wiki/Homing_pigeon',
#     'https://en.wikipedia.org/wiki/Magnetoreception',
# ]
# web_reader = SimpleWebPageReader(html_to_text=True)
# docs.extend(web_reader.load_data(urls))

# # Build the index
# from llama_index.core import VectorStoreIndex

# index = VectorStoreIndex.from_documents(
#     docs,
#     show_progress=True,
# )
# # Save the index
# index.storage_context.persist(persist_dir="./storage")


# Rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="./storage")

# Load index from the storage context
index = load_index_from_storage(storage_context)



query_engine = index.as_query_engine()

print(query_engine.query("What were homing pigeons used for?"))
