import typing
from collections.abc import Callable

__all__ = [
	"LexType",
	"ErrorType",
	"TitleLexType",
	"TransformerType",
	"TitleTransformerType",
]


class TransformerType(typing.Protocol):
	start: int
	pos: int
	input: str
	output: str
	currentKey: str
	attrs: "dict[str, str | None]"
	attrName: str
	audio: bool
	resFileSet: "set[str]"
	exampleColor: str

	def __init__(self) -> None:
		pass

	def end(self) -> bool:
		pass

	def move(self, chars: int) -> None:
		pass

	def next(self) -> str:
		pass

	def follows(self, st: str) -> bool:
		pass

	def skipAny(self, chars: str):
		pass

	def addText(self, st: str) -> None:
		pass

	def resetBuf(self) -> str:
		pass


class TitleTransformerType(TransformerType, typing.Protocol):
	title: str
	outputAlt: str

	def addText2(self, st: str) -> None:
		pass


ErrorType = str | None

# it is an State Function (state as in state machine)
LexType = Callable[[TransformerType], tuple["LexType", ErrorType]] | None

TitleLexType = Callable[[TitleTransformerType], tuple["TitleLexType", ErrorType]] | None
