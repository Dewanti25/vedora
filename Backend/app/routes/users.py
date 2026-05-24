from fastapi import APIRouter, Depends
from ..schemas.user import UserOut
from ..deps import get_current_user, admin_required, student_required, teacher_required

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserOut)
async def me(user=Depends(get_current_user)):
    # user is a dict from DB; map keys to UserOut
    return {
        "id": user.get("id") or str(user.get("_id")),
        "name": user.get("name"),
        "email": user.get("email"),
        "role": user.get("role"),
        "profileImage": user.get("profileImage"),
        "createdAt": user.get("createdAt"),
    }


@router.get("/admin-check")
async def admin_check(user=Depends(admin_required)):
    return {"ok": True, "role": user.get("role")}


@router.get("/student-check")
async def student_check(user=Depends(student_required)):
    return {"ok": True, "role": user.get("role")}


@router.get("/teacher-check")
async def teacher_check(user=Depends(teacher_required)):
    return {"ok": True, "role": user.get("role")}
