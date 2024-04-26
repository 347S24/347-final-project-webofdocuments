from ninja import NinjaAPI, Schema
# from react_wod.users.models import User
# from react_wod.matrix.models import Matrix, Document, Connection
from typing import List

api = NinjaAPI()

class UserOut(Schema):
    username: str
    email: str
    name: str = None
    # password: str


class NodeOut(Schema):
    file_name: str
    # file_contents: File
    # matrix: Matrix
    # owner: User

class MatrixOut(Schema):
    title: str
    # owner: User
    documents: List[NodeOut] = []

class ConnectionOut(Schema):
    # start_node: Document
    # end_node: Document
    # matrix: Matrix
    pass

@api.get("matricies", response=List[MatrixOut])
def get_owned_matricies(request):
    return request.user.owned_matricies.all()

@api.get("nodes", response=List[NodeOut])
def get_owned_nodes(request):
    return request.user.owned_documents.all()

