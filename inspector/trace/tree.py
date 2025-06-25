"""
inspector.trace.tree

Generates tree-style prefixes for visualizing nested call flows.
"""

def get_tree_prefix(depth: int, is_entering: bool) -> str:
    """
    Generate a visual prefix for function call tracing, forming a tree-like hierarchy.

    Args:
        depth (int): Current call stack depth (0 for root).
        is_entering (bool): Whether this prefix is for a function entry (True) or exit (False).

    Returns:
        str: A formatted string representing the tree structure at this level.
    """
    # Root level: return standalone icon or final branch
    if depth == 0:
        return "🔍 " if is_entering else "└─ "

    # Indent with vertical bars for each parent depth
    prefix = "│  " * depth

    # Append entry or exit marker
    return prefix + ("├─ 🔍 " if is_entering else "└─ ")
