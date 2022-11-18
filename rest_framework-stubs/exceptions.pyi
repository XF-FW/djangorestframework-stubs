from collections.abc import Sequence
from typing import Any

from typing_extensions import TypeAlias

from django.http import HttpRequest, JsonResponse
from django.utils.functional import _StrPromise
from rest_framework.renderers import BaseRenderer
from rest_framework.request import Request

def _get_error_details(data: Any, default_code: str | None = ...) -> Any: ...
def _get_codes(detail: Any) -> Any: ...
def _get_full_details(detail: Any) -> Any: ...

class ErrorDetail(str):
    code: str | None
    def __new__(cls, string: str, code: str | None = ...): ...

_Detail: TypeAlias = str | _StrPromise | list[Any] | dict[str, Any]

class APIException(Exception):
    status_code: int
    default_detail: _Detail
    default_code: str

    detail: _Detail
    def __init__(self, detail: _Detail | None = ..., code: str | None = ...) -> None: ...
    def get_codes(self) -> Any: ...
    def get_full_details(self) -> Any: ...

class ValidationError(APIException): ...
class ParseError(APIException): ...
class AuthenticationFailed(APIException): ...
class NotAuthenticated(APIException): ...
class PermissionDenied(APIException): ...
class NotFound(APIException): ...

class MethodNotAllowed(APIException):
    def __init__(self, method: str, detail: _Detail | None = ..., code: str | None = ...) -> None: ...

class NotAcceptable(APIException):
    available_renderers: Sequence[BaseRenderer] | None
    def __init__(
        self,
        detail: _Detail | None = ...,
        code: str | None = ...,
        available_renderers: Sequence[BaseRenderer] | None = ...,
    ) -> None: ...

class UnsupportedMediaType(APIException):
    def __init__(self, media_type: str, detail: _Detail | None = ..., code: str | None = ...) -> None: ...

class Throttled(APIException):
    extra_detail_singular: str
    extra_detail_plural: str
    def __init__(self, wait: float | None = ..., detail: _Detail | None = ..., code: str | None = ...): ...

def server_error(request: HttpRequest | Request, *args: Any, **kwargs: Any) -> JsonResponse: ...
def bad_request(request: HttpRequest | Request, exception: Exception, *args: Any, **kwargs: Any) -> JsonResponse: ...
