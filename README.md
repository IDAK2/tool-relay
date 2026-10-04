# Tool Relay

## Crib plate

**Account:** IDAK2  
**Network:** GenLayer StudioNet  
**Category:** Projects  
**Primary tag:** Marketplaces

## The circulation promise

A shared tool should move only when the planned job fits its capabilities, avoids every prohibited use, and arrives back with a complete inspection record. Tool Relay makes that promise executable. A librarian freezes the rules. A borrower explains the job. GenLayer validators independently judge fit before checkout and condition before recirculation.

## Fit gate

`request_checkout` compares the job plan and safety plan with the frozen capability and prohibition plates. The contract does not ask a model to manage custody. Deterministic code enforces one state, one borrower, a bounded loan window, and the exact due time.

## Custody cycle

`AVAILABLE -> CHECKED_OUT -> AVAILABLE` is the clean path. Anyone can flag a genuinely overdue loan. A failed return review moves the tool to `QUARANTINED`, where only the registered steward can record a resolution. This recovery path prevents a rejected inspection from trapping the asset forever.

## Consensus bench

The leader returns a compact structured finding. Validators independently reread the same frozen rules and evidence. User text is treated as data. Accepted output never grants money, identity, or safety certification.

## Bench setup

```text
cd frontend
npm install
npm run typecheck
npm run build
```

Contract tests run with `pytest tests -q`. The static client connects to StudioNet, reads public tool state, and sends real checkout and return transactions through the connected browser wallet.

## Deployment record

The contract address, deployment transaction, lifecycle transaction, Cloudflare URL, and GitHub repository are written to `deployment.json` after live verification.

## Inspection ledger

Tool Relay is educational coordination software. Physical tool condition and operator competence must still be checked by qualified people at the lending bench.
