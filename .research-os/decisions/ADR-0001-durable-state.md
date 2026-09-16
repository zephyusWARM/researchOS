# ADR-0001: Git is the durable research state layer

**Status:** Accepted  
**Date:** 2026-09-16

## Decision

Canonical research state lives in versioned Markdown and JSON inside Git.

## Why

Long AI conversations fail, expire, branch, and lose context. Git provides durable history, review, diffing, merge semantics, and offline recoverability without requiring a database service.

## Consequence

Chats are execution environments, not the source of truth.
