import g4f
import streamlit as st


def get_gpt3_response(messages: list) -> str:
    response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    stream=False,
    )

    return response

def main():
    st.title("GPT4Free Demo")

    # Session state for retaining messages
    if 'messages' not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "私はAIアシスタントです。何かお手伝いしましょうか？"}]

    # Placeholder for chat history
    chat_history_placeholder = st.container()

    # Input for the user message
    user_message = st.text_input("Your Message")

    # If user has entered a new message
    if user_message:
        st.session_state.messages.append({"role": "user", "content": user_message})
        gpt3_response = get_gpt3_response(st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": gpt3_response})

    # Display chat history within the placeholder
    with chat_history_placeholder :
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.info(f"{message['content']}", icon = "🙂")
            elif message["role"] == "assistant":
                st.info(f"{message['content']}", icon = "🤖")


if __name__ == "__main__":
    main()
