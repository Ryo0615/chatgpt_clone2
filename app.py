import g4f
import streamlit as st
import requests

def generate_g4f_response(messages: list) -> str:
    try:
        response_stream = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            stream=True
        )

        response = "".join([message for message in response_stream])
    except requests.HTTPError as e:
        st.markdown(f"{e} - {e.response.text}")
        return ""
    return response

def main():
    st.title("Chat with ChatGPT Clone!")

    # Session state for retaining messages
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(f"{message['content']}")

    # Input for the user message
    user_message = st.chat_input("Your Message")

    # React to user input
    if user_message:
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(f"{user_message}")
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_message})

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            for char in generate_g4f_response([{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]):
                full_response += char
                message_placeholder.markdown(full_response + "❙")

            message_placeholder.markdown(full_response)

        st.session_state.messages.append({"role": "assistant", "content": full_response})


if __name__ == "__main__":
    main()
