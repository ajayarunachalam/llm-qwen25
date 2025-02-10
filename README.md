# llm-qwen25

[![PyPI](https://img.shields.io/pypi/v/llm-qwen25.svg)](https://pypi.org/project/llm-qwen25/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/ajayarunachalam/llm-qwen25/blob/main/LICENSE)

Qwen2.5-0.5B.Q8_0 for LLM. 

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).
```bash
llm install llm-qwen25
```
If you have [uv](https://github.com/astral-sh/uv) installed you can chat with the model without any installation step like this:
```bash
uvx --with llm-qwen25 llm chat -m Qwen25
```
## Usage

This plugin bundles a full copy of the [Qwen2.5-0.5B](https://huggingface.co/Qwen/Qwen2.5-0.5B) quantized version of the [Qwen2.5-0.5B.Q8_0.gguf](https://huggingface.co/QuantFactory/Qwen2.5-0.5B-GGUF) model by [QuantFactory](https://huggingface.co/QuantFactory).

Once installed, run the model like this:
```bash
llm -m Qwen25 'Hi'
```
Or to chat with the model (keeping it resident in memory):
```bash
llm chat -m Qwen25
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-qwen25
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
llm install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```

## Credits
Inspired from the amazing work of [Simon Willison](https://github.com/simonw)
