from typing import Generic, TypeVar

InputDTO = TypeVar("InputDTO")
OutputDTO = TypeVar("OutputDTO")

class Interactor(Generic[InputDTO, OutputDTO]):
    def __call__(selfm, input_dto: InputDTO) -> OutputDTO:
        raise NotImplementedError