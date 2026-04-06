# 🔍 Análise GSD=0.0 nos Drones

## **Por que alguns drones não calculam GSD?**

**Fato observado no `metadata_completa_custom.json`:**

| Drone | LRFStatus | LRFTargetDistance | AbsoluteAltitude | GSD Resultado |
|-------|-----------|-------------------|------------------|---------------|
| **5_LUZI (M3E)** | "Normal" | `"0.000"` | ~389m | **0.0** |
| **M3E_DRTK...** | "Normal" | `"0.000"` | ~397m | **0.0** |

## **Causa Raiz:**
```
LRFStatus = "Normal" ➜ Laser funcionando
LRFTargetDistance = "0.000" ➜ NÃO atingiu alvo/detectou solo
```

**DJI LRF (Laser Range Finder):**
- Dispara laser para baixo do drone
- Se **não reflete** (grama alta, água, sombra, noite, alvo muito próximo/distante) → `0.000`
- Altitude normal (~120-380m) ➜ LRF deveria funcionar

## **Soluções para GSD sem LRF:**

### 1. **Fallback: AbsoluteAltitude**
```
GSD_altitude = (AbsoluteAltitude * pixel_pitch_mm / FocalLength * 100)
Exemplo: 168m * (7.49mm/5280px) / 12.29mm * 100 = ~10.25cm/pixel
```

### 2. **Config CustomUtil.py:**
```python
lrf_distance = CustomUtil.safe_float(data.get('LRFTargetDistance', 0))
if lrf_distance == 0:
    lrf_distance = CustomUtil.safe_float(data.get('AbsoluteAltitude', 0)) * 0.85  # 85% terreno

gsd_cm_px = (lrf_distance * pixel_pitch_mm / focal_length_mm * 100)
```

## **Recomendação:**
- **M3E/M4E LRF ativo**: `LRFTargetDistance` direto (~5-20cm/px)
- **LRF=0**: Fallback `AbsoluteAltitude * 0.85` (~10-40cm/px realista)
- **Sem altitude**: `0.0` (flag para revisar voo)

**Implementar fallback?** GSD sempre útil para fotogrametria! 🎯
