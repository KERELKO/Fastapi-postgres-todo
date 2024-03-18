from fastapi import FastAPI


def create_app():
    return FastAPI(
        title='FastAPI todo app',
        docs_url='/api/docs',
        description='Simple todo app on FastAPI',
        debug=True,
    )
