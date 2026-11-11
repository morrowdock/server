# Third-party inventory

Status: source-only scaffold, 2026-11-02. No runtime/model/container/third-party source is bundled. Contract tests require installed Python standard library (PSF); CI uses actions/checkout and actions/setup-python (both MIT), pinned by commit SHA in the workflow and fetched by CI, not vendored. No official private prompts or code have been imported. OpenAPI is a document format, not a bundled runtime dependency.

Future implementation requires version/hash/license and transitive inventory for all runtime dependencies, container base layers and model distributions. Pyodide/MPL, CheerpJ/custom and uncleared GPL/LGPL guest runtime bundles remain excluded. Embedded CPython/PSF is the proposed permissive Python path, subject to exact-artifact review. Apache licensing here does not grant redistribution of arbitrary Ollama model weights or external SDKs.
