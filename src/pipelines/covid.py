"""COVID-19 pipeline"""
from src.nodes.nextstrain import \
    align, \
    construct_tree, \
    download, \
    visualize_tree

PIPELINE = [
    download,
    align,
    construct_tree,
    visualize_tree,
]
