# ADR-0002: Evidence and knowledge history are append-only

**Status:** Accepted  
**Date:** 2026-09-16

## Decision

Merged source, evidence, and claim records are immutable. Corrections are additive. Claim changes use explicit revision chains.

## Why

Silent edits destroy auditability and make it impossible to tell what a prior conclusion was based on.
