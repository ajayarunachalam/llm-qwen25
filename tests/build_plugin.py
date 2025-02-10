from llama_cpp import Llama
from pprint import pprint
llm = Llama(model_path="llm-qwen25\llm_qwen25\Qwen2.5-0.5B.Q8_0.gguf")
output = llm.create_chat_completion(messages=[
    {"role": "user", "content": "Hi"}
])
pprint(output)

