"""Construct phylo tree"""
import subprocess
from src.helpers import logger

LOG = logger.getLogger(__name__)


def run(settings: dict):
    """Construct phylo tree"""
    LOG.info('Constructing phylo tree')

    subprocess.run([
        'augur',
        'tree',
        '--alignment',
        f"{settings['data_dir']}/interim/{settings['pipeline']}_aligned.fasta",
        '--output',
        f"{settings['data_dir']}/interim/{settings['pipeline']}_tree.nwk",
        '--method',
        'iqtree',
        '--nthreads',
        'auto',
    ])
