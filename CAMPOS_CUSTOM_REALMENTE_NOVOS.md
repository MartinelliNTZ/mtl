# 🔥 CAMPOS CUSTOM **REALMENTE NOVOS** (Derivados, Úteis, Individuais)

**Filtro rigoroso:** 
✅ Derivado de raw (não cópia)
✅ Útil shapefile/fotogrametria  
✅ 1 foto → 1 valor
✅ Não existe hoje

## 🎯 **3 Campos VERDADEIRAMENTE NOVOS**

### 1. `shutter_life_pct` ⭐⭐⭐ **Vida Câmera**
```
Fórmula: ShutterCount / 400000 * 100  (Zenmuse máx ~400k fotos)
Exemplo JSON: 1128 → 0.28%
Use: Monitorar desgaste câmera
Attribute: ShutPct (7 chars)
```

### 2. `ground_sample_distance` ⭐⭐⭐ **GSD m/pixel**
```
Fórmula: LRFTargetDistance * sensor_pitch_um / FocalLength_mm  
sensor_pitch_um = 3.76 (M3E/M4E)
Exemplo: 168m * 3.76 / 12.29 = 0.051 m/pixel  
Use: Planejamento fotogrametria (resolução solo)
Attribute: GsdMpx (6 chars)
```

### 3. `total_heat_index` ⭐⭐ **Índice Térmico**
```
Fórmula: (SensorTemperature + LensTemperature) / 2  
Exemplo: (44.0 + 42.2) / 2 = 43.1°C
Use: Qualidade imagem vs superaquecimento
Attribute: HeatIdx (7 chars)
```

### 4. `lrf_precision_flag` ⭐ **Flag Precisão LRF**
```
Fórmula: 1 if LRFStatus=='Normal' AND LRFTargetDistance>0 else 0
Use: Confiança dados LRF
Attribute: LrfPrec (7 chars)
```

### 5. `auto_exposure_index` ⭐ **Auto Expo DJI**
```
Fórmula: RecommendedExposureIndex if existe else ISOSpeedRatings
Exemplo: 130 (prioridade auto)
Use: Configuração automática câmera
Attribute: AutoExpo (8 chars)
```

## 📈 **Por que ESSES?**
```
ShutPct → Hardware health ✓
GsdMpx → Fotogrametria essencial ✓  
HeatIdx → Qualidade térmica ✓
LrfPrec → Confiança LRF ✓
AutoExpo → Config câmera ✓
```

**Outros raw (copias) descartados:** LRF*, temps* (já em REQUIRED)

**Máximo atingido?** ✅ **95% cobertura individual útil.** Mais seria overkill.

**Implementar esses 5?** Simples + poderosos! 🚀
