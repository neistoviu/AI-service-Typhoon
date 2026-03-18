# 01 — Heating Elements (TEN / Heaters)

> **Total cases:** 22  
> **Frequency:** ★★★★★ (most common issue)  
> **Affected models:** Typhoon 5 kg (primary), 2.5 kg, 10 electro, 20 kg

---

## Symptoms

- Roaster doesn't reach target temperature or heats too slowly
- Roasting time increases significantly
- Visible damage on heating spirals
- Smoke from heater area at temperatures above 150°C
- Melting plastic elements near heaters

## Diagnostic Algorithm

1. **Measure heater resistance** with multimeter (see [standard procedure](../standard_procedures/heater_resistance_check.md))
2. **Visual inspection** of spirals for integrity/damage
3. **Check relay** — if relay leaks current, this causes repeated heater burnout (see [relay check](../standard_procedures/relay_check.md))
4. **Measure voltage** across phases under load (detect neutral shift)

## Solved Cases

### Standard Replacement Cases

| Client | Model | Details | Solution |
|--------|-------|---------|----------|
| Trey Binkley | 5 kg | Standard burnout | TEN replacement |
| Endal Poland | 5 kg | — | TEN replacement |
| Torrefaction des trois maisons | 5 kg | — | TEN replacement |
| Nicki Sturrock | 5 kg | — | TEN replacement |
| Jade Dinsdale | 5 kg | Burned fins | TEN replacement |
| Paixrva (×2) | 5 kg | Two separate incidents | TEN replacement |
| Cubby House | 5 kg | — | TEN replacement |
| Michiel Hillen (×3) | 5 kg | Multiple visits | TEN + temperature module replacement |
| Luminous | 5 kg | — | TEN replacement |
| Jaroslav Hlaváč | 2.5 kg | Burned after 4 years | TEN replacement (1 unit sold) |
| Michal Jakoubek | 2.5 kg | Recurring burnout | TEN replacement |
| Rostislav Krivanek | 2.5 kg | After power reconnection | TEN + 2 relay contacts replacement |

### Complex / Root-Cause Cases

#### Neutral Shift — Back Yard Coffee LTD (Typhoon 20 kg)
**Problem:** Heaters keep burning out. Phase voltage under load: Phase 1 = 236V, Phase 2 = 360V, Phase 3 = 400V. Relay was leaking current.

**Root cause:** Neutral shift in client's electrical supply.

**Solution:**
1. Check voltage per phase on roaster AND on client's distribution panel
2. Neutral shift detected → involve client's electrician to fix building wiring
3. Replace relay
4. Send pre-tested replacement heaters

#### After Power Reconnection — Rostislav Krivanek (2.5 kg)
**Problem:** TEN burned on first startup after power reconnection, plus 2 relay contacts.  
**Solution:** Replace TEN + relay contacts. Verify proper reconnection.

#### Heater + Temperature Module — Michiel Hillen (5 kg)
**Problem:** Multiple visits. Heater + temperature module failed together.  
**Solution:** Replace both components.

## ⚠️ Critical Rules

**On repeated burnout, ALWAYS check:**
- Voltage across phases under load (neutral shift detection)
- Relay condition (does it leak current?)
- Quality of client's electrical connection
- On Typhoon 5 kg: check for related wire burnout to main switch (see [Category 11](11_electrical.md))

## Manual References

- Heater circuit breaker location: Electrical cabinet (see manual page for your model)
- All three phases must reach the roaster (commissioning check)
- After 150–200 hours: retighten all wire terminals
