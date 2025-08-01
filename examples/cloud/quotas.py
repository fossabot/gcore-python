import os
from typing import Any, Union, Sequence

from gcore import Gcore
from gcore.types.cloud.quota_get_all_response import GlobalQuotas, RegionalQuota
from gcore.types.cloud.quota_get_global_response import QuotaGetGlobalResponse
from gcore.types.cloud.quota_get_by_region_response import QuotaGetByRegionResponse


def main() -> None:
    # TODO set API key before running
    # api_key = os.environ["GCORE_API_KEY"]
    # TODO set cloud project ID before running
    # cloud_project_id = os.environ["GCORE_CLOUD_PROJECT_ID"]
    # TODO set cloud region ID before running
    # cloud_region_id = os.environ["GCORE_CLOUD_REGION_ID"]

    gcore_client_id = int(os.environ["GCORE_CLIENT_ID"])

    gcore = Gcore(
        # No need to explicitly pass to Gcore constructor if using environment variables
        # api_key=api_key,
        # cloud_project_id=cloud_project_id,
        # cloud_region_id=cloud_region_id,
    )

    get_all_quotas(client=gcore)
    get_regional_quotas(client=gcore, client_id=gcore_client_id)
    get_global_quotas(client=gcore, client_id=gcore_client_id)


def get_all_quotas(*, client: Gcore) -> None:
    print("\n=== GET ALL QUOTAS ===")
    all_quotas = client.cloud.quotas.get_all()

    if all_quotas.global_quotas:
        print("\n--- Global Quotas ---")
        _print_global_quotas(all_quotas.global_quotas)

    if all_quotas.regional_quotas:
        print("\n--- Regional Quotas ---")
        _print_regional_quotas(all_quotas.regional_quotas)

    print("========================")


def get_regional_quotas(*, client: Gcore, client_id: int) -> None:
    print(f"\n=== GET REGIONAL QUOTAS ===")
    regional_quota = client.cloud.quotas.get_by_region(client_id=client_id)
    _print_regional_quotas([regional_quota])
    print("========================")


def get_global_quotas(*, client: Gcore, client_id: int) -> None:
    print(f"\n=== GET GLOBAL QUOTAS ===")
    global_quota = client.cloud.quotas.get_global(client_id)
    _print_global_quotas(global_quota)
    print("========================")


def _print_global_quotas(global_quotas: Union[GlobalQuotas, QuotaGetGlobalResponse]) -> None:
    # Show only first 3 fields
    fields = list(global_quotas.__dict__.items())
    _print_truncated_fields(fields)


def _print_regional_quotas(regional_quotas: Sequence[Union[RegionalQuota, QuotaGetByRegionResponse]]) -> None:
    display_count = 3
    if len(regional_quotas) < display_count:
        display_count = len(regional_quotas)

    for idx in range(display_count):
        region = regional_quotas[idx]
        print(f"Region #{idx + 1}: region_id={region.region_id}")

        # Show only first 3 fields (excluding region_id)
        fields = [(field, value) for field, value in region.__dict__.items() if field != "region_id"]
        _print_truncated_fields(fields, indent="  ")

    if len(regional_quotas) > display_count:
        print()
        print(f"... and {len(regional_quotas) - display_count} more regions")


def _print_truncated_fields(fields: "list[tuple[str, Any]]", *, display_limit: int = 3, indent: str = "") -> None:
    display_count = display_limit
    if len(fields) < display_count:
        display_count = len(fields)

    for i in range(display_count):
        field, value = fields[i]
        print(f"{indent}{field}: {value}")

    if len(fields) > display_count:
        print(f"{indent}... and {len(fields) - display_count} more quota fields")


if __name__ == "__main__":
    main()
