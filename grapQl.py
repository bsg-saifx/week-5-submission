import typing
import strawberry
from fastapi import FastAPI

from strawberry.fastapi import GraphQLRouter

@strawberry.type
class Book:
    title: str
    author: str


def get_books()-> typing.List[Book]:
    return [
            Book(
                title="The Da Vinci Code",
                author="Dan Brown"
                ),
            Book(
                title="Himur Hate 5 ti nil podmo",
                author="Humayan Ahmed"
                ),
            ]


@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)


schema = strawberry.Schema(query=Query)

app = FastAPI()

graphQlapp = GraphQLRouter(schema)
app.include_router(graphQlapp,prefix="/simpleObject")

