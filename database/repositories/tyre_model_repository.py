from database.models import TyreModel
from database.repositories.base_repository import BaseRepository


class TyreModelRepository(BaseRepository[TyreModel]):

    def __init__(self, db):
        super().__init__(db, int)


