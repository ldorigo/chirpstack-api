"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import chirpstack_api.as_pb.external.api.profiles_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CreateDeviceProfileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEVICE_PROFILE_FIELD_NUMBER: builtins.int
    # Device-profile object to create.
    @property
    def device_profile(self) -> chirpstack_api.as_pb.external.api.profiles_pb2.DeviceProfile: ...
    def __init__(self,
        *,
        device_profile : typing.Optional[chirpstack_api.as_pb.external.api.profiles_pb2.DeviceProfile] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"device_profile",b"device_profile"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"device_profile",b"device_profile"]) -> None: ...
global___CreateDeviceProfileRequest = CreateDeviceProfileRequest

class CreateDeviceProfileResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    # Device-profile ID (UUID string).
    id: typing.Text = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"id",b"id"]) -> None: ...
global___CreateDeviceProfileResponse = CreateDeviceProfileResponse

class GetDeviceProfileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    # Device-profile ID (UUID string).
    id: typing.Text = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"id",b"id"]) -> None: ...
global___GetDeviceProfileRequest = GetDeviceProfileRequest

class GetDeviceProfileResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEVICE_PROFILE_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    # Device-profile object.
    @property
    def device_profile(self) -> chirpstack_api.as_pb.external.api.profiles_pb2.DeviceProfile: ...
    # Created at timestamp.
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # Last update timestamp.
    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(self,
        *,
        device_profile : typing.Optional[chirpstack_api.as_pb.external.api.profiles_pb2.DeviceProfile] = ...,
        created_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        updated_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"created_at",b"created_at",u"device_profile",b"device_profile",u"updated_at",b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"created_at",b"created_at",u"device_profile",b"device_profile",u"updated_at",b"updated_at"]) -> None: ...
global___GetDeviceProfileResponse = GetDeviceProfileResponse

class UpdateDeviceProfileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEVICE_PROFILE_FIELD_NUMBER: builtins.int
    # Device-profile object to update.
    @property
    def device_profile(self) -> chirpstack_api.as_pb.external.api.profiles_pb2.DeviceProfile: ...
    def __init__(self,
        *,
        device_profile : typing.Optional[chirpstack_api.as_pb.external.api.profiles_pb2.DeviceProfile] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"device_profile",b"device_profile"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"device_profile",b"device_profile"]) -> None: ...
global___UpdateDeviceProfileRequest = UpdateDeviceProfileRequest

class DeleteDeviceProfileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    # Device-profile ID (UUID string).
    id: typing.Text = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"id",b"id"]) -> None: ...
global___DeleteDeviceProfileRequest = DeleteDeviceProfileRequest

class DeviceProfileListItem(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    NETWORK_SERVER_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    NETWORK_SERVER_NAME_FIELD_NUMBER: builtins.int
    # Device-profile ID (UUID string).
    id: typing.Text = ...
    # Device-profile name.
    name: typing.Text = ...
    # Organization ID.
    organization_id: builtins.int = ...
    # Network-server ID.
    network_server_id: builtins.int = ...
    # Created at timestamp.
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # Last update timestamp.
    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # Network-server name.
    network_server_name: typing.Text = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        name : typing.Text = ...,
        organization_id : builtins.int = ...,
        network_server_id : builtins.int = ...,
        created_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        updated_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        network_server_name : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"created_at",b"created_at",u"updated_at",b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"created_at",b"created_at",u"id",b"id",u"name",b"name",u"network_server_id",b"network_server_id",u"network_server_name",b"network_server_name",u"organization_id",b"organization_id",u"updated_at",b"updated_at"]) -> None: ...
global___DeviceProfileListItem = DeviceProfileListItem

class ListDeviceProfileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LIMIT_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    APPLICATION_ID_FIELD_NUMBER: builtins.int
    # Max number of items to return.
    limit: builtins.int = ...
    # Offset in the result-set (for pagination).
    offset: builtins.int = ...
    # Organization id to filter on.
    organization_id: builtins.int = ...
    # Application id to filter on.
    application_id: builtins.int = ...
    def __init__(self,
        *,
        limit : builtins.int = ...,
        offset : builtins.int = ...,
        organization_id : builtins.int = ...,
        application_id : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"application_id",b"application_id",u"limit",b"limit",u"offset",b"offset",u"organization_id",b"organization_id"]) -> None: ...
global___ListDeviceProfileRequest = ListDeviceProfileRequest

class ListDeviceProfileResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TOTAL_COUNT_FIELD_NUMBER: builtins.int
    RESULT_FIELD_NUMBER: builtins.int
    # Total number of device-profiles.
    total_count: builtins.int = ...
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DeviceProfileListItem]: ...
    def __init__(self,
        *,
        total_count : builtins.int = ...,
        result : typing.Optional[typing.Iterable[global___DeviceProfileListItem]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"result",b"result",u"total_count",b"total_count"]) -> None: ...
global___ListDeviceProfileResponse = ListDeviceProfileResponse