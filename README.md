# llm-qwen25

[![PyPI](https://img.shields.io/pypi/v/llm-qwen25.svg)](https://pypi.org/project/llm-qwen25/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/ajayarunachalam/llm-qwen25/blob/main/LICENSE)

Qwen2.5-0.5B.Q8_0 for LLM. 

## Installation

Download the whl file from here [llm_qwen25-0.0.1-py3-none-any.whl](https://drive.google.com/file/d/1qezCUs2Ltg6sqwwdX8ZFvZpNxb97A83V/view?usp=sharing) to your root directory within the virtual environment.
```bash
pip install ./llm_qwen25-0.0.1-py3-none-any.whl
```
## Usage

This plugin bundles a full copy of the [Qwen2.5-0.5B](https://huggingface.co/Qwen/Qwen2.5-0.5B) with a quantized version [Qwen2.5-0.5B.Q8_0.gguf](https://huggingface.co/QuantFactory/Qwen2.5-0.5B-GGUF) model provided by [QuantFactory](https://huggingface.co/QuantFactory).

Once installed, to chat with the model:
```bash
llm chat -m Qwen25
```

## Credits
Inspired from the amazing work of [Simon Willison](https://github.com/simonw)
