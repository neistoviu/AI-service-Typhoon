# 04 — Temperature Loss / Drop

> **Total cases:** 15  
> **Frequency:** ★★★★☆  
> **Affected models:** 5 kg, 2.5 kg Cyclone, 10 electro, 20 gas

---

## Symptoms

- Roaster doesn't reach target temperature
- Roasting time increases significantly
- Rate of Rise (RoR) drops
- Coffee not developing properly

## Diagnostic Algorithm

1. **Measure heater resistance** → send [standard instruction](../standard_procedures/heater_resistance_check.md)
2. **Check relay** → send [relay check instruction](../standard_procedures/relay_check.md)
3. **Check seals/gaps** — especially at the BACK, under plate, at neck
4. **Cyclone mesh** — contamination = airflow loss = temperature loss
5. **Check breakers** — are all switched on?
6. **Request startup video** from client for remote analysis

## Solved Cases

| Client | Model | Details | Solution |
|--------|-------|---------|----------|
| Jacek Kowal | 5 kg | — | Standard TEN measurement → escalate to electrician |
| Jade Dinsdale | 5 kg | — | Standard diagnostics |
| Josef Suska | 2.5 kg Cyclone | — | Standard diagnostics |
| Christian | 5 kg | "Roaster not heating up, takes much longer. Was fine last week." | Standard TEN + relay diagnostics |
| Mohaji s.r.o. | — | — | Standard diagnostics |
| Ovride Specialty Coffee | 5 kg | Roasts taking 7–8 min instead of 5 min | Standard power diagnostics |
| Broadway Coffee Roasters | 10 electro | Client claimed relay not working, but tests showed all OK | Request video of startup process for analysis |
| Daniel Baum | — | Minor loss in first roast phase | Standard diagnostics |

## ⚠️ Unresolved Cases

| Client | Model | Details | Status |
|--------|-------|---------|--------|
| Šoltýs | 2.5 kg Cyclone | Roaster periodically doesn't heat. Breakers OK, relay and TEN tested — all working. | **Intermittent — no solution found** |
| Erin Maguire | 20 gas | At 201°C for 7 min, coffee very dark (Agtron 52). Burner 10-45 can't cope. | **Possibly coefficient in software — needs engineer review** |

## Manual References

- Check operation of modules in control cabinet
- Check heating elements
- Check heater circuit breaker is switched on
- Verify PLC/PC mode setting (use PLC mode only)
