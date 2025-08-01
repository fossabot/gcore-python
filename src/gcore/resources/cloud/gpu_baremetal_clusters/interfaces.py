# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.cloud.network_interface_list import NetworkInterfaceList

__all__ = ["InterfacesResource", "AsyncInterfacesResource"]


class InterfacesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InterfacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return InterfacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InterfacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return InterfacesResourceWithStreamingResponse(self)

    def list(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NetworkInterfaceList:
        """
        Retrieve a list of network interfaces attached to the GPU cluster servers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return self._get(
            f"/cloud/v1/ai/clusters/{project_id}/{region_id}/{cluster_id}/interfaces",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkInterfaceList,
        )


class AsyncInterfacesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInterfacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInterfacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInterfacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncInterfacesResourceWithStreamingResponse(self)

    async def list(
        self,
        cluster_id: str,
        *,
        project_id: int | None = None,
        region_id: int | None = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NetworkInterfaceList:
        """
        Retrieve a list of network interfaces attached to the GPU cluster servers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if project_id is None:
            project_id = self._client._get_cloud_project_id_path_param()
        if region_id is None:
            region_id = self._client._get_cloud_region_id_path_param()
        if not cluster_id:
            raise ValueError(f"Expected a non-empty value for `cluster_id` but received {cluster_id!r}")
        return await self._get(
            f"/cloud/v1/ai/clusters/{project_id}/{region_id}/{cluster_id}/interfaces",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkInterfaceList,
        )


class InterfacesResourceWithRawResponse:
    def __init__(self, interfaces: InterfacesResource) -> None:
        self._interfaces = interfaces

        self.list = to_raw_response_wrapper(
            interfaces.list,
        )


class AsyncInterfacesResourceWithRawResponse:
    def __init__(self, interfaces: AsyncInterfacesResource) -> None:
        self._interfaces = interfaces

        self.list = async_to_raw_response_wrapper(
            interfaces.list,
        )


class InterfacesResourceWithStreamingResponse:
    def __init__(self, interfaces: InterfacesResource) -> None:
        self._interfaces = interfaces

        self.list = to_streamed_response_wrapper(
            interfaces.list,
        )


class AsyncInterfacesResourceWithStreamingResponse:
    def __init__(self, interfaces: AsyncInterfacesResource) -> None:
        self._interfaces = interfaces

        self.list = async_to_streamed_response_wrapper(
            interfaces.list,
        )
