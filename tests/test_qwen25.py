import llm
import pytest


@pytest.mark.parametrize("no_stream", (False, True))
def test_model(no_stream):
    model = llm.get_model("Qwen25")
    kwargs = {}
    if no_stream:
        kwargs["stream"] = False
    response = model.prompt("The capital of India is", **kwargs)
    assert "New Delhi" or "Delhi" in response.text().lower()
