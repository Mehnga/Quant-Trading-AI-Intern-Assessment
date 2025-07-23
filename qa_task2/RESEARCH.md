# RESEARCH.md

## Comparison of TinyLlama and TinyGPT2

As a beginner, I wanted to choose a small and easy-to-use AI model for generating text summaries. I compared two popular lightweight models: **TinyLlama** and **TinyGPT2**. Here are my findings:

### TinyLlama
- Based on the Llama architecture, which is known for strong performance on many tasks.
- Usually requires more resources (RAM, VRAM) compared to TinyGPT2, even in its smallest versions.
- May not be as widely supported in the Hugging Face Transformers library as GPT2-based models.
- Sometimes harder to run on a regular laptop or without a GPU.
- Community support and tutorials are still growing, but not as extensive as GPT2.

### TinyGPT2 (sshleifer/tiny-gpt2)
- Based on the GPT2 architecture, which is very popular and well-documented.
- Extremely lightweight and fast, designed for testing and quick prototyping.
- Runs easily on CPUs and low-resource machines (like laptops) without needing a GPU.
- Excellent support in the Hugging Face Transformers library.
- Lots of beginner-friendly tutorials and community help available.
- Output quality is basic, but good enough for simple tasks and learning purposes.

## Why I Chose TinyGPT2
- **Easy to use:** TinyGPT2 works out-of-the-box with the Transformers library and is simple to set up.
- **Low resource requirements:** It runs smoothly on my laptop without a GPU.
- **Great for learning:** There are many guides and examples for beginners.
- **Sufficient for my project:** For generating short summaries, TinyGPT2 is fast and good enough.

**In summary:** While TinyLlama is promising, TinyGPT2 is more accessible and practical for beginners and small projects like mine. 