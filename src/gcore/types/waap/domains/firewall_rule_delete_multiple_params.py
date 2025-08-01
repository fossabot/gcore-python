# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["FirewallRuleDeleteMultipleParams"]


class FirewallRuleDeleteMultipleParams(TypedDict, total=False):
    rule_ids: Required[Iterable[int]]
    """The IDs of the rules to delete"""
