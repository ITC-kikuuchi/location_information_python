from fastapi import APIRouter

router = APIRouter()

# エリア一覧取得API
@router.post("/areas")
def getAreas():
    pass

# エリア登録API
@router.post("/areas")
def createArea():
    pass

# エリア詳細取得API
@router.get("/areas/{area_id}")
def getAreaDetail():
    pass

# エリア更新API
@router.put("/areas/{area_id}")
def updateArea():
    pass

# エリア削除API
@router.delete("/areas/{area_id}")
def deleteArea():
    pass