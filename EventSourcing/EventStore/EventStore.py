import abc
import uuid
import typing
class EventStore(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def load_stream(self, aggregate_uuid:uuid.UUID) -> EventStream:
        pass

    @abc.abstractmethod
    def append_to_stream(self,
                         aggregate_uuid:uuid.UUID,
                         expected_version:int,
                         events:typing.List[Event]
    ) -> None :
        pass











