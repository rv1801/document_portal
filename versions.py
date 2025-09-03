import importlib.metadata
packages = [
    "langchain",
    "python-dotenv",
    "langchain_groq",
    "ipykernel",
    "langchain_google_genai",
    "pypdf",
    "faiss-cpu",
    "langchain-community",
    "chromadb",
    "langchain_core",
    "structlog",
    "PyMuPDF",
    "pylint",
    "pandas",
    "streamlit",
    "pytest",
    "langchain_core[tracing]",
    "fastapi",
    "uvicorn",
    "python-multipart",
    "docx2txt"
]
for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")

# # serve static & templates
# app.mount("/static", StaticFiles(directory="../static"), name="static")
# templates = Jinja2Templates(directory="../templates")