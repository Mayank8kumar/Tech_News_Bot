from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm_response(context: str, question: str):
    prompt_template = """
You are a helpful assistant who analyzes how a tech article is relevant to a person's resume and career.

Use the resume as background and the news article as context to explain the potential impact.

Resume:
{context}

Tech News:
{question}

Instructions:
- Be specific and career-focused.
- If there's no clear connection, reply: "This article may not be directly related to your current profile, but could be of general interest."

Answer:
"""

    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain.run({"input_documents": [], "context": context, "question": question})
