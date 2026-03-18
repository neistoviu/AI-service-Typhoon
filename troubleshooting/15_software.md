# 15 — Software and Controller

> **Total cases:** 7  
> **Frequency:** ★★☆☆☆  
> **Affected models:** 2.5 kg, 5 kg, 20 electro, 30 electro

---

## Symptoms

- PLC no response
- Roaster freezes / hangs during operation
- Artisan won't connect
- RoR interference / incorrect readings
- Profile won't repeat correctly
- Mac-Artisan connection issues

## Solved Cases

| Client | Model | Details | Solution |
|--------|-------|---------|----------|
| Chocolat Purokao | 2.5 kg | PLC no response | Restart / PLC diagnostics |
| Communal Coffee Berlin | 20 electro | Overheating + roaster freezing | Software update |
| Emil Peltekov | 30 electro | Program issues | Software update |
| Jade Dinsdale | 5 kg | Mac-Artisan connection | Configure connection (see Artisan setup below) |
| Caffe4U | — | Sensor and program problem | Software update / reconfiguration |
| Biz s.r.o | — | Program burner problem | Software update |

## ⚠️ Unresolved Cases

| Client | Model | Details | Status |
|--------|-------|---------|--------|
| Nostos Coffee | — | Artisan won't connect | Under investigation |
| OBEDIENTPENGUIN | — | RoR interference | Under investigation |
| Солярис | — | Profile won't repeat | Under investigation |

## Artisan Connection Setup

1. Artisan version must be **2.8.4 or latest**
2. Go to **Config → Machine → Typhoon Roasters**
3. Select roaster type:
   - **Shoproaster** — 2.5 kg, 5 kg
   - **Hybrid** — 10 kg, 20 kg, 30 kg
4. IP address: **192.168.0.210**
5. Select energy type (gas/electric) and capacity
6. Configure network adapter:
   - IP: **192.168.0.211** or **192.168.0.12**
   - Mask: **255.255.255.0**
7. **Restart computer** (required by Artisan)
8. Verify adapter settings saved after restart

**Cropster:** https://help.cropster.com/en/knowledge/typhoon-roasting-intelligence-ri-setup

## Key Software Parameters

| Parameter | Description |
|-----------|-------------|
| SP | Temperature setpoint |
| UP | Upper sensor (bean temperature) |
| Down | Lower sensor (air temperature) |
| ROR | Rate of Rise (30-second interval) |
| Motor % | Main motor power |
| Mixer | Rotation speed (0–10) |
| Power % | Heater power |
| PLC/PC | Mode selector (**use PLC only**) |
