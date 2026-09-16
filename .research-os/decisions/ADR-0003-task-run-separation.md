# ADR-0003: Separate persistent tasks from disposable runs

**Status:** Accepted  
**Date:** 2026-09-16

## Decision

A research question is a Task. Each execution attempt is a Run.

## Why

Chat crashes and failed searches should not fragment one research question into many pseudo-tasks or erase failed attempts.
