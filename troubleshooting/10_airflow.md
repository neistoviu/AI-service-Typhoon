# 10 — Airflow Loss

> **Total cases:** 6  
> **Frequency:** ★★☆☆☆  
> **Affected models:** 2.5 kg Cyclone, 5 kg

---

## Symptoms

- Coffee doesn't "fly" (no fluidized bed) in chamber
- Weak bean agitation
- Roasting efficiency drops
- Uneven roasting

## Diagnostic Algorithm

1. **CYCLONE MESH** — most common cause! (see [mesh cleaning](../standard_procedures/cyclone_mesh_cleaning.md))
2. **Seal under motor** — can sag and leak
3. **Cyclone motor socket** — plug may come loose
4. **PHASE CHECK** — critical after any power outage! (see [phase check](../standard_procedures/phase_check.md))

## Solved Cases

| Client | Model | Details | Solution |
|--------|-------|---------|----------|
| Flying Pig | 2.5 kg Cyclone | After power outage — incorrect phasing | Fix phasing (phase check procedure) |
| RöstFlair | 2.5 kg Cyclone | Dirty mesh | Clean mesh |
| Michal Dvorak | 5 kg | Dirty mesh + collapsed seal under motor | Clean mesh + replace seal |
| TRE-261 | 2.5 kg Cyclone | Coffee not flying → dirty mesh. After cleaning, recurred after 4 batches. Cyclone motor plug disconnects periodically. | 1) Clean mesh. 2) Check and fix cyclone motor socket. |
| Melco Coffee | — | — | Standard diagnostics |

## ⚠️ Unresolved Cases

| Client | Model | Details | Status |
|--------|-------|---------|--------|
| Chatwick Specialty Coffee | 5 kg | With completely clean mesh, plate, and no gaps — zero airflow at exhaust "10". When partially closed — normal. | **Possibly excessive building ventilation draft — non-standard case** |

## ⚠️ IMPORTANT

**After ANY power outage — always check motor phasing!** Incorrect phasing means motors run backwards → zero airflow → coffee doesn't roast.

## Manual References

- Check all parts tightly closed
- Check mesh inside cyclone system
- Verify PLC mode (not PC mode)
- Check main/cyclone motors and circuit breakers are on
- Check motor phasing (motors must run clockwise)
