# 🎯 SUGESTÕES CAMPOS CUSTOM INDIVIDUAIS - Análise Completa

**Análise metadata_completa_custom.json (10+ fotos DJI M3E/M4E/L2)** + Strings.py

**Critérios:** 
- **Individual:** Calculado por foto (sem sequência)
- **Útil:** Shapefile, fotogrametria, qualidade voo
- **Simples:** <5 linhas código  
- **Não duplicado:** Fora REQUIRED_FIELDS + CustomUtil atuais

## 📊 **8 Campos Sugeridos (Pronto Shapefile)**

### 1. `lrf_distance` ⭐⭐⭐ **LRF Distance**
**O que faz:** Distância **real medida por laser** da câmera ao solo (m)
**Por que útil:** GSD preciso, valida altitude, fotogrametria
**Fórmula:** `LRFTargetDistance` (já raw)
**Exemplo JSON:** 168.207 m, 87.091 m, 0.000 m
**Attribute:** `LrfDist` (7 chars)
**Shapefile:** Campo numérico direto

### 2. `lrf_altitude` ⭐⭐⭐ **LRF Relative Alt** 
**O que faz:** Altitude **relativa LRF** (drone vs terreno)
**Por que útil:** Topografia instantânea, overlap real
**Fórmula:** `LRFTargetAlt`
**Exemplo:** -0.775 m, -10.729 m, 0.000 m
**Attribute:** `LrfAlt` (6 chars)

### 3. `lrf_abs_altitude` ⭐⭐⭐ **LRF Abs Altitude**
**O que faz:** Altitude **absoluta WGS84** do ponto solo LRF
**Por que útil:** Modelo digital terreno (DTM)
**Fórmula:** `LRFTargetAbsAlt`
**Exemplo:** 211.700 m, 376.100 m
**Attribute:** `LrfAbsA` (7 chars)

### 4. `sensor_temperature` ⭐⭐ **Sensor Temp**
**O que faz:** Temperatura **sensor** (°C)
**Por que útil:** Qualidade imagem (ruído térmico)
**Fórmula:** `SensorTemperature`
**Exemplo:** 44.0°C, 43.0°C, null
**Attribute:** `SensTemp` (8 chars)

### 5. `lens_temperature` ⭐ **Lens Temp**
**O que faz:** Temp **lente** (°C)
**Por que útil:** Desfocagem térmica
**Fórmula:** `LensTemperature`
**Exemplo:** 42.2°C, 44.1°C
**Attribute:** `LensTemp` (8 chars)

### 6. `white_balance_kelvin` ⭐⭐ **Luz Ambiente**
**O que faz:** Temperatura cor luz ambiente (Kelvin)
**Por que útil:** Correção espectral
**Fórmula:** `WhiteBalanceCCT`
**Exemplo:** 4333 K, 4040 K, null
**Attribute:** `WbKelvin` (8 chars)

### 7. `shutter_progress` ⭐⭐ **Vida Câmera**
**O que faz:** % fotos tiradas câmera (vida útil)
**Fórmula:** `ShutterCount / 400000 * 100` (400k máx Zenmuse)
**Exemplo:** 1128/400k = 0.28%
**Attribute:** `ShutProg` (8 chars)

### 8. `ground_sample_distance` ⭐⭐⭐ **GSD m/pixel**
**O que faz:** **Resolução espacial** no solo (m/pixel)
**Fórmula:** `lrf_distance * sensor_pitch_mm / focal_length_mm`
**Exemplo:** 168m * 3.76μm / 12.29mm ≈ 0.051 m/px
**Por que útil:** Planejamento fotogrametria
**Attribute:** `GsdMpx` (6 chars)

## ⚙️ **Outros Candidatos (menos prioritários)**
```
9. image_quality_score = PictureQuality (compressão DJI) → ImgQual (7 chars)
10. lrf_status_clean = 1 if 'Normal' else 0 → LrfFlag (7 chars) 
11. exposure_index = RecommendedExposureIndex → ExpIdx (6 chars)
12. lens_position_um = LensPosition*1000 (μm foco) → LensPosUm (9 chars)
```

## 💾 **Shapefile Impacto (16 atributos novos)**
```
📏 LrfDist | LrfAlt | LrfAbsA | GsdMpx | SensTemp | ShutProg
🌡️ WbKelvin | LensTemp | ImgQual | LrfFlag | ExpIdx
```

**Recomendação:** **Começar com TOP 5** (LRF + GSD + Temps + Shutter)

**Implementar quais? Código pronto em 10min!** 🚀
