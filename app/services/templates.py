from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an e-commerce support assistant."
    ),
    (
        "human",
        "{message}"
    )
])