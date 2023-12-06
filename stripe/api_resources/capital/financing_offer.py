# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import TYPE_CHECKING
from warnings import warn

warn(
    """
    The stripe.api_resources.capital.financing_offer package is deprecated, please change your
    imports to import from stripe.capital directly.
    From:
      from stripe.api_resources.capital.financing_offer import FinancingOffer
    To:
      from stripe.capital import FinancingOffer
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.capital._financing_offer import (  # noqa
        FinancingOffer,
    )
