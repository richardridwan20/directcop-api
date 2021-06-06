from typing import Optional


async def common_parameters(
            q: Optional[str] = None,
            skip: int = 0,
            limit: int = 100
        ):
    return {"q": q, "skip": skip, "limit": limit}

async def paginate_parameters(
            page: int = 1,
            order: str = 'asc',
            sort: str = 'id',
        ):
    return {"page": page, "order": order, "sort": sort}
