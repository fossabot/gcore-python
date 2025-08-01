# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["IPInfoGetCountsParams"]


class IPInfoGetCountsParams(TypedDict, total=False):
    ip: Required[str]
    """The IP address to check"""

    domain_id: int
    """The identifier for a domain.

    When specified, the response will exclusively contain data pertinent to the
    indicated domain, filtering out information from other domains.
    """
