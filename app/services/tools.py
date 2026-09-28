from langchain_core.tools import tool
from app.services.llm_provider import llm

@tool
def get_order(order_id: int) -> dict:
    """Get order information using the order ID."""

    orders = {
        123: {
            "status": "shipped",
            "delivery": "2026-09-30"
        },
        456: {
            "status": "processing",
            "delivery": "2026-10-02"
        }
    }

    return orders.get(
        order_id,
        {"error": "Order not found"}
    )


TOOLS = [
    get_order,
]


TOOL_MAP = {
    tool.name: tool
    for tool in TOOLS
}

llm_with_tools = llm.bind_tools(TOOLS)