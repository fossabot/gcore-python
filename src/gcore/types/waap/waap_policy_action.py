# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["WaapPolicyAction"]

WaapPolicyAction: TypeAlias = Literal["Allow", "Block", "Captcha", "Gateway", "Handshake", "Monitor", "Composite"]
