# Standard Procedure: Phase Sequence Check

> **When to use:** After power outage, during commissioning, when airflow is zero  
> **⚠️ CRITICAL:** After ANY power outage, always check phasing!

## Why This Matters

Incorrect phase sequence means motors run **backwards**:
- Zero airflow → coffee doesn't fly
- No roasting possible
- Potential equipment damage

## Motor Directions (Reference)

| Motor | Correct Direction |
|-------|-------------------|
| Agitator motor | Clockwise |
| Cooling table motor | Check scroll housing direction (usually counterclockwise) |
| Cooling table paddle motor | Clockwise |
| Main motor | Follow direction on motor sticker; if no marking, confirm with engineer |
| Exhaust motor | Check scroll housing direction (usually counterclockwise) |

## Steps

1. Check phase sequence on **all** motors
2. Verify each motor rotates in correct direction:
   - Run each motor separately from **service mode**
   - Observe rotation direction
   - Compare with table above
3. If any motor runs backwards → **swap two phases** at the motor connection or at the main breaker
4. Re-verify after correction

## Case Reference

Flying Pig (2.5 kg Cyclone): After power outage → incorrect phasing → airflow fix.

## Related

- [10 — Airflow](../troubleshooting/10_airflow.md)
- [Commissioning documents](../manuals/commissioning_2.5_5kg.md)
