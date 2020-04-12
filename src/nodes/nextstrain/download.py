"""Download"""
import subprocess
from src.helpers import logger

LOG = logger.getLogger(__name__)


def run(settings: dict):
    """Download"""
    sequences_file = settings['downloads']['sequences']
    LOG.info(f"Downloading {sequences_file}")

    subprocess.run([
        'wget',
        '-q',
        sequences_file,
        '-O',
        f"{settings['data_dir']}/raw/{settings['pipeline']}_sequences.fasta",
    ])
