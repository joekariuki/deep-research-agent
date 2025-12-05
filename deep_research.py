
import gradio as gr
from dotenv import load_dotenv

load_dotenv(override=True)

from research_agents.research_manager import ResearchManager


async def run(query: str):
    async for chunk in ResearchManager().run(query):
        yield chunk

with gr.Blocks() as ui:
    gr.Markdown("# Deep Research")
    query_textbox = gr.Textbox(label="What topic would you like to research?", placeholder="Enter your search query here")
    run_button = gr.Button("Run", variant="primary")
    report = gr.Markdown(label="Report")

    run_button.click(run, inputs=query_textbox, outputs=report)
    query_textbox.submit(run, inputs=query_textbox, outputs=report)


ui.launch(theme=gr.themes.Default(primary_hue="blue"), inbrowser=True)