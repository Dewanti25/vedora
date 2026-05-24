from fastapi import JSONResponse

def ok(data=None):
    return JSONResponse({'ok': True, 'data': data})
