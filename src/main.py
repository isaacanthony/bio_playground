"""Main entrypoint"""
from sys import argv
from yaml import safe_load
from src.helpers import logger
from src.pipelines import \
    covid, \
    zika

LOG = logger.getLogger(__name__)

PIPELINES = {
    'covid': covid.PIPELINE,
    'zika': zika.PIPELINE,
}


def main():
    """Main entrypoint"""
    # Check for missing params
    if len(argv) < 2:
        LOG.error('Missing pipeline parameter')
        return

    pipelines = argv[1].split(',')

    # Check for invalid params
    for pipeline in pipelines:
        if pipeline not in PIPELINES.keys():
            LOG.error(f"Invalid pipeline parameter: {pipeline}")
            return

    # Run each pipeline
    for pipeline in pipelines:
        LOG.info(f"Running {pipeline} pipeline")

        # Import settings
        settings = safe_load(open('config/base.yml').read())
        settings.update(safe_load(open(f"config/{pipeline}.yml").read()))
        settings['pipeline'] = pipeline

        # Run each node in pipeline
        for node in PIPELINES[pipeline]:
            node.run(settings)


if __name__ == '__main__':
    main()
