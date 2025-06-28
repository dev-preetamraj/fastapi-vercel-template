from fastapi import APIRouter

router = APIRouter(tags=["App"])


@router.get("/log-entry")
async def get_log_entries():
    file = open("log.txt", "r")
    content = file.read().strip().split("\n")[-2:]
    file.close()
    return {"data": content}
