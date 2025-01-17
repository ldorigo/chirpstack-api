"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.protobuf.empty_pb2
import grpc

from .user_pb2 import *
# UserService is the service managing the user access.
class UserServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    # Get user list.
    List:grpc.UnaryUnaryMultiCallable[
        global___ListUserRequest,
        global___ListUserResponse] = ...

    # Get data for a particular user.
    Get:grpc.UnaryUnaryMultiCallable[
        global___GetUserRequest,
        global___GetUserResponse] = ...

    # Create a new user.
    Create:grpc.UnaryUnaryMultiCallable[
        global___CreateUserRequest,
        global___CreateUserResponse] = ...

    # Update an existing user.
    Update:grpc.UnaryUnaryMultiCallable[
        global___UpdateUserRequest,
        google.protobuf.empty_pb2.Empty] = ...

    # Delete a user.
    Delete:grpc.UnaryUnaryMultiCallable[
        global___DeleteUserRequest,
        google.protobuf.empty_pb2.Empty] = ...

    # UpdatePassword updates a password.
    UpdatePassword:grpc.UnaryUnaryMultiCallable[
        global___UpdateUserPasswordRequest,
        google.protobuf.empty_pb2.Empty] = ...


# UserService is the service managing the user access.
class UserServiceServicer(metaclass=abc.ABCMeta):
    # Get user list.
    @abc.abstractmethod
    def List(self,
        request: global___ListUserRequest,
        context: grpc.ServicerContext,
    ) -> global___ListUserResponse: ...

    # Get data for a particular user.
    @abc.abstractmethod
    def Get(self,
        request: global___GetUserRequest,
        context: grpc.ServicerContext,
    ) -> global___GetUserResponse: ...

    # Create a new user.
    @abc.abstractmethod
    def Create(self,
        request: global___CreateUserRequest,
        context: grpc.ServicerContext,
    ) -> global___CreateUserResponse: ...

    # Update an existing user.
    @abc.abstractmethod
    def Update(self,
        request: global___UpdateUserRequest,
        context: grpc.ServicerContext,
    ) -> google.protobuf.empty_pb2.Empty: ...

    # Delete a user.
    @abc.abstractmethod
    def Delete(self,
        request: global___DeleteUserRequest,
        context: grpc.ServicerContext,
    ) -> google.protobuf.empty_pb2.Empty: ...

    # UpdatePassword updates a password.
    @abc.abstractmethod
    def UpdatePassword(self,
        request: global___UpdateUserPasswordRequest,
        context: grpc.ServicerContext,
    ) -> google.protobuf.empty_pb2.Empty: ...


def add_UserServiceServicer_to_server(servicer: UserServiceServicer, server: grpc.Server) -> None: ...
