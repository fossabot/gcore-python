# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GPUBaremetalClusterDeleteParams"]


class GPUBaremetalClusterDeleteParams(TypedDict, total=False):
    project_id: int

    region_id: int

    delete_floatings: bool
    """True if it is required to delete floating IPs assigned to the servers.

    Can't be used with floatings.
    """

    floatings: str
    """Comma separated list of floating ids that should be deleted.

    Can't be used with `delete_floatings`.
    """

    reserved_fixed_ips: str
    """Comma separated list of port IDs to be deleted with the servers"""
