# Proposed shared API

The same versioned contract is intended for official hosting and independently operated servers. All operations require a scoped bearer token. Private hosted implementation details are not part of this repository. Every path in openapi.json is proposed, with implementation status pending.

Persist exact request bytes and consent before a job POST. Bind operation ID, kind, endpoint, server/account/profile identity, source revision/hash and approved payload digest. An ambiguous reply is recovered only with GET /v1/runs/{id}; never automatically send a second POST or switch backend. Cancellation invalidates presentation while retaining recovery evidence. Self-hosted model/provider costs are operator-managed; credits are null rather than fabricated hosted balances. Capability negotiation states model/feature differences. Sync writes use expected revision and digest; conflicts preserve both versions and never overwrite learner work silently.

Sandbox execution remains disabled until unprivileged worker isolation, no secrets/host access, default network denial, bounded CPU/memory/process/time/disk/output and tenant separation are proven. Container packaging alone is not proof. Open defaults remain usable without the private Plus repo when runtime implementation lands.
