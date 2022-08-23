import logging

from .adapters import UnderscoreToHyphenAdapter
from .transformers import HyphenSpaceTransformer, UnderscoreTransformer
from ..base import StructuralDemoService

LOGGER = logging.getLogger(__name__)


class AdapterStructuralDemoService(StructuralDemoService):
    """
    Class for demonstrating the adapter pattern.
    """

    _hyphen = HyphenSpaceTransformer = None
    _under = UnderscoreTransformer = None
    _under_adapt = UnderscoreToHyphenAdapter = None

    def _create_transformers_and_adapters(self) -> None:
        """
        Private method for setting up the transformers and adapters.
        """

        LOGGER.info('Setting up transformers.')
        self._hyphen = HyphenSpaceTransformer()
        self._under = UnderscoreTransformer()
        self._under_adapt = UnderscoreToHyphenAdapter()

    def _do_transform_and_adapt(self) -> None:
        """
        Private method for attempting to transform the string using the transformers and adapters.
        """

        _input = 'This string has a lot of space.'
        LOGGER.info(f'Input: {_input}')

        LOGGER.info('Transforming using HyphenSpaceTransformer...')
        output = self._hyphen.transform(_input)
        LOGGER.info(f'Output: {output}')

        LOGGER.info('Transforming using UnderscoreTransformer...')
        output = self._under.convert_to_hyphen(_input)
        LOGGER.info(f'Output: {output}')

        LOGGER.info(f'Outputs are not the same. We want uniform output.')

        LOGGER.info('Transforming using UnderscoreSpaceTransformerAdapter...')
        output = self._under_adapt.transform(_input)
        LOGGER.info(f'Output: {output}')

        LOGGER.info(f'Outputs are now the same.')

    def execute(self) -> None:
        """
        Method for executing the demo routine of the adapter pattern.
          - Creates transformers and adapters.
          - Transforms the string using transformers and adapters.
        """

        LOGGER.info('Executing demo routine...')
        self._create_transformers_and_adapters()
        self._do_transform_and_adapt()
        LOGGER.info('Demo routine Finished.')
