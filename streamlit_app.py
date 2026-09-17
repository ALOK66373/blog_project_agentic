import streamlit as st

from src.graphs.graph_builder import GraphBuilder
from src.llms.groqllm import GroqLLM


st.set_page_config(
    page_title="Blog Studio",
    page_icon="✍",
    layout="centered",
)

st.title("Blog Studio")
st.caption("Turn an idea into a structured Markdown blog post.")

with st.form("blog_form"):
    topic = st.text_input(
        "Blog topic",
        placeholder="For example: How AI is changing education",
    )
    submitted = st.form_submit_button("Generate blog", type="primary")

if submitted:
    if not topic.strip():
        st.warning("Enter a topic before generating a blog.")
    else:
        try:
            with st.spinner("Writing your blog..."):
                llm = GroqLLM().get_llm()
                graph = GraphBuilder(llm).setup_graph(usecase="topic")
                result = graph.invoke({"topic": topic.strip()})
                blog = result["blog"]

            st.success("Blog generated")
            st.subheader(blog["title"])
            st.markdown(blog["content"])

            st.download_button(
                "Download Markdown",
                data=f"# {blog['title']}\n\n{blog['content']}",
                file_name="generated_blog.md",
                mime="text/markdown",
            )
        except ValueError as error:
            st.error(str(error))
        except Exception:
            st.error("Blog generation failed. Check the server terminal for details.")
