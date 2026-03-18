# Standard Procedure: Kinco VFD Check

> **When to use:** Main motor no signal, motor not starting, VFD error codes  
> **Created from case:** 1957026832

## Quick Diagnosis

1. Open electrical cabinet
2. Check VFD display:
   - **If VFD is on:** Read error code, photograph it, send to technologist
   - **If VFD is off:** Check motor circuit breaker
3. Check wire integrity from breaker to VFD
4. **Isolation test:** Disconnect VFD power wires → try to start roaster
5. If roaster starts without VFD → **VFD is dead**, needs replacement

## Common VFD Error Codes

| Code | Meaning | Action |
|------|---------|--------|
| E001 | Overcurrent | Try increasing parameter A006 by +2 seconds. If persists → further diagnostics. |

## VFD Parameter Configuration

After VFD replacement, parameters must be reconfigured. Contact technologist for model-specific parameter list.

## Related

- [03 — Main Motor](../troubleshooting/03_main_motor.md)
- [06 — VFD](../troubleshooting/06_vfd.md)
