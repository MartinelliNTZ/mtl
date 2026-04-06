# 📋 NOVOS CAMPOS CUSTOM - SIMPLES e ÚTEIS

**Baseado no JSON `metadata_completa_custom.json`**

Já temos **~80 campos** (raw + custom). Aqui vão **8 novos campos INDIVIDUAIS** simples:

## ✅ **8 Campos Prontos (cálculo direto)**

| Nome Inglês | Abreviação | O que é? | Como calcular | Exemplo JSON |
|-------------|------------|----------|---------------|--------------|
| `lrf_distance` | `LrfDist` | Distância laser ao solo | `LRFTargetDistance` | 168.207 m |
| `lrf_altitude` | `LrfAlt` | Altitude LRF (relativa) | `LRFTargetAlt` | -0.775 m |
| `sensor_temperature` | `SensTemp` | Temp sensor | `SensorTemperature` | 44.0 °C |
| `lens_temperature` | `LensTemp` | Temp lente | `LensTemperature` | 42.2 °C |
| `white_balance_kelvin` | `WbKelvin` | Cor luz (Kelvin) | `WhiteBalanceCCT` | 4333 K |
| `shutter_progress_percent` | `ShutPrct` | % vida câmera | `ShutterCount / 300000 * 100` | 0.37% |
| `lrf_status_flag` | `LrfFlag` | LRF OK? (1/0) | `1 if LRFStatus=='Normal' else 0` | 1 |
| `ground_sample_distance` | `GsdMp` | GSD m/pixel | `lrf_distance * 0.00376mm / (12.29mm focal)` | ~0.052 m/px |

## 🎯 **Por que ÚTEIS?**
```
Shapefile pronto → LrfDist | SensTemp | GsdMp | ShutPrct
Fotogrametria → GSD + LRF altitude + temp sensor
Qualidade → WB Kelvin + LRF status + Shutter %
```

## 🔧 **Implementação (5 linhas)**
```
# Em CustomUtil._calculate_individual_fields():
custom['lrf_distance'] = safe_float(data.get('LRFTargetDistance'))
custom['sensor_temperature'] = safe_float(data.get('SensorTemperature'))
custom['ground_sample_distance'] = custom['lrf_distance'] * 0.00376 / 12.29 if custom['lrf_distance'] else 0
# etc...
```

**Adicionar essas 8? Simples e valiosas!** 👍
