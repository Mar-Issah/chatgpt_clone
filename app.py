import streamlit as st
# from utils import get_response
from streamlit_chat import message

def main():
	# set page congigurations
     st.set_page_config(page_title="ChatGPT Clone",
                              page_icon='🤖💬',
                              layout='centered',
                               initial_sidebar_state='expanded')

     st.markdown("<h3 style='text-align: center;'>How can I assist you? </h3>", unsafe_allow_html=True)

     # Initialize the Application state. A state to hold the conversation summary and messages b/n AI and Human
     if 'conversation' not in st.session_state:
          st.session_state['conversation'] = None
     if 'messages' not in st.session_state:
          st.session_state['messages'] =[]

     # sidebarbar UI below
     # disable the btn when there are no messages
     with st.sidebar:
          st.title("📄💬➡️🔍")
          st.write("Click the button below to obtain a summary of your chat.")
          summarise_btn = st.button("Summarise the conversation", key="summarise", type="secondary")

          if summarise_btn:
               summarise_placeholder = st.write("Below is the summary of our conversation ❤️:\n\n"+st.session_state['conversation'].memory.buffer)


     response_container = st.container()
     # Here we will have a container for user input text box
     container = st.container()

     prompt = st.chat_input("Enter a prompt here")
     if prompt:
          # Append the user's prompt and by the AI's repsonse
          st.session_state['messages'].append(prompt)
        #   model_response=get_response(prompt)
        #   st.session_state['messages'].append(model_response)

		# Finally display the user message and AI message
          with response_container:
               st.download_button(
				label="Download data as CSV",
				data=st.session_state['messages'],
				file_name='large_df.csv',
				mime='text',
			)
               for i in range(len(st.session_state['messages'])):
                    if (i % 2) == 0:
                         message(st.session_state['messages'][i], is_user=True, key=str(i) + '_user')
                    else:
                         message(st.session_state['messages'][i], key=str(i) + '_AI')

if __name__ == "__main__":
	main()