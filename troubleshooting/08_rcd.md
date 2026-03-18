# 08 — RCD (GFCI) Tripping

> **Total cases:** 4  
> **Frequency:** ★★★☆☆  
> **Affected models:** 2.5 kg, 5 kg

---

## Symptoms

- RCD/GFCI trips when starting roaster
- RCD trips when turning off with main switch
- RCD trips when plugging in destoner

## ⚠️ ROOT CAUSE IDENTIFIED

**Heater neutral wire connected to the GROUNDING bus** instead of the neutral bus → instant RCD trip when heaters engage.

## Solution Procedure

**Requirements:** Electrician with multimeter at client's location.

1. Disassemble electrical cabinet harness
2. Trace the cable going to heaters
3. **Reconnect neutral wire** from grounding bus to neutral bus
4. Verify all connections
5. Test with RCD

## Solved Cases

| Client | Model | Details | Solution |
|--------|-------|---------|----------|
| Chocolat Purokao | 2.5 kg | Multiple incidents. At 30% TEN and 20% motor, RCD trips. Neutral wire on grounding bus confirmed. | Reconnect neutral wire with client's electrician |
| Chocolat Purokao | 2.5 kg | RCD trips when turning off roaster with main switch | After motors stop, wait 15 min, then turn off |
| Plaumann Tostadurica | — | Simply plugging destoner into outlet trips breaker. Destoner unused for a month. | Destoner diagnostics with electrician |
| Luca | — | RCD trips when turning off roaster | Connection diagnostics |
| Sam Yalla Coffee | 20 electro | Breaker tripped during roasting. UPS didn't activate. Jaw motor tried to over-close — sensors offset. | Move sensor slightly right (reduce motor pressure) + close gap with tie rods + adjust neck gap |

## Diagnostic Steps from Service Mode

1. Determine **exact moment** of tripping (startup / shutdown / during operation)
2. Test from **service mode**: enable TENs and main motor at various power levels
3. Check client's **RCD model** (type and rating)
4. Check **neutral wire connection**

## ⚠️ SYSTEMIC ISSUE

**Factory did NOT test roasters through RCD connection.** Known since June, case TRE-286. This means any new installation may encounter this issue.
