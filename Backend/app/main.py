from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from .config import FRONTEND_URL
from .database import connect_to_mongo, close_mongo_connection
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("vedora")

from .routes import health

def create_app() -> FastAPI:
    app = FastAPI(title="Vedora AI - Backend (new app)")

    # CORS - allow frontend
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[FRONTEND_URL, "http://127.0.0.1:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health.router)
    # user routes
    from .routes import users
    app.include_router(users.router)
    # api routes
    from .routes import api
    app.include_router(api.router)
    # auth
    from .routes import auth_routes
    app.include_router(auth_routes.router)
    # batches
    from .routes import batch_routes
    app.include_router(batch_routes.router)
    # textbooks
    from .routes import textbook_routes
    app.include_router(textbook_routes.router)
    # sessions
    from .routes import session_routes
    app.include_router(session_routes.router)
    # ai
    from .routes import ai_routes
    app.include_router(ai_routes.router)
    # resources listing
    from .routes import resources_routes
    app.include_router(resources_routes.router)
    # schools
    from .routes import school_routes
    app.include_router(school_routes.router)
    # catalog (boards, grades, subjects, courses, chapters)
    from .routes import catalog_routes
    app.include_router(catalog_routes.router)
    # schedules
    from .routes import schedule_routes
    app.include_router(schedule_routes.router)
    # syllabus planner
    from .routes import syllabus_routes
    app.include_router(syllabus_routes.router)
    # register alternate routes (root-level batch syllabus path)
    try:
        app.include_router(syllabus_routes.router_alt)
    except Exception:
        pass
    # homework
    from .routes import homework_routes
    app.include_router(homework_routes.router)
    # notes
    from .routes import notes_routes
    app.include_router(notes_routes.router)
    # quizzes
    from .routes import quiz_routes
    app.include_router(quiz_routes.router)
    # ai service endpoints
    from .routes import ai_routes
    app.include_router(ai_routes.router)

    @app.on_event("startup")
    async def startup_event():
        # connect to mongodb
        connect_to_mongo()
        logger.info("Connected to MongoDB")
        # ensure important indexes
        try:
            from .database import db
            # unique enrollment per user+batch
            await db.enrollments.create_index([('user_id', 1), ('batch_id', 1)], unique=True)
            # unique email for users
            await db.users.create_index([('email', 1)], unique=True)
            logger.info("Ensured enrollment unique index")
        except Exception:
            logger.exception("Failed to ensure indexes")

    @app.on_event("shutdown")
    async def shutdown_event():
        close_mongo_connection()

    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
