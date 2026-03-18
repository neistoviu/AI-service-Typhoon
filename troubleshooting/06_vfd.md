# 06 — Variable Frequency Drive (VFD)

> **Total cases:** 8  
> **Frequency:** ★★★☆☆  
> **Affected models:** 20 gas, 5 kg, 20 electro, 10 electro

---

## Symptoms

- Main motor breaker trips
- Roaster won't start
- Error codes on VFD display (e.g., E001)
- Motor doesn't respond

## Diagnostic Algorithm

1. Check **wire integrity** from breaker to VFD
2. **Disconnect VFD power wires** and try to start roaster
3. If roaster starts with VFD disconnected → **diagnosis confirmed: VFD replacement needed**
4. For error codes: photograph VFD display and send to technologist

See [Kinco VFD Check Procedure](../standard_procedures/kinco_vfd_check.md)

## Solved Cases — VFD Replacement

| Client | Model | Details | Solution |
|--------|-------|---------|----------|
| James Price | 20 gas | After 350 kg of roasting, main motor breaker tripped. Wires intact. Roaster starts with VFD disconnected. | VFD replacement + parameter configuration |
| First Crack Coffee Roasters | 20 electro | VFD + breaker burned | Replace both VFD and breaker |
| Erin Maguire | 20 gas | VFD burned | VFD replacement |
| Momentum-C | 20 electro | Short circuit in VFD (11 kW roaster) | VFD replacement |
| Efficiense Oy | 5 kg (filter) | Filter VFD burned after 2 years | Replace filter VFD (cause under investigation) |
| Velvet coffee | 10 electro | Short circuit | VFD replacement |
| Guzo coffee | 20 electro | VFD failure | VFD replacement |
| Sam Yallah | — | — | VFD replacement |

## Solved Cases — VFD Error E001

| Client | Model | Details | Solution |
|--------|-------|---------|----------|
| Daniel Baum | 10 gas | Error E001. Increased parameter A006 by +2 seconds → error recurred during BBP. | **Partial fix only.** Increase A006 parameter. ⚠️ Requires further diagnostics. |

## Solved Cases — Missing Phase

| Client | Model | Details | Solution |
|--------|-------|---------|----------|
| Jade | — | Missing phase on VFD | Check electrical connection, phasing |
| TRE-359 | — | One phase doesn't reach roaster | Check connection with client's electrician |
