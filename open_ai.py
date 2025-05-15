from openai import OpenAI
import time
import streamlit as st


def ask_assistant(question):

    OpenAI.api_key = st.secrets["openai"]["api_key"]
    assistant_id = "asst_G4dQNm038kcoM9RcgfG9ZtVo"

    thread = OpenAI.beta.threads.create() 
    thread_id=thread.id

    OpenAI.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=question,
    )

    run = OpenAI.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id,
        )

    while True:
            run_status = OpenAI.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
            if run_status.status == "completed":
                break
            elif run_status.status in ["failed", "cancelled"]:
                raise Exception(f"Run {run_status.status}")
            time.sleep(1)


    messages = OpenAI.beta.threads.messages.list(thread_id=thread_id)
        
    for msg in reversed(messages.data):  # messages are in reverse order
        if msg.role == "assistant":
            return msg.content[0].text.value

    return "No assistant response found."

