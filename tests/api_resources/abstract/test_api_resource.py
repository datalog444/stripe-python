import pytest

import stripe


class TestAPIResource(object):
    class MyResource(stripe.APIResource):
        OBJECT_NAME = "myresource"

    def test_retrieve_and_refresh(self, http_client_mock):
        path = "/v1/myresources/foo%2A"
        query_string = "myparam=5"
        http_client_mock.stub_request(
            "get",
            path,
            query_string,
            '{"id": "foo2", "bobble": "scrobble"}',
            rheaders={"request-id": "req_id"},
        )

        res = self.MyResource.retrieve(
            "foo*",
            myparam=5,
            stripe_version="2018-02-28",
            stripe_account="acct_foo",
        )

        http_client_mock.assert_requested(
            "get",
            path=path,
            query_string=query_string,
            api_key="sk_test_123",
            stripe_version="2018-02-28",
            stripe_account="acct_foo",
        )
        assert res.bobble == "scrobble"
        assert res.id == "foo2"
        assert res.api_key == "sk_test_123"
        assert res.stripe_version == "2018-02-28"
        assert res.stripe_account == "acct_foo"

        assert res.last_response is not None
        assert res.last_response.request_id == "req_id"

        path = "/v1/myresources/foo2"
        query_string = "myparam=5"
        http_client_mock.stub_request(
            "get", path, query_string, '{"frobble": 5}'
        )

        res = res.refresh()

        http_client_mock.assert_requested(
            "get", path=path, query_string=query_string
        )
        assert res.frobble == 5
        with pytest.raises(KeyError):
            res["bobble"]

    def test_request_with_special_fields_prefers_explicit(
        self, http_client_mock
    ):
        path = "/v1/myresources/foo"
        query_string = "bobble=scrobble"
        http_client_mock.stub_request(
            "get",
            path,
            query_string,
            '{"id": "foo2", "bobble": "scrobble"}',
        )

        self.MyResource._static_request(
            "get",
            path,
            idempotency_key="explicit",
            params={"idempotency_key": "params", "bobble": "scrobble"},
        )

        http_client_mock.assert_requested(
            "get",
            path=path,
            query_string=query_string,
            idempotency_key="explicit",
        )

    def test_convert_to_stripe_object(self):
        sample = {
            "foo": "bar",
            "adict": {"object": "charge", "id": 42, "amount": 7},
            "alist": [{"object": "customer", "name": "chilango"}],
        }

        converted = stripe.util.convert_to_stripe_object(
            sample, "akey", None, None
        )

        # Types
        assert isinstance(converted, stripe.stripe_object.StripeObject)
        assert isinstance(converted.adict, stripe.Charge)
        assert len(converted.alist) == 1
        assert isinstance(converted.alist[0], stripe.Customer)

        # Values
        assert converted.foo == "bar"
        assert converted.adict.id == 42
        assert converted.alist[0].name == "chilango"

        # Stripping
        # TODO: We should probably be stripping out this property
        # self.assertRaises(AttributeError, getattr, converted.adict, 'object')

    def test_raise_on_incorrect_id_type(self):
        for obj in [None, 1, 3.14, dict(), list(), set(), tuple(), object()]:
            with pytest.raises(stripe.error.InvalidRequestError):
                self.MyResource.retrieve(obj)

    @pytest.fixture
    def resource(self):
        return self.MyResource.construct_from(
            {"id": "foo"},
            key="newkey",
            stripe_version="2023-01-01",
            stripe_account="acct_foo",
        )

    @pytest.fixture
    def check_request_options(self, http_client_mock):
        def check_request_options(
            *, api_key=None, stripe_version=None, stripe_account=None
        ):
            extra_headers = {}
            if stripe_account is None:
                extra_headers = {"Stripe-Account": None}
            if api_key is None:
                api_key = stripe.api_key
            if stripe_version is None:
                stripe_version = stripe.api_version

            http_client_mock.assert_requested(
                "get",
                path="/v1/myresources/foo",
                api_key=api_key,
                stripe_version=stripe_version,
                extra_headers=extra_headers,
            )

        return check_request_options

    def test_class_method_does_not_forward_options(
        self, resource, http_client_mock, check_request_options
    ):
        http_client_mock.stub_request(
            "get",
            "/v1/myresources/foo",
            rbody='{"id": "foo"}',
        )

        resource.retrieve("foo")

        check_request_options()

    def test_instance_method_forwards_options(
        self, resource, http_client_mock, check_request_options
    ):
        http_client_mock.stub_request(
            "get",
            "/v1/myresources/foo",
            rbody='{"id": "foo"}',
        )

        resource.refresh()

        check_request_options(
            api_key="newkey",
            stripe_version="2023-01-01",
            stripe_account="acct_foo",
        )
