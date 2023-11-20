# pyright: strict
import stripe


def test_can_import_stripe_object() -> None:
    from stripe.stripe_object import (
        StripeObject as StripeObjectFromStripeStripeObject,
    )

    assert (
        stripe.stripe_object.StripeObject is StripeObjectFromStripeStripeObject
    )


def test_can_import_webhook_members() -> None:
    from stripe import (
        Webhook,
        WebhookSignature,
    )

    assert Webhook is not None
    assert WebhookSignature is not None


def test_can_import_list_search_objects() -> None:
    from stripe.api_resources import (
        ListObject as ListObjectFromApiResources,
        SearchResultObject as SearchObjectFromApiResources,
    )
    from stripe.stripe_object import (
        StripeObject,
    )

    assert (
        ListObjectFromApiResources[StripeObject]
        == stripe.ListObject[StripeObject]
    )
    assert (
        SearchObjectFromApiResources[StripeObject]
        == stripe.SearchResultObject[StripeObject]
    )


def test_can_import_misc_resources() -> None:
    from stripe.api_resources import ErrorObject, OAuthErrorObject, FileUpload

    assert ErrorObject is stripe.ErrorObject
    assert OAuthErrorObject is stripe.OAuthErrorObject
    assert FileUpload is stripe.FileUpload


def test_can_import_abstract() -> None:
    from stripe.api_resources.abstract import (
        APIResource as APIResourceFromAbstract,
        SingletonAPIResource as SingletonAPIResourceFromAbstract,
        CreateableAPIResource as CreateableAPIResourceFromAbstract,
        UpdateableAPIResource as UpdateableAPIResourceFromAbstract,
        DeletableAPIResource as DeletableAPIResourceFromAbstract,
        ListableAPIResource as ListableAPIResourceFromAbstract,
        SearchableAPIResource as SearchableAPIResourceFromAbstract,
        VerifyMixin as VerifyMixinFromAbstract,
        custom_method as custom_methodFromAbstract,
        APIResourceTestHelpers as APIResourceTestHelpersFromAbstract,
        nested_resource_class_methods as nested_resource_class_methodsFromAbstract,
    )
    from stripe.stripe_object import (
        StripeObject,
    )

    assert (
        APIResourceFromAbstract[StripeObject]
        == stripe.abstract.APIResource[StripeObject]
    )
    assert (
        stripe.api_resources.abstract.SingletonAPIResource
        == SingletonAPIResourceFromAbstract
    )
    assert (
        stripe.api_resources.abstract.CreateableAPIResource
        == CreateableAPIResourceFromAbstract
    )
    assert (
        stripe.api_resources.abstract.UpdateableAPIResource
        == UpdateableAPIResourceFromAbstract
    )
    assert (
        stripe.api_resources.abstract.DeletableAPIResource
        == DeletableAPIResourceFromAbstract
    )
    assert (
        stripe.api_resources.abstract.ListableAPIResource
        == ListableAPIResourceFromAbstract
    )
    assert (
        stripe.api_resources.abstract.SearchableAPIResource
        == SearchableAPIResourceFromAbstract
    )
    assert stripe.api_resources.abstract.VerifyMixin == VerifyMixinFromAbstract
    assert (
        stripe.api_resources.abstract.custom_method
        == custom_methodFromAbstract
    )
    assert (
        stripe.api_resources.abstract.APIResourceTestHelpers
        == APIResourceTestHelpersFromAbstract
    )
    assert (
        stripe.api_resources.abstract.nested_resource_class_methods
        == nested_resource_class_methodsFromAbstract
    )


def test_can_import_app_info() -> None:
    from stripe.app_info import AppInfo as AppInfoFromStripeAppInfo
    from stripe import AppInfo as AppInfoFromStripe

    assert AppInfoFromStripeAppInfo is AppInfoFromStripe
    assert AppInfoFromStripeAppInfo is stripe.AppInfo


def test_can_import_stripe_response() -> None:
    from stripe.stripe_response import (
        StripeResponse as StripeResponseFromStripeResponse,
    )

    assert (
        StripeResponseFromStripeResponse
        is stripe.stripe_response.StripeResponse
    )


def test_can_import_oauth_members() -> None:
    from stripe import (
        OAuth,
    )

    assert OAuth is not None


def test_can_import_errors() -> None:
    from stripe.error import (
        StripeError as StripeErrorFromStripeError,
    )

    assert StripeErrorFromStripeError is not None


def test_can_import_top_level_resource() -> None:
    from stripe import Account as AccountFromStripe
    from stripe.api_resources import Account as AccountFromStripeResources
    from stripe.api_resources.account import (
        Account as AccountFromStripeResourcesAccount,
    )

    assert stripe.Account == AccountFromStripe
    assert AccountFromStripe == AccountFromStripeResources
    assert AccountFromStripeResourcesAccount == AccountFromStripeResources


def test_can_import_namespaced_resource() -> None:
    from stripe import tax as TaxPackage
    from stripe.api_resources.tax import (
        Calculation as CalculationFromResources,
    )
    from stripe.api_resources.tax.calculation import (
        Calculation as CalculationFromResourcesCalculation,
    )

    assert stripe.tax is TaxPackage
    assert stripe.tax.Calculation is TaxPackage.Calculation
    assert stripe.tax.Calculation is CalculationFromResources
    assert CalculationFromResources is CalculationFromResourcesCalculation
