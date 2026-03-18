# 03 — Main Motor

> **Total cases:** 18  
> **Frequency:** ★★★★☆  
> **Affected models:** 2.5 kg Cyclone (primary), 5 kg, 20 electro, 10 electro

---

## Symptoms

### "Main Motor No Signal" Error
- Error message on display
- Motor doesn't start

### Rattling / Vibration
- Vibration during operation
- Sound worsens over time
- Pressing on motor casing eliminates the sound

### Overheating
- Motor stops during roasting
- Roaster freezes / hangs

## Diagnostic Algorithms

### No Signal
1. Check what VFD displays
2. Check wire integrity from circuit breaker to VFD
3. **Disconnect VFD power wires** → try to start roaster
4. If roaster starts without VFD → **VFD is dead** (see [Category 6](06_vfd.md))

### Rattling / Vibration
1. Check gaps — base must be pulled tight (**1.5 mm under each bolt**)
2. Remove motor, check internal bolt torque and component condition
3. Inspect impeller — scratches on scroll housing, hub condition
4. Check seal under motor

### Overheating
1. Check software version → update if needed
2. Check motor ventilation
3. Check for obstructions in discharge path

## Solved Cases — No Signal

| Client | Model | Details | Solution |
|--------|-------|---------|----------|
| Kafay Lin | 2.5 kg Cyclone | Standard error — VFD problem | VFD diagnostics/replacement |
| Plaumann Tostadurica | 5 kg | — | Diagnostics, escalate to electrician |
| RöstFlair | 2.5 kg Cyclone | — | VFD diagnostics |

## Solved Cases — Rattling / Vibration

| Client | Model | Details | Solution |
|--------|-------|---------|----------|
| Prazirna Smrk | 2.5 kg Cyclone | Seal under motor worn out | Replace seal under motor |
| Šoltýs | 2.5 kg Cyclone | Scratches on scroll housing, bad impeller hub, counterweight welded externally. Progressive worsening. | 1) Remove motor, check bolt torque. 2) Replace impeller. 3) If recurring — send new wheel, old one for balancing |
| Ahoi Marie | 5 kg | After 1 hour of operation | Motor and impeller diagnostics |
| Sump Coffee | 10 electro | Strange sound | Diagnostics |

## Solved Cases — Overheating

| Client | Model | Details | Solution |
|--------|-------|---------|----------|
| Communal Coffee Berlin | 20 electro | Roaster freezes, coffee stuck in chamber, discharge problems | Software update + motor diagnostics |

## Motor Disassembly Procedure

> See [Motor Disassembly Manual](../manuals/general_manual.md)

**⚠️ WARNING:** Must be performed by qualified electrician on de-energized equipment.

1. Remove 10 fastening nuts (decorative linings)
2. Remove decorative and protective motor linings
3. Remove 10 clamping nuts
4. Remove motor with impeller — **requires 2 people** (weight: 35–50 kg)
5. Reinstall in reverse order
6. Tighten until metal contacts seal — **do NOT overtighten** (damages fixing studs)
7. After first start: check motor mount tightness, tighten at any air suction points
