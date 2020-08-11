# Events to track:
    1. Agent movements
    2. Agent actions other than movements
    3. Resource used.

# the histories should be recorded and managed by the game, not individual objects. Remove history from agent class.

# Event
1. type : enum
2. associatedObjectId (no reference) :
3. message
4. ownerId (who raised the event) (no object reference)
5. turn (the game turn): int
6. time : date

# History
a collection of events
configuration: record all, or record a max number of events (keep the latest max number of events). Use python deque class.