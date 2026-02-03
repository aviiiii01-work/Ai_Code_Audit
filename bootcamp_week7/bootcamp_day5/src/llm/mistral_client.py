import subprocess

class MistralLLM:
    def generate(self, prompt: str) -> str:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt,
            text=True,
            capture_output=True
        )
        return result.stdout.strip()
    