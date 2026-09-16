# State Machines

## Task

Allowed states: `open`, `active`, `blocked`, `done`, `cancelled`.

Recommended transitions:

- `open → active`
- `active ↔ blocked`
- `open|active|blocked → done`
- `open|active|blocked → cancelled`

## Run

Allowed states: `running`, `succeeded`, `failed`, `interrupted`, `superseded`.

Only `running` is non-terminal. A merged running record may be terminalized once. Terminal records are immutable.

## Claim revision

Stored status describes the epistemic status **of that historical revision**: `proposed`, `supported`, `disputed`, or `retired`.

Supersession is represented by the next revision's `supersedes` pointer. This avoids mutating old claim files.
