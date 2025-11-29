from ninja import Router

router = Router()


@router.get("/list")
def orders_list(request):
    return [{"id": 1, "status": "new"}, {"id": 2, "status": "paid"}]
