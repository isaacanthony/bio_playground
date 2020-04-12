"""Align sequences"""
import subprocess
from src.helpers import logger

LOG = logger.getLogger(__name__)


def run(settings: dict):
    """Align sequences"""
    LOG.info('Aligning sequences')

    subprocess.run([
        'augur',
        'align',
        '--sequences',
        f"{settings['data_dir']}/raw/{settings['pipeline']}_sequences.fasta",
        '--output',
        f"{settings['data_dir']}/interim/{settings['pipeline']}_aligned.fasta",
        '--method',
        'mafft',
        '--nthreads',
        'auto',
        '--fill-gaps',
    ])
