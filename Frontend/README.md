# Frontend (Vite + React)

Run:

Create an optional `.env` file in `Frontend` to set the backend API URL:

```
VITE_API_URL=http://127.0.0.1:8000
```

Then run:

```powershell
cd Frontend
npm install
npm run dev
```

The app uses `localStorage` for the JWT token and expects the backend to be running at `VITE_API_URL`.
