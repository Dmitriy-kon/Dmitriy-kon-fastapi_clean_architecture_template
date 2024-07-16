from typing import Protocol, TypeVar

InputDTO_contra = TypeVar("InputDTO_contra", contravariant=True)
OutputDTO_co = TypeVar("OutputDTO_co", covariant=True)


class Interactor(Protocol[InputDTO_contra, OutputDTO_co]):
    async def __call__(self, input_dto: InputDTO_contra) -> OutputDTO_co:
        raise NotImplementedError
