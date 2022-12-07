"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.protobuf.empty_pb2
import grpc

from .internal_pb2 import *
# InternalService is the service providing API endpoints for internal usage.
class InternalServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    # Log in a user
    Login:grpc.UnaryUnaryMultiCallable[
        global___LoginRequest,
        global___LoginResponse] = ...

    # Get the current user's profile
    Profile:grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        global___ProfileResponse] = ...

    # Perform a global search.
    GlobalSearch:grpc.UnaryUnaryMultiCallable[
        global___GlobalSearchRequest,
        global___GlobalSearchResponse] = ...

    # CreateAPIKey creates the given API key.
    CreateAPIKey:grpc.UnaryUnaryMultiCallable[
        global___CreateAPIKeyRequest,
        global___CreateAPIKeyResponse] = ...

    # DeleteAPIKey deletes the API key.
    DeleteAPIKey:grpc.UnaryUnaryMultiCallable[
        global___DeleteAPIKeyRequest,
        google.protobuf.empty_pb2.Empty] = ...

    # ListAPIKeys lists the available API keys.
    ListAPIKeys:grpc.UnaryUnaryMultiCallable[
        global___ListAPIKeysRequest,
        global___ListAPIKeysResponse] = ...

    # Get the global settings.
    Settings:grpc.UnaryUnaryMultiCallable[
        google.protobuf.empty_pb2.Empty,
        global___SettingsResponse] = ...

    # OpenID Connect login.
    OpenIDConnectLogin:grpc.UnaryUnaryMultiCallable[
        global___OpenIDConnectLoginRequest,
        global___OpenIDConnectLoginResponse] = ...

    # GetDevicesSummary returns an aggregated summary of the devices.
    GetDevicesSummary:grpc.UnaryUnaryMultiCallable[
        global___GetDevicesSummaryRequest,
        global___GetDevicesSummaryResponse] = ...

    # GetGatewaysSummary returns an aggregated summary of the gateways.
    GetGatewaysSummary:grpc.UnaryUnaryMultiCallable[
        global___GetGatewaysSummaryRequest,
        global___GetGatewaysSummaryResponse] = ...


# InternalService is the service providing API endpoints for internal usage.
class InternalServiceServicer(metaclass=abc.ABCMeta):
    # Log in a user
    @abc.abstractmethod
    def Login(self,
        request: global___LoginRequest,
        context: grpc.ServicerContext,
    ) -> global___LoginResponse: ...

    # Get the current user's profile
    @abc.abstractmethod
    def Profile(self,
        request: google.protobuf.empty_pb2.Empty,
        context: grpc.ServicerContext,
    ) -> global___ProfileResponse: ...

    # Perform a global search.
    @abc.abstractmethod
    def GlobalSearch(self,
        request: global___GlobalSearchRequest,
        context: grpc.ServicerContext,
    ) -> global___GlobalSearchResponse: ...

    # CreateAPIKey creates the given API key.
    @abc.abstractmethod
    def CreateAPIKey(self,
        request: global___CreateAPIKeyRequest,
        context: grpc.ServicerContext,
    ) -> global___CreateAPIKeyResponse: ...

    # DeleteAPIKey deletes the API key.
    @abc.abstractmethod
    def DeleteAPIKey(self,
        request: global___DeleteAPIKeyRequest,
        context: grpc.ServicerContext,
    ) -> google.protobuf.empty_pb2.Empty: ...

    # ListAPIKeys lists the available API keys.
    @abc.abstractmethod
    def ListAPIKeys(self,
        request: global___ListAPIKeysRequest,
        context: grpc.ServicerContext,
    ) -> global___ListAPIKeysResponse: ...

    # Get the global settings.
    @abc.abstractmethod
    def Settings(self,
        request: google.protobuf.empty_pb2.Empty,
        context: grpc.ServicerContext,
    ) -> global___SettingsResponse: ...

    # OpenID Connect login.
    @abc.abstractmethod
    def OpenIDConnectLogin(self,
        request: global___OpenIDConnectLoginRequest,
        context: grpc.ServicerContext,
    ) -> global___OpenIDConnectLoginResponse: ...

    # GetDevicesSummary returns an aggregated summary of the devices.
    @abc.abstractmethod
    def GetDevicesSummary(self,
        request: global___GetDevicesSummaryRequest,
        context: grpc.ServicerContext,
    ) -> global___GetDevicesSummaryResponse: ...

    # GetGatewaysSummary returns an aggregated summary of the gateways.
    @abc.abstractmethod
    def GetGatewaysSummary(self,
        request: global___GetGatewaysSummaryRequest,
        context: grpc.ServicerContext,
    ) -> global___GetGatewaysSummaryResponse: ...


def add_InternalServiceServicer_to_server(servicer: InternalServiceServicer, server: grpc.Server) -> None: ...