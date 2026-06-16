from dotenv import load_dotenv
from langfuse import Langfuse

load_dotenv()

langfuse = Langfuse()

print("AUTH:", langfuse.auth_check())

trace = langfuse.trace(
    name="manual-test"
)

print("TRACE CREATED")

langfuse.flush()

print("FLUSHED")