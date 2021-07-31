from typing import Optional


async def common_parameters(
            q: Optional[str] = None,
            skip: int = 1,
            limit: int = 100
        ):
    return {"q": q, "skip": skip, "limit": limit}

async def paginate_parameters(
            page: int = 1,
            order: str = 'asc',
            sort: str = 'id',
        ):
    return {"page": page, "order": order, "sort": sort}

async def filter_parameters(
            filter_field: str = None,
            filter_value: str = None
        ):
    return {"filter_field": filter_field, "filter_value": filter_value}
