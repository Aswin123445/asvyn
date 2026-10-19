# Event Conflict Prevention in CivicEdge

## Project Context

**Project:** CivicEdge — Smart City Civic Engagement Platform

**Area:** Event management and volunteer participation

**Problem category:** Business-rule validation and scheduling conflicts

CivicEdge allows users to participate in community events. A user joining multiple events must not be allowed to register for events that overlap in time.

## Problem Encountered

A scheduling conflict could occur when a user attempted to join an event while already registered for another event scheduled during an overlapping time period.

Without conflict validation, the same user could register for multiple events that they could not reasonably attend.

This required the backend to validate event schedules before accepting a new registration.

## Expected Behavior

When a user attempts to join an event, the system should:

1. Identify the event the user wants to join.
2. Retrieve the user's relevant existing event registrations.
3. Check whether the requested event overlaps with any applicable existing event.
4. Reject the registration if a conflict exists.
5. Allow the registration if no conflict exists and other registration rules are satisfied.

The exact behavior should also account for event status, cancellation, and any other participation rules implemented by the application.

## Conflict Detection Logic

For two events, A and B, where each has a start and end time, their schedules overlap when:

```python
event_a.start_time < event_b.end_time and \
event_b.start_time < event_a.end_time
```

This comparison treats events that meet exactly at an endpoint as non-overlapping. If the application requires a buffer between events, that rule must be added separately.

The comparison assumes valid event intervals and consistent time-zone handling.

## Backend Validation Flow

1. Receive the request to join an event.
2. Authenticate the user and identify the requested event.
3. Validate that the event is eligible for registration.
4. Retrieve the user's applicable existing registrations.
5. Compare the requested event's time interval with existing event intervals.
6. Return a suitable validation error if a conflict is found.
7. Otherwise, proceed with registration and persist the result.

## Correctness Considerations

- **Time boundaries:** Define whether events ending at the exact start of another event count as conflicts.
- **Invalid intervals:** Ensure the event end time is later than the start time.
- **Time zones:** Compare normalized, timezone-aware timestamps where applicable.
- **Cancelled events:** Exclude registrations that should no longer block participation.
- **Concurrent requests:** Consider whether two simultaneous registration requests could both pass validation before either is saved. If necessary, use an appropriate transaction or locking strategy.
- **Error handling:** Return a clear, consistent API response when registration is rejected.

These are design considerations, not claims that every safeguard is already implemented in CivicEdge.

## Solution Implemented

The CivicEdge backend was updated to check for overlapping upcoming events that the user had already joined before allowing another registration.

**Implementation details to complete:**
- Relevant Django model and relationship:
- Registration endpoint or service:
- Exact database query:
- Validation response:
- Transaction or concurrency handling, if implemented:

## Outcome

The intended outcome is to prevent users from joining overlapping events and maintain more consistent event participation data.

Add verified evidence here, such as a test showing that an overlapping registration is rejected and a non-overlapping registration is accepted.

No performance improvement or production metric is claimed in this document.

## Lessons Learned

- Business rules should be enforced on the backend, not only in the frontend.
- Date and time comparisons require clearly defined boundary behavior.
- Validation should consider existing database records.
- Concurrent requests can introduce race conditions even when individual validation checks are correct.
- Tests should cover overlapping events, non-overlapping events, boundary times, and cancelled registrations.

## Interview Summary

**Situation:** Users could attempt to join events with overlapping schedules.

**Task:** Prevent conflicting event registrations at the backend.

**Action:** Add validation that compares a requested event with the user's existing upcoming event registrations.

**Result:** Document the verified behavior and supporting tests once confirmed.

**Learning:** Scheduling rules need explicit time-boundary semantics and reliable backend enforcement.