# Edge checklist

Pre-flight checks for running JuniorPiThon as the edge Python host.

- [ ] Services bind to `127.0.0.1` only (loopback).
- [ ] No model pulls; models are already local or not needed.
- [ ] Handshake target is `goldend-osai-omega/1`.
- [ ] FieldCore jsonl and JuniorSOL CU receipts are read, not rewritten.
- [ ] No GitHub Actions workflows exist in this repo.
- [ ] Changes are additive: no deletes, no force-push.

See also: `docs/RAILS.md`, `docs/LOCAL.md`.
