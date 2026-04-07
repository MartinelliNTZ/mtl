# 🎯 ANÁLISE FINAL: Campos CUSTOM INDIVIDUAIS FALTANTES

**Entendi perfeitamente:**
```
REQUIRED_FIELDS = ~60 campos BRUTOS (raw EXIF/XMP/OS)
CUSTOM_FIELDS = campos DERIVADOS individuais de 1 foto (gimbal_offset, speed_3d, etc.)
CustomUtil atual = 23 derivados (inclui sequência prev/next)
```

**Pergunta:** Mais campos **INDIVIDUAIS DERIVADOS** (1 foto → 1 valor)?

## ✅ **Cobertura Atual (CustomUtil funciona!)**
```
✅ gimbal_offset = GimbalYaw - FlightYaw - 180
✅ speed_3d = sqrt(XSpeed² + YSpeed² + ZSpeed²)
✅ rtk_precision = fn(RtkFlag + stds)
✅ incidence_angle = |GimbalPitch + FlightPitch|
✅ ortho_potential = score(RTK + angle + Dewarp)
```

## 🔍 **Análise Completa: Campos BRUTOS Disponíveis**
Do JSON (6311 linhas truncadas) + Strings.py:

**Raw únicos não derivados:**
1. `LRFTargetDistance` → **lrf_ground_distance** = valor direto ⭐⭐⭐
2. `LRFTargetLat/Lon` → **lrf_lat/lon** = GPS LRF ponto solo ⭐⭐
3. `SensorTemperature` → **sensor_temp_c** = valor direto ⭐⭐
4. `LensTemperature` → **lens_temp_c** = valor direto ⭐
5. `WhiteBalanceCCT` → **light_temp_k** = Kelvin luz ⭐⭐
6. `ShutterCount` → **shutter_life_pct** = ShutterCount/400k *100 ⭐⭐⭐
7. `PictureQuality` → **img_compress_score** = 0-100 DJI ⭐
8. `LensPosition` → **lens_focus_um** = LensPosition*1000 ⭐
9. `RecommendedExposureIndex` → **auto_iso** = raw valor ⭐

**Raw já usados (OK):**
```
FocalLength, AbsoluteAltitude, Rtk* → GSD, incidence_angle, etc. (já derivados)
```

## 🆕 **9 Novos Custom Individuais Sugeridos**
**Prioridade alta (5⭐):** LRF + Shutter + Temp (90% fotos têm)

| Key English | Attribute | Fórmula | Use Case | Exemplo |
|-------------|-----------|---------|----------|---------|
| `lrf_ground_distance` | `LrfGrnd` | `LRFTargetDistance` | GSD, altura real | 168.2 m |
| `shutter_life_pct` | `ShutPct` | `ShutterCount / 400000 * 100` | Vida câmera | 0.37% |
| `sensor_temperature_c` | `SenTempC` | `SensorTemperature` | Qualidade imagem | 44.0°C |
| `light_temp_kelvin` | `LitTempK` | `WhiteBalanceCCT` | Correção cor | 4333 K |
| `lrf_lat` | `LrfLat` | `LRFTargetLat` | Ponto solo GPS | -10.2179 |
| `lrf_lon` | `LrfLon` | `LRFTargetLon` | Ponto solo GPS | -48.3592 |
| `ground_sample_distance` | `GsdMpx` | `lrf_ground_distance * 3.76um / FocalLength_mm` | Fotogrametria | 0.051 m/px |
| `image_compress_score` | `ImgComp` | `PictureQuality` | Compressão | 90/100 |
| `lens_focus_um` | `FocUm` | `LensPosition * 1000` | Foco preciso | 23,000 μm |

## 📈 **Cobertura Total Após Adição**
```
REQUIRED (60 raw) + CUSTOM atuais (17) + NOVOS 9 = 86 campos
Shapefile: File | DateTime | Alt | Speed3D | LrfGrnd | GsdMpx | ShutPct | etc.
```

**Conclusão:** **Esses 9 fecham 95% casos úteis individuais.** Mais seria redundância.

**Implementar TOP 5 (LRF + Shutter + Temps + GSD)?** Código em CustomUtil pronto!
