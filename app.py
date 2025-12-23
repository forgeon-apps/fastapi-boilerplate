from datetime import datetime

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(
    title="Forgeon + FastAPI",
    description="FastAPI playground wired for Forgeon",
    version="1.0.0",
)

# ───────────────── SHELL ─────────────────

HTML_SHELL = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>{title}</title>
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <style>
      :root {{
        color-scheme: dark;
        --bg: #050505;
        --card: #0f0f10;
        --border: #222;
        --text: #f5f5f5;
        --muted: #9ca3af;
        --accent: #e5e5e5;
      }}
      * {{ box-sizing: border-box; margin: 0; padding: 0; }}
      body {{
        min-height: 100vh;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif;
        background: radial-gradient(circle at top, #111 0, #050505 55%);
        color: var(--text);
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 2rem 1.5rem;
      }}
      .card {{
        width: 100%;
        max-width: 720px;
        border-radius: 1.25rem;
        border: 1px solid var(--border);
        background: radial-gradient(circle at top left, #151515 0, var(--card) 50%, #050505 100%);
        padding: 1.75rem 1.75rem 1.5rem;
      }}
      .eyebrow {{
        font-size: 0.7rem;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        color: var(--muted);
        margin-bottom: 0.75rem;
      }}
      h1 {{
        font-size: 1.6rem;
        line-height: 1.2;
        margin-bottom: 0.75rem;
      }}
      p {{
        font-size: 0.9rem;
        line-height: 1.6;
        color: var(--muted);
      }}
      .grid {{
        display: grid;
        grid-template-columns: 1.1fr 1fr;
        gap: 1.5rem;
      }}
      @media (max-width: 640px) {{
        .grid {{ grid-template-columns: 1fr; }}
      }}
      .pill-row {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.4rem;
        margin: 1.25rem 0 0.75rem;
      }}
      .pill {{
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.16em;
        padding: 0.25rem 0.6rem;
        border-radius: 999px;
        border: 1px solid var(--border);
        color: var(--muted);
      }}
      .pill strong {{
        color: var(--accent);
        font-weight: 600;
      }}
      .links {{
        display: flex;
        flex-direction: column;
        gap: 0.35rem;
        margin-top: 0.5rem;
        font-size: 0.8rem;
      }}
      .links a {{
        color: var(--accent);
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 0.3rem;
      }}
      .links a span {{
        font-size: 0.75rem;
        color: var(--muted);
      }}
      .links a:hover {{
        text-decoration: underline;
      }}
      .meta {{
        margin-top: 1.5rem;
        padding-top: 0.75rem;
        border-top: 1px solid var(--border);
        display: flex;
        justify-content: space-between;
        gap: 0.75rem;
        font-size: 0.75rem;
        color: var(--muted);
      }}
      .badge {{
        padding: 0.1rem 0.55rem;
        border-radius: 999px;
        border: 1px solid var(--border);
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 0.14em;
      }}
      .back {{
        font-size: 0.8rem;
        margin-bottom: 1rem;
      }}
      .back a {{
        color: var(--muted);
        text-decoration: none;
      }}
      .back a:hover {{
        color: var(--accent);
        text-decoration: underline;
      }}
      ul {{
        padding-left: 1rem;
        margin-top: 0.6rem;
        font-size: 0.85rem;
        color: var(--muted);
      }}
    </style>
  </head>
  <body>
    <div class="card">
      {body}
    </div>
  </body>
</html>"""

def html_shell(title: str, body: str) -> str:
    return HTML_SHELL.format(title=title, body=body)

# ───────────────── HTML PAGES ─────────────────

@app.get("/", response_class=HTMLResponse)
async def home_page():
    body = """
        <div class="grid">
          <div>
            <div class="eyebrow">Forgeon · FastAPI playground</div>
            <h1>FastAPI boilerplate, ready for deploy tests.</h1>
            <p>
              This service is a small FastAPI app you can use to test routing,
              health checks, JSON APIs, and HTML responses inside Forgeon or on your
              local machine.
            </p>

            <div class="pill-row">
              <div class="pill"><strong>GET</strong> /</div>
              <div class="pill">FastAPI · Uvicorn</div>
              <div class="pill">Playground mode (no DB required)</div>
            </div>
          </div>

          <div>
            <div class="links">
              <a href="/info">
                /info
                <span>– service overview & Forgeon context</span>
              </a>
              <a href="/about">
                /about
                <span>– what this boilerplate is for</span>
              </a>
              <a href="/framework">
                /framework
                <span>– stack: FastAPI, Python, etc.</span>
              </a>
              <a href="/status">
                /status
                <span>– JSON health endpoint</span>
              </a>
              <a href="/v1">
                /v1
                <span>– JSON API index</span>
              </a>
              <a href="/docs">
                /docs
                <span>– interactive Swagger UI</span>
              </a>
            </div>
          </div>
        </div>

        <div class="meta">
          <span>Try deploying this to Forgeon as a simple FastAPI playground.</span>
          <span class="badge">127.0.0.1:8000</span>
        </div>
    """
    return HTMLResponse(html_shell("Forgeon FastAPI playground", body))


@app.get("/info", response_class=HTMLResponse)
async def info_page():
    body = """
        <div class="back">
          <a href="/">← Back to home</a>
        </div>

        <div class="grid">
          <div>
            <div class="eyebrow">Service info</div>
            <h1>fastapi-playground · Forgeon-ready microservice</h1>
            <p>
              This instance exposes a couple of HTML & JSON endpoints so you can
              quickly verify that traffic is reaching the container correctly.
            </p>

            <ul>
              <li>Check that the container boots and responds.</li>
              <li>Wire health checks to <code>/status</code>.</li>
              <li>Inspect logs and latency from Forgeon.</li>
            </ul>
          </div>

          <div>
            <div class="links">
              <a href="/">
                / <span>– landing page</span>
              </a>
              <a href="/v1">
                /v1 <span>– JSON index for API v1</span>
              </a>
              <a href="https://forgeon.io" target="_blank" rel="noreferrer">
                forgeon.io <span>– learn more about the platform</span>
              </a>
            </div>
          </div>
        </div>
    """
    return HTMLResponse(html_shell("Forgeon · FastAPI Playground · Info", body))


@app.get("/about", response_class=HTMLResponse)
async def about_page():
    body = """
        <div class="back">
          <a href="/">← Back to home</a>
        </div>

        <div>
          <div class="eyebrow">About this playground</div>
          <h1>FastAPI app wired for Forgeon.</h1>
          <p>
            This tiny service is a <strong>FastAPI</strong> playground used to test how
            Forgeon talks to containers: health checks, routes, timeouts, and log streaming.
          </p>
          <p>
            It&apos;s not a production API – just a safe sandbox you can deploy, poke, and
            then replace with your real service once everything feels right.
          </p>

          <ul>
            <li>Boots fast with no database configured.</li>
            <li>Has HTML endpoints for visual checks.</li>
            <li>Has JSON endpoints for programmatic checks.</li>
          </ul>
        </div>
    """
    return HTMLResponse(html_shell("Forgeon · About this FastAPI demo", body))


@app.get("/framework", response_class=HTMLResponse)
async def framework_page():
    body = """
        <div class="back">
          <a href="/">← Back to home</a>
        </div>

        <div class="grid">
          <div>
            <div class="eyebrow">Stack</div>
            <h1>Built with FastAPI & Python.</h1>
            <p>
              The service uses <strong>FastAPI</strong> for routing and OpenAPI docs,
              typically served by <strong>Uvicorn</strong> behind Forgeon. In playground mode
              it runs without any database.
            </p>
          </div>

          <div>
            <div class="links">
              <a href="/status">
                /status <span>– health JSON</span>
              </a>
              <a href="/info">
                /info <span>– service overview</span>
              </a>
              <a href="/v1">
                /v1 <span>– API index</span>
              </a>
              <a href="/docs">
                /docs <span>– interactive API docs</span>
              </a>
            </div>
          </div>
        </div>
    """
    return HTMLResponse(html_shell("Forgeon · FastAPI Framework stack", body))


# ───────────────── JSON HEALTH & INDEX ─────────────────

@app.get("/status")
async def status_view():
    now = datetime.utcnow().isoformat() + "Z"
    return {
        "status": "ok",
        "service": "fastapi-playground",
        "timestamp": now,
    }


@app.get("/v1")
async def v1_index():
    return {
        "message": "FastAPI API v1 index",
        "service": "fastapi-playground",
        "routes": {
            "html": ["/", "/info", "/about", "/framework"],
            "health": ["/status"],
            "api": ["/v1", "/api/data", "/api/items/{item_id}"],
            "docs": ["/docs", "/redoc"],
        },
    }

# ───────────────── SAMPLE API ROUTES ─────────────────

@app.get("/api/data")
async def get_sample_data():
    return {
        "data": [
            {"id": 1, "name": "Sample Item 1", "value": 100},
            {"id": 2, "name": "Sample Item 2", "value": 200},
            {"id": 3, "name": "Sample Item 3", "value": 300},
        ],
        "total": 3,
        "timestamp": "2024-01-01T00:00:00Z",
    }


@app.get("/api/items/{item_id}")
async def get_item(item_id: int):
    return {
        "item": {
            "id": item_id,
            "name": f"Sample Item {item_id}",
            "value": item_id * 100,
        },
        "timestamp": "2024-01-01T00:00:00Z",
    }
