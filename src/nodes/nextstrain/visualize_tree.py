"""Visualize phylo tree"""
from Bio import Phylo
from src.helpers import logger


LOG = logger.getLogger(__name__)


def run(settings: dict):
    """Visualize phylo tree"""
    LOG.info('Visualizing phylo tree')
    prefix = f"{settings['data_dir']}/interim/{settings['pipeline']}"
    tree = Phylo.read(f"{prefix}_tree.nwk", 'newick')

    with open(f"{prefix}_tree.txt", 'w') as file:
        Phylo.draw_ascii(tree, file)
