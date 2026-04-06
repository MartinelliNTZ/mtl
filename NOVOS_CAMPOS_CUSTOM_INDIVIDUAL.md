# 🚁 NOVOS CAMPOS INDIVIDUAIS para CUSTOM_FIELDS - Análise metadata_completa_custom.json + Strings.py

**Análise:** 
- **~60 campos raw** em REQUIRED_FIELDS (OS+EXIF+XMP)
- **23 campos derivados** já em CustomUtil (sequência + qualidade)
- **Oportunidades:** 12 novos campos **INDIVIDUAIS** (sem sequência/prev-next)

## 🆕 **12 Campos Individuais Propostos**

| Campo English | Attribute (≤9) | Descrição/Fórmula | Input Raw | Tipo | Prioridade |
|---------------|----------------|-------------------|-----------|------|------------|
| **lrf_distance** | LrfDist | `LRFTargetDistance` (distância laser ao solo) | `LRFTargetDistance` | float m | ⭐⭐⭐ |
| **lrf_altitude** | LrfAlt | `LRFTargetAlt` (altitude relativa LRF) | `LRFTargetAlt` | float m | ⭐⭐⭐ |
| **lrf_abs_altitude** | LrfAbsAlt | `LRFTargetAbsAlt` (altitude absoluta LRF) | `LRFTargetAbsAlt` | float m | ⭐⭐⭐ |
| **sensor_temp** | SensTemp | `SensorTemperature` (°C sensor) | `SensorTemperature` | float °C | ⭐⭐⭐ |
| **lens_temp** | LensTemp | `LensTemperature` (°C lente) | `LensTemperature` | float °C | ⭐⭐ |
| **white_balance_temp** | WbTemp | `WhiteBalanceCCT` (Kelvin cor luz ambiente) | `WhiteBalanceCCT` | int K | ⭐⭐ |
| **shutter_progress** | ShutterPr | `ShutterCount / max_shutter_detected` (progresso câmera %) | `ShutterCount` | float % | ⭐⭐ |
| **ground_sample_distance** | GsdMpx | `LRFTargetDistance * pixel_size / FocalLength` (GSD m/pixel) | `LRFTargetDistance`, `FocalLength`, `ExifImageWidth` | float m/px | ⭐⭐⭐ |
| **image_quality_score** | ImgQual | `PictureQuality` (compressão DJI 0-100) | `PictureQuality` | int | ⭐ |
| **lrf_status_clean** | LrfStat | `'Normal'` → 1, `'NoTarget'` → 0, outros → -1 | `LRFStatus` | int | ⭐ |
| **exposure_index** | ExpIndex | `RecommendedExposureIndex` ou `ISOSpeedRatings` | `RecommendedExposureIndex` | int | ⭐ |
| **lens_position_um** | LensPos | `LensPosition * 1000` (μm foco) | `LensPosition` | float μm | ⭐ |

## 📊 **Detalhes Técnicos**

### 1. **LRF Fields** (3⭐ - Laser Range Finder)
```
lrf_distance = safe_float(LRFTargetDistance)
lrf_altitude = safe_float(LRFTargetAlt)  
lrf_abs_altitude = safe_float(LRFTargetAbsAlt)
```
**Uso:** Precisão vertical + GSD cálculo

### 2. **Temperaturas** (2-3⭐)
```
sensor_temp = safe_float(SensorTemperature)
lens_temp = safe_float(LensTemperature)
```
**Uso:** Qualidade imagem térmica

### 3. **GSD (Ground Sample Distance)** ⭐⭐⭐
```
pixel_size = 0.00376  # M3E/M4E sensor (mm) 
gsd_mpx = LRFTargetDistance * pixel_size / (FocalLength * 1000)  # m/pixel
```
**Uso:** Escala espacial fotogrametria

### 4. **Shutter Progress** ⭐⭐
```
# Detecta max_shutter no dataset
shutter_progress = ShutterCount / max_shutter_dataset * 100
```
**Uso:** Vida útil câmera

### 5. **Status LRF** ⭐
```
lrf_status_clean = 1 if LRFStatus=='Normal' else (0 if 'NoTarget' in str(LRFStatus) else -1)
```

## 🎯 **Impacto Shapefile**
```
+12 atributos ≤9 chars → Shapefile pronto
GsdMpx | LrfDist | SensTemp | WbTemp | ShutterPr | etc.
```

**Adicionar ao Strings.CUSTOM_FIELDS e CustomUtil._calculate_individual_fields?**

**Qual priorizar? Todas? Alguma ajustar fórmula?** 👍
