"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc

from .fuota_pb2 import *
# FUOTAServerService provides the fuota-server API methods.
# Note: this API considered experimental.
class FUOTAServerServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    # CreateDeployment creates the given FUOTA deployment.
    CreateDeployment:grpc.UnaryUnaryMultiCallable[
        global___CreateDeploymentRequest,
        global___CreateDeploymentResponse] = ...

    # GetDeploymentStatus returns the FUOTA deployment status given an ID.
    GetDeploymentStatus:grpc.UnaryUnaryMultiCallable[
        global___GetDeploymentStatusRequest,
        global___GetDeploymentStatusResponse] = ...

    # GetDeploymentDeviceLogs returns the FUOTA logs given a deployment ID and DevEUI.
    GetDeploymentDeviceLogs:grpc.UnaryUnaryMultiCallable[
        global___GetDeploymentDeviceLogsRequest,
        global___GetDeploymentDeviceLogsResponse] = ...


# FUOTAServerService provides the fuota-server API methods.
# Note: this API considered experimental.
class FUOTAServerServiceServicer(metaclass=abc.ABCMeta):
    # CreateDeployment creates the given FUOTA deployment.
    @abc.abstractmethod
    def CreateDeployment(self,
        request: global___CreateDeploymentRequest,
        context: grpc.ServicerContext,
    ) -> global___CreateDeploymentResponse: ...

    # GetDeploymentStatus returns the FUOTA deployment status given an ID.
    @abc.abstractmethod
    def GetDeploymentStatus(self,
        request: global___GetDeploymentStatusRequest,
        context: grpc.ServicerContext,
    ) -> global___GetDeploymentStatusResponse: ...

    # GetDeploymentDeviceLogs returns the FUOTA logs given a deployment ID and DevEUI.
    @abc.abstractmethod
    def GetDeploymentDeviceLogs(self,
        request: global___GetDeploymentDeviceLogsRequest,
        context: grpc.ServicerContext,
    ) -> global___GetDeploymentDeviceLogsResponse: ...


def add_FUOTAServerServiceServicer_to_server(servicer: FUOTAServerServiceServicer, server: grpc.Server) -> None: ...
