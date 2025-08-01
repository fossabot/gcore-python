# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from .insights import (
    InsightsResource,
    AsyncInsightsResource,
    InsightsResourceWithRawResponse,
    AsyncInsightsResourceWithRawResponse,
    InsightsResourceWithStreamingResponse,
    AsyncInsightsResourceWithStreamingResponse,
)
from .policies import (
    PoliciesResource,
    AsyncPoliciesResource,
    PoliciesResourceWithRawResponse,
    AsyncPoliciesResourceWithRawResponse,
    PoliciesResourceWithStreamingResponse,
    AsyncPoliciesResourceWithStreamingResponse,
)
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from .api_paths import (
    APIPathsResource,
    AsyncAPIPathsResource,
    APIPathsResourceWithRawResponse,
    AsyncAPIPathsResourceWithRawResponse,
    APIPathsResourceWithStreamingResponse,
    AsyncAPIPathsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .custom_rules import (
    CustomRulesResource,
    AsyncCustomRulesResource,
    CustomRulesResourceWithRawResponse,
    AsyncCustomRulesResourceWithRawResponse,
    CustomRulesResourceWithStreamingResponse,
    AsyncCustomRulesResourceWithStreamingResponse,
)
from ....pagination import SyncOffsetPage, AsyncOffsetPage
from ....types.waap import WaapDomainStatus, domain_list_params, domain_update_params
from .advanced_rules import (
    AdvancedRulesResource,
    AsyncAdvancedRulesResource,
    AdvancedRulesResourceWithRawResponse,
    AsyncAdvancedRulesResourceWithRawResponse,
    AdvancedRulesResourceWithStreamingResponse,
    AsyncAdvancedRulesResourceWithStreamingResponse,
)
from .firewall_rules import (
    FirewallRulesResource,
    AsyncFirewallRulesResource,
    FirewallRulesResourceWithRawResponse,
    AsyncFirewallRulesResourceWithRawResponse,
    FirewallRulesResourceWithStreamingResponse,
    AsyncFirewallRulesResourceWithStreamingResponse,
)
from ...._base_client import AsyncPaginator, make_request_options
from .api_path_groups import (
    APIPathGroupsResource,
    AsyncAPIPathGroupsResource,
    APIPathGroupsResourceWithRawResponse,
    AsyncAPIPathGroupsResourceWithRawResponse,
    APIPathGroupsResourceWithStreamingResponse,
    AsyncAPIPathGroupsResourceWithStreamingResponse,
)
from .insight_silences import (
    InsightSilencesResource,
    AsyncInsightSilencesResource,
    InsightSilencesResourceWithRawResponse,
    AsyncInsightSilencesResourceWithRawResponse,
    InsightSilencesResourceWithStreamingResponse,
    AsyncInsightSilencesResourceWithStreamingResponse,
)
from .analytics.analytics import (
    AnalyticsResource,
    AsyncAnalyticsResource,
    AnalyticsResourceWithRawResponse,
    AsyncAnalyticsResourceWithRawResponse,
    AnalyticsResourceWithStreamingResponse,
    AsyncAnalyticsResourceWithStreamingResponse,
)
from .api_discovery.api_discovery import (
    APIDiscoveryResource,
    AsyncAPIDiscoveryResource,
    APIDiscoveryResourceWithRawResponse,
    AsyncAPIDiscoveryResourceWithRawResponse,
    APIDiscoveryResourceWithStreamingResponse,
    AsyncAPIDiscoveryResourceWithStreamingResponse,
)
from ....types.waap.waap_domain_status import WaapDomainStatus
from ....types.waap.waap_summary_domain import WaapSummaryDomain
from ....types.waap.waap_detailed_domain import WaapDetailedDomain
from ....types.waap.domain_list_rule_sets_response import DomainListRuleSetsResponse

__all__ = ["DomainsResource", "AsyncDomainsResource"]


class DomainsResource(SyncAPIResource):
    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def api_paths(self) -> APIPathsResource:
        return APIPathsResource(self._client)

    @cached_property
    def api_path_groups(self) -> APIPathGroupsResource:
        return APIPathGroupsResource(self._client)

    @cached_property
    def api_discovery(self) -> APIDiscoveryResource:
        return APIDiscoveryResource(self._client)

    @cached_property
    def insights(self) -> InsightsResource:
        return InsightsResource(self._client)

    @cached_property
    def insight_silences(self) -> InsightSilencesResource:
        return InsightSilencesResource(self._client)

    @cached_property
    def policies(self) -> PoliciesResource:
        return PoliciesResource(self._client)

    @cached_property
    def analytics(self) -> AnalyticsResource:
        return AnalyticsResource(self._client)

    @cached_property
    def custom_rules(self) -> CustomRulesResource:
        return CustomRulesResource(self._client)

    @cached_property
    def firewall_rules(self) -> FirewallRulesResource:
        return FirewallRulesResource(self._client)

    @cached_property
    def advanced_rules(self) -> AdvancedRulesResource:
        return AdvancedRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return DomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return DomainsResourceWithStreamingResponse(self)

    def update(
        self,
        domain_id: int,
        *,
        status: Literal["active", "monitor"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Update Domain

        Args:
          domain_id: The domain ID

          status: Domain statuses that can be used when updating a domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/waap/v1/domains/{domain_id}",
            body=maybe_transform({"status": status}, domain_update_params.DomainUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        ids: Iterable[int] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        ordering: Literal["id", "name", "status", "created_at", "-id", "-name", "-status", "-created_at"]
        | NotGiven = NOT_GIVEN,
        status: WaapDomainStatus | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[WaapSummaryDomain]:
        """
        Retrieve a list of domains associated with the client

        Args:
          ids: Filter domains based on their IDs

          limit: Number of items to return

          name: Filter domains based on the domain name. Supports '\\**' as a wildcard character

          offset: Number of items to skip

          ordering: Sort the response by given field.

          status: The different statuses a domain can have

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/waap/v1/domains",
            page=SyncOffsetPage[WaapSummaryDomain],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "ordering": ordering,
                        "status": status,
                    },
                    domain_list_params.DomainListParams,
                ),
            ),
            model=WaapSummaryDomain,
        )

    def delete(
        self,
        domain_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete an inactive domain by ID.

        Only domains with status 'bypass' can be
        deleted.

        Args:
          domain_id: The domain ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/waap/v1/domains/{domain_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        domain_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaapDetailedDomain:
        """
        Retrieve detailed information about a specific domain

        Args:
          domain_id: The domain ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/waap/v1/domains/{domain_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapDetailedDomain,
        )

    def list_rule_sets(
        self,
        domain_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainListRuleSetsResponse:
        """
        Retrieve all rule sets linked to a particular domain

        Args:
          domain_id: The domain ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/waap/v1/domains/{domain_id}/rule-sets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainListRuleSetsResponse,
        )


class AsyncDomainsResource(AsyncAPIResource):
    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def api_paths(self) -> AsyncAPIPathsResource:
        return AsyncAPIPathsResource(self._client)

    @cached_property
    def api_path_groups(self) -> AsyncAPIPathGroupsResource:
        return AsyncAPIPathGroupsResource(self._client)

    @cached_property
    def api_discovery(self) -> AsyncAPIDiscoveryResource:
        return AsyncAPIDiscoveryResource(self._client)

    @cached_property
    def insights(self) -> AsyncInsightsResource:
        return AsyncInsightsResource(self._client)

    @cached_property
    def insight_silences(self) -> AsyncInsightSilencesResource:
        return AsyncInsightSilencesResource(self._client)

    @cached_property
    def policies(self) -> AsyncPoliciesResource:
        return AsyncPoliciesResource(self._client)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResource:
        return AsyncAnalyticsResource(self._client)

    @cached_property
    def custom_rules(self) -> AsyncCustomRulesResource:
        return AsyncCustomRulesResource(self._client)

    @cached_property
    def firewall_rules(self) -> AsyncFirewallRulesResource:
        return AsyncFirewallRulesResource(self._client)

    @cached_property
    def advanced_rules(self) -> AsyncAdvancedRulesResource:
        return AsyncAdvancedRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/G-Core/gcore-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/G-Core/gcore-python#with_streaming_response
        """
        return AsyncDomainsResourceWithStreamingResponse(self)

    async def update(
        self,
        domain_id: int,
        *,
        status: Literal["active", "monitor"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Update Domain

        Args:
          domain_id: The domain ID

          status: Domain statuses that can be used when updating a domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/waap/v1/domains/{domain_id}",
            body=await async_maybe_transform({"status": status}, domain_update_params.DomainUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        ids: Iterable[int] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        ordering: Literal["id", "name", "status", "created_at", "-id", "-name", "-status", "-created_at"]
        | NotGiven = NOT_GIVEN,
        status: WaapDomainStatus | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WaapSummaryDomain, AsyncOffsetPage[WaapSummaryDomain]]:
        """
        Retrieve a list of domains associated with the client

        Args:
          ids: Filter domains based on their IDs

          limit: Number of items to return

          name: Filter domains based on the domain name. Supports '\\**' as a wildcard character

          offset: Number of items to skip

          ordering: Sort the response by given field.

          status: The different statuses a domain can have

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/waap/v1/domains",
            page=AsyncOffsetPage[WaapSummaryDomain],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ids": ids,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "ordering": ordering,
                        "status": status,
                    },
                    domain_list_params.DomainListParams,
                ),
            ),
            model=WaapSummaryDomain,
        )

    async def delete(
        self,
        domain_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete an inactive domain by ID.

        Only domains with status 'bypass' can be
        deleted.

        Args:
          domain_id: The domain ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/waap/v1/domains/{domain_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        domain_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WaapDetailedDomain:
        """
        Retrieve detailed information about a specific domain

        Args:
          domain_id: The domain ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/waap/v1/domains/{domain_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WaapDetailedDomain,
        )

    async def list_rule_sets(
        self,
        domain_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainListRuleSetsResponse:
        """
        Retrieve all rule sets linked to a particular domain

        Args:
          domain_id: The domain ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/waap/v1/domains/{domain_id}/rule-sets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainListRuleSetsResponse,
        )


class DomainsResourceWithRawResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

        self.update = to_raw_response_wrapper(
            domains.update,
        )
        self.list = to_raw_response_wrapper(
            domains.list,
        )
        self.delete = to_raw_response_wrapper(
            domains.delete,
        )
        self.get = to_raw_response_wrapper(
            domains.get,
        )
        self.list_rule_sets = to_raw_response_wrapper(
            domains.list_rule_sets,
        )

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._domains.settings)

    @cached_property
    def api_paths(self) -> APIPathsResourceWithRawResponse:
        return APIPathsResourceWithRawResponse(self._domains.api_paths)

    @cached_property
    def api_path_groups(self) -> APIPathGroupsResourceWithRawResponse:
        return APIPathGroupsResourceWithRawResponse(self._domains.api_path_groups)

    @cached_property
    def api_discovery(self) -> APIDiscoveryResourceWithRawResponse:
        return APIDiscoveryResourceWithRawResponse(self._domains.api_discovery)

    @cached_property
    def insights(self) -> InsightsResourceWithRawResponse:
        return InsightsResourceWithRawResponse(self._domains.insights)

    @cached_property
    def insight_silences(self) -> InsightSilencesResourceWithRawResponse:
        return InsightSilencesResourceWithRawResponse(self._domains.insight_silences)

    @cached_property
    def policies(self) -> PoliciesResourceWithRawResponse:
        return PoliciesResourceWithRawResponse(self._domains.policies)

    @cached_property
    def analytics(self) -> AnalyticsResourceWithRawResponse:
        return AnalyticsResourceWithRawResponse(self._domains.analytics)

    @cached_property
    def custom_rules(self) -> CustomRulesResourceWithRawResponse:
        return CustomRulesResourceWithRawResponse(self._domains.custom_rules)

    @cached_property
    def firewall_rules(self) -> FirewallRulesResourceWithRawResponse:
        return FirewallRulesResourceWithRawResponse(self._domains.firewall_rules)

    @cached_property
    def advanced_rules(self) -> AdvancedRulesResourceWithRawResponse:
        return AdvancedRulesResourceWithRawResponse(self._domains.advanced_rules)


class AsyncDomainsResourceWithRawResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

        self.update = async_to_raw_response_wrapper(
            domains.update,
        )
        self.list = async_to_raw_response_wrapper(
            domains.list,
        )
        self.delete = async_to_raw_response_wrapper(
            domains.delete,
        )
        self.get = async_to_raw_response_wrapper(
            domains.get,
        )
        self.list_rule_sets = async_to_raw_response_wrapper(
            domains.list_rule_sets,
        )

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._domains.settings)

    @cached_property
    def api_paths(self) -> AsyncAPIPathsResourceWithRawResponse:
        return AsyncAPIPathsResourceWithRawResponse(self._domains.api_paths)

    @cached_property
    def api_path_groups(self) -> AsyncAPIPathGroupsResourceWithRawResponse:
        return AsyncAPIPathGroupsResourceWithRawResponse(self._domains.api_path_groups)

    @cached_property
    def api_discovery(self) -> AsyncAPIDiscoveryResourceWithRawResponse:
        return AsyncAPIDiscoveryResourceWithRawResponse(self._domains.api_discovery)

    @cached_property
    def insights(self) -> AsyncInsightsResourceWithRawResponse:
        return AsyncInsightsResourceWithRawResponse(self._domains.insights)

    @cached_property
    def insight_silences(self) -> AsyncInsightSilencesResourceWithRawResponse:
        return AsyncInsightSilencesResourceWithRawResponse(self._domains.insight_silences)

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithRawResponse:
        return AsyncPoliciesResourceWithRawResponse(self._domains.policies)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithRawResponse:
        return AsyncAnalyticsResourceWithRawResponse(self._domains.analytics)

    @cached_property
    def custom_rules(self) -> AsyncCustomRulesResourceWithRawResponse:
        return AsyncCustomRulesResourceWithRawResponse(self._domains.custom_rules)

    @cached_property
    def firewall_rules(self) -> AsyncFirewallRulesResourceWithRawResponse:
        return AsyncFirewallRulesResourceWithRawResponse(self._domains.firewall_rules)

    @cached_property
    def advanced_rules(self) -> AsyncAdvancedRulesResourceWithRawResponse:
        return AsyncAdvancedRulesResourceWithRawResponse(self._domains.advanced_rules)


class DomainsResourceWithStreamingResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

        self.update = to_streamed_response_wrapper(
            domains.update,
        )
        self.list = to_streamed_response_wrapper(
            domains.list,
        )
        self.delete = to_streamed_response_wrapper(
            domains.delete,
        )
        self.get = to_streamed_response_wrapper(
            domains.get,
        )
        self.list_rule_sets = to_streamed_response_wrapper(
            domains.list_rule_sets,
        )

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._domains.settings)

    @cached_property
    def api_paths(self) -> APIPathsResourceWithStreamingResponse:
        return APIPathsResourceWithStreamingResponse(self._domains.api_paths)

    @cached_property
    def api_path_groups(self) -> APIPathGroupsResourceWithStreamingResponse:
        return APIPathGroupsResourceWithStreamingResponse(self._domains.api_path_groups)

    @cached_property
    def api_discovery(self) -> APIDiscoveryResourceWithStreamingResponse:
        return APIDiscoveryResourceWithStreamingResponse(self._domains.api_discovery)

    @cached_property
    def insights(self) -> InsightsResourceWithStreamingResponse:
        return InsightsResourceWithStreamingResponse(self._domains.insights)

    @cached_property
    def insight_silences(self) -> InsightSilencesResourceWithStreamingResponse:
        return InsightSilencesResourceWithStreamingResponse(self._domains.insight_silences)

    @cached_property
    def policies(self) -> PoliciesResourceWithStreamingResponse:
        return PoliciesResourceWithStreamingResponse(self._domains.policies)

    @cached_property
    def analytics(self) -> AnalyticsResourceWithStreamingResponse:
        return AnalyticsResourceWithStreamingResponse(self._domains.analytics)

    @cached_property
    def custom_rules(self) -> CustomRulesResourceWithStreamingResponse:
        return CustomRulesResourceWithStreamingResponse(self._domains.custom_rules)

    @cached_property
    def firewall_rules(self) -> FirewallRulesResourceWithStreamingResponse:
        return FirewallRulesResourceWithStreamingResponse(self._domains.firewall_rules)

    @cached_property
    def advanced_rules(self) -> AdvancedRulesResourceWithStreamingResponse:
        return AdvancedRulesResourceWithStreamingResponse(self._domains.advanced_rules)


class AsyncDomainsResourceWithStreamingResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

        self.update = async_to_streamed_response_wrapper(
            domains.update,
        )
        self.list = async_to_streamed_response_wrapper(
            domains.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            domains.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            domains.get,
        )
        self.list_rule_sets = async_to_streamed_response_wrapper(
            domains.list_rule_sets,
        )

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._domains.settings)

    @cached_property
    def api_paths(self) -> AsyncAPIPathsResourceWithStreamingResponse:
        return AsyncAPIPathsResourceWithStreamingResponse(self._domains.api_paths)

    @cached_property
    def api_path_groups(self) -> AsyncAPIPathGroupsResourceWithStreamingResponse:
        return AsyncAPIPathGroupsResourceWithStreamingResponse(self._domains.api_path_groups)

    @cached_property
    def api_discovery(self) -> AsyncAPIDiscoveryResourceWithStreamingResponse:
        return AsyncAPIDiscoveryResourceWithStreamingResponse(self._domains.api_discovery)

    @cached_property
    def insights(self) -> AsyncInsightsResourceWithStreamingResponse:
        return AsyncInsightsResourceWithStreamingResponse(self._domains.insights)

    @cached_property
    def insight_silences(self) -> AsyncInsightSilencesResourceWithStreamingResponse:
        return AsyncInsightSilencesResourceWithStreamingResponse(self._domains.insight_silences)

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithStreamingResponse:
        return AsyncPoliciesResourceWithStreamingResponse(self._domains.policies)

    @cached_property
    def analytics(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        return AsyncAnalyticsResourceWithStreamingResponse(self._domains.analytics)

    @cached_property
    def custom_rules(self) -> AsyncCustomRulesResourceWithStreamingResponse:
        return AsyncCustomRulesResourceWithStreamingResponse(self._domains.custom_rules)

    @cached_property
    def firewall_rules(self) -> AsyncFirewallRulesResourceWithStreamingResponse:
        return AsyncFirewallRulesResourceWithStreamingResponse(self._domains.firewall_rules)

    @cached_property
    def advanced_rules(self) -> AsyncAdvancedRulesResourceWithStreamingResponse:
        return AsyncAdvancedRulesResourceWithStreamingResponse(self._domains.advanced_rules)
