import streamlit as st
import requests
import time

API_BASE = "http://localhost:8000"

st.set_page_config(page_title="Local GGUF LLM", layout="centered")

st.title("Local GGUF LLM")
st.caption("FastAPI + llama.cpp (CPU)")


st.sidebar.header("Generation Settings")

max_tokens = st.sidebar.slider("Max tokens", 32, 512, 256)
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.15)
top_p = st.sidebar.slider("Top-p", 0.1, 1.0, 0.85)
top_k = st.sidebar.slider("Top-k", 1, 100, 30)

mode = st.sidebar.radio("Mode", ["Chat", "Single Prompt"])


if "messages" not in st.session_state:
    st.session_state.messages = []


if mode == "Chat":
    st.subheader("Chat")

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Type your message")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.markdown(user_input)

        assistant_container = st.chat_message("assistant")
        response_placeholder = assistant_container.empty()

        full_response = ""

        payload = {
            "messages": st.session_state.messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
        }

        start = time.time()
        try:
            with requests.post(
                f"{API_BASE}/chat",
                json=payload,
                stream=True,
                timeout=300,
            ) as r:
                for chunk in r.iter_content(chunk_size=None):
                    if chunk:
                        text = chunk.decode("utf-8")
                        full_response += text
                        response_placeholder.markdown(full_response)

        except Exception as e:
            full_response = f"Error: {e}"
            response_placeholder.markdown(full_response)

        latency = round(time.time() - start, 2)

        response_placeholder.markdown(full_response)
        assistant_container.caption(f"{latency}s")

        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )


else:
    st.subheader("Single Prompt")

    prompt = st.text_area("Prompt", height=150)

    if st.button("Generate"):
        if not prompt.strip():
            st.warning("Please enter a prompt.")
        else:
            payload = {
                "prompt": prompt,
                "max_tokens": max_tokens,
                "temperature": temperature,
                "top_p": top_p,
                "top_k": top_k,
            }

            with st.spinner("Generating..."):
                start = time.time()
                try:
                    r = requests.post(f"{API_BASE}/generate", json=payload, timeout=300)
                    data = r.json()
                    response = data.get("response", "")
                    latency = data.get("latency_sec", round(time.time() - start, 2))
                except Exception as e:
                    response = f"Error: {e}"
                    latency = None

            st.markdown("### Response")
            st.write(response if response else "[No output generated]")
            if latency is not None:
                st.caption(f"{latency}s")
