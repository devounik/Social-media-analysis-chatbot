# app.py
import streamlit as st
from api_handler import LangflowAPI
from config import Config
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)  # Corrected from _name_ to __name__

class ChatApp:
    def __init__(self):
        self.api = LangflowAPI()
        self.setup_streamlit()

    def setup_streamlit(self):
        """Initialize Streamlit configuration and session state"""
        st.set_page_config(
            page_title="AI Chat Assistant",
            page_icon="🤖",
            layout="wide"
        )

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

    def render_chat_history(self):
        """Render the chat history with styling"""
        for chat in reversed(st.session_state.chat_history):
            with st.container():
                # User message
                st.markdown("*You:*")
                st.text_area(
                    label="",
                    value=chat["user"],
                    height=70,
                    disabled=True,
                    key=f"user_{hash(chat['user'])}"
                )

                # Assistant response
                st.markdown("*Assistant:*")
                with st.expander("Response", expanded=True):
                    if isinstance(chat["assistant"], dict):
                        st.json(chat["assistant"])
                    else:
                        st.write(chat["assistant"])

            # Add spacing between messages
            st.markdown("<hr style='margin: 20px 0; opacity: 0.3;'>", unsafe_allow_html=True)

    def handle_user_input(self, user_input: str):
        """Process user input and get API response"""
        try:
            response = self.api.run_flow(
                message=user_input,
                endpoint=Config.ENDPOINT,
                tweaks=Config.TWEAKS
            )

            st.session_state.chat_history.append({
                "user": user_input,
                "assistant": response
            })

        except Exception as e:
            st.error(f"Error: {str(e)}")
            logger.error(f"Error processing user input: {str(e)}")

    def run(self):
        """Main application loop"""
        st.title("AI Chat Assistant")

        # Chat input form
        with st.container():
            with st.form(key="chat_form", clear_on_submit=True):
                cols = st.columns([4, 1])
                with cols[0]:
                    user_input = st.text_input(
                        "Type your message:",
                        key="user_input",
                        placeholder="Enter your message here..."
                    )
                with cols[1]:
                    submit_button = st.form_submit_button(
                        "Send",
                        use_container_width=True
                    )

                if submit_button and user_input:
                    self.handle_user_input(user_input)

        # Display chat history
        with st.container():
            self.render_chat_history()

        # Add custom styling
        st.markdown("""
            <style>
                /* Input area styling */
                .stTextArea textarea {
                    background-color: #f0f2f6;
                    border-radius: 10px;
                    padding: 10px;
                }

                /* Expander styling */
                .streamlit-expanderHeader {
                    background-color: #f0f2f6;
                    border-radius: 10px;
                }

                /* Button styling */
                .stButton > button {
                    border-radius: 20px;
                    padding: 1rem 1rem;
                    background-color: #4CAF50;
                    color: white;
                }

                .stButton > button:hover {
                    background-color: #45a049;
                }

                /* Message container styling */
                .stMarkdown {
                    margin-bottom: 0.5rem;
                }

                /* Disabled text area styling */
                .stTextArea[disabled] textarea {
                    background-color: #f8f9fa;
                    border: 1px solid #e9ecef;
                }
            </style>
        """, unsafe_allow_html=True)

if __name__ == "__main__":  # Corrected from _name_ to __name__
    app = ChatApp()
    app.run()
