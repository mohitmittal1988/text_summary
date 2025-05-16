import validators
import streamlit as st
from langchain.prompts  import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import   UnstructuredURLLoader, UnstructuredPDFLoader
import re
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.docstore.document import Document



# Streamlit APP
st.set_page_config(page_title="TXTSUM: Summarize TEXT From YT, Website or PDF", page_icon="🦜")
st.title("🦜TEXT SUMMARIZER🦜 Youtube URL or Website  ")
st.subheader('summarize URL')


## Get the Groq API Key and url(YT or website)to be summarized
with st.sidebar:
    groq_api_key=st.text_input("Groq API Key",value="",type="password")

generic_url=st.text_input("URL",label_visibility="collapsed")

## llama 3 Model USsing Groq API
llm = ChatGroq(model="llama3-8b-8192", groq_api_key=groq_api_key)

prompt_template="""
Provide a summary of the following content in 300 words:
Content:{text}

"""
prompt=PromptTemplate(template=prompt_template,input_variables=["text"])


if st.button("Summarize the Content from YT or Website"):
    # Validate all inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL (YouTube or website)")
    elif "youtube.com" in generic_url and "list=" in generic_url:
        st.warning("Playlist links are not supported. Only individual YouTube videos are allowed.")
    else:
        try:
            with st.spinner("Fetching content..."):
                docs = None  # Initialize docs

                if "youtube.com" in generic_url:
                    video_id = re.search(r"v=([a-zA-Z0-9_-]+)", generic_url)
                    if video_id:
                        video_id = video_id.group(1)
                        try:
                            transcript = YouTubeTranscriptApi.get_transcript(video_id)
                            text = " ".join([entry["text"] for entry in transcript])
                            docs = [Document(page_content=text)]
                        except Exception as yt_error:
                            st.error("⚠️ Could not fetch transcript. The video may not have captions.")
                            st.stop()
                    else:
                        st.error("⚠️ Could not extract YouTube video ID.")
                        st.stop()

                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=False,
                        headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
                        }
                    )
                    docs = loader.load()

                # ✅ Only truncate if docs is valid
                if docs and len(docs) > 0:
                    max_chars = 12000
                    docs[0].page_content = docs[0].page_content[:max_chars]

                    # Summarization Chain
                    chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                    output_summary = chain.run(docs)
                    st.success(output_summary)
                else:
                    st.error("⚠️ No content found to summarize.")
        except Exception as e:
            st.exception(f"Exception: {e}")
