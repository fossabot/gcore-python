# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SecretDeleteParams"]


class SecretDeleteParams(TypedDict, total=False):
    force: bool
    """Force delete secret even if it is used in slots"""
