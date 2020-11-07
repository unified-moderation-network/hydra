### Common

All payloads are msgpack encoded 2-tuples with the first item being a topic.
Between the fixed size of the outer container and fixed topic names, we have predictable prefixes allowing zmq to work optimally for pub/sub

Many of the topic names are just having fun with the component names,
if this is problematic for anyone, just use a constant with a less fun name assigned to this

## Payloads

### Filter request

Msgpack encoded 2-tuple of (Topic, Payload)

- Topic: "basilisk.offer"
- Payload: 2-tuple of (If Match, To Check)

  - If Match: a payload to be broadcast on a filter match (See next payload for details)
    
  - To Check: a string to check against the filter


### Filter match broadcast

Msgpack encoded 2-tuple of (Topic, Payload)

- Topic: "basilisk.gaze"
- Payload: 2-tuple of (uuid4, Any)

  - uuid4: a uuid4 for matching exact event
    
  - Any: Any messagepack serializable data which is useful to the asker to have included in the response, can be Null


### Modify Filter

Msgpack encoded 2-tuple of (Topic, Payload)

- Topic: "basilisk.refocus"
- Payload: 2-tuple of (Add, Remove)
    
  - Add: Tuple of filters to add (0-N)
    
  - Remove Tuple of filters to remove (0-N)


### Cache invalidation

Msgpack encoded 2-tuple of (Topic, Payload)

- Topic: "cache.invalidate"
- Payload: Cache Name
    
  - Cache Name: Currently, this may only be "basilisk", other caches will be added later.


### Status Check

Msgpack encoded 2-tuple of (Topic, Payload)

- Topic: "status.check"
- Payload: uuid4 (Sent for use in response)


### Status response

Note: The payload of this one is partially subject to change, specifically with the status portion of the payload.

Msgpack encoded 2-tuple of (Topic, Payload)

- Topic: "status.response"
- Payload: 4-tuple of (uuid4, component name, uptime, status)
    
  - uuid4: used for matching with a status request (see above)
    
  - component name: the component which is responding (most should)
    
  - uptime: the unix timestamp the component has been alive since
    
  - status: a map containing details about the current health of the component (differs by component, to be documented more)

    - Basilisk: "patterns" => sequence of patterns being filtered


### Schedule message

Msgpack encoded 2-tuple of (Topic, Payload)

- Topic: "serpent.start"
- Payload: 4-Tuple of (uuid4, schedule, timezone_info, scheduled_message)

  - uuid: used to unschedule
   
  - schedule: 2-tuple of (schedule type, parseable schedule)
    
    - The type can currently only be "CRON" with a matching parseable entry
  
  - scheduled_message: binary representation of the scheduled message


### Unschedule message

Msgpack encoded 2-tuple of (Topic, Payload)

- Topic: "serpent.stop"
- Payload: 2-tuple of (schedule type, uuid4)
  - see above scheduling for these
