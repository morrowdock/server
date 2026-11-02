# Morrowdock Server

PRIVATE WORKING REPOSITORY. Apache-2.0 contract-and-prompts scaffold; no runnable server, Docker image, account service, provider integration or sandbox worker yet. Do not treat contract checks as runtime acceptance.

Target: a self-hosted implementation of the same public Plus API for sync, course-pack generation/grading, isolated code execution, a pinned catalog mirror and waitlist-free single-user/small-group accounts. Operators supply OpenAI, Anthropic, OpenRouter, Gemini keys or an Ollama model endpoint. No official subscription, hosted credits, premium packs or private package is required. Model/backend quality and features can differ.

`api/openapi.json` is a proposed contract, not a deployed API. `prompts/` contains newly authored open defaults, not official hosted tuning. Official Plus retains tuned prompts/routing, premium content, managed scaling and zero setup. Source extraction, persistence, authentication, deployment and worker isolation are pending. No code execution or network calls are enabled by this scaffold.

Run contract checks on Linux or macOS: `python3 -m unittest discover -s tests`. Docker packaging is a future deliverable after runtime and isolation tests. Do not run untrusted code in an API process or give a worker provider credentials, host volumes or a container-engine socket.

Public contact, Code of Conduct concerns and privacy/deletion requests: [hello@morrowdock.app](mailto:hello@morrowdock.app). Security reporting: [SECURITY.md](SECURITY.md). Org/service-account contact is admin@morrowdock.app.
