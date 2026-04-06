# ANÁLISE e Fórmulas para Campos CUSTOM_FIELDS (17 campos)

**Objetivo:** Documentar **EXATAMENTE** como calcular cada campo `custom` a partir dos dados brutos (Manager.collect_metadata).

**Dependências:** Manager já fornece REQUIRED_FIELDS. CustomUtil receberá `{foto.jpg: {required_fields_dict}}` e retornará `{foto.jpg: {required + custom_fields}}`.

**Estrutura CustomUtil:**
```
class CustomUtil:
    @staticmethod
    def calculate_all_custom_fields(metadata_dict: Dict[str, Dict]) -> Dict[str, Dict]:
        # Ordena por DateTimeOriginal
        sorted_metadata = sort_by_datetime(metadata_dict)
        result = {}
        for i, (filename, data) in enumerate(sorted_metadata):
            prev_data = sorted_metadata[i-1] if i > 0 else None
            custom_data = CustomUtil._calculate_individual_fields(data, prev_data)
            result[filename] = {**data, **custom_data}
        return result
```

## 🧮 FÓRMULAS por Campo (ENGLISH keys)

### 1. **GimbalOffset** `[GimOffset]`
```
GimbalYawDegree - FlightYawDegree - 180
Exemplo: -173.20 - (-174.00) - 180 = 180.8°
```
**Inputs:** `GimbalYawDegree`, `FlightYawDegree`  
**Output:** float graus

### 2. **3DSpeed** `[3DSpeed]`
```
sqrt(FlightXSpeed² + FlightYSpeed² + FlightZSpeed²)
Exemplo: sqrt((-14.0)² + (-1.5)² + 0²) = 14.1 m/s
```
**Inputs:** `FlightXSpeed`, `FlightYSpeed`, `FlightZSpeed`  
**Output:** float m/s

### 3. **time_since_previous** `[TimePrv]` *(per image)*
```
parse_date(DateTimeOriginal atual) - parse_date(DateTimeOriginal anterior)
Formato: '%Y:%m:%d %H:%M:%S' → datetime → seconds diff
Se primeira foto: 0
```
**Inputs:** `DateTimeOriginal` atual + anterior  
**Output:** float segundos

### 4. **geodesic_distance_previous** `[GeoDstP]`
```
haversine(GpsLatitude_ant, GPSLongitude_ant, GpsLatitude_atual, GPSLongitude_atual)
Fórmula Haversine para distância 2D no solo (m)
```
**Inputs:** `GpsLatitude`, `GpsLongitude` anterior + atual  
**Output:** float metros

### 5. **distance_3d_previous** `[Dist3DP]`
```
sqrt(geodesic_distance_previous² + (AbsoluteAltitude_atual - AbsoluteAltitude_ant)²)
```
**Inputs:** `geodesic_distance_previous`, `AbsoluteAltitude` anterior + atual  
**Output:** float metros 3D

### 6. **avg_velocity_between_photos** `[AvgVelB]`
```
distance_3d_previous / time_since_previous  (se time > 0)
```
**Inputs:** `distance_3d_previous`, `time_since_previous`  
**Output:** float m/s

### 7. **linear_velocity_instant** `[LinVelI]`
```
sqrt(FlightXSpeed² + FlightYSpeed² + FlightZSpeed²)  [= 3DSpeed mas independente de sequência]
```
**Inputs:** `FlightXSpeed`, `FlightYSpeed`, `FlightZSpeed`  
**Output:** float m/s

### 8. **displacement_direction** `[DirDispl]` 
```
bearing_angle(GpsLat_ant, GPSLong_ant, GpsLat_atual, GPSLong_atual)
Azimute (0-360°) do vetor deslocamento (atan2 + ajustes)
```
**Inputs:** GPS coords anterior + atual  
**Output:** float graus (0=Norte)

### 9. **incidence_angle** `[IncAngle]`
```
abs(GimbalPitchDegree + FlightPitchDegree)
Ângulo real vs nadir (90°=vertical)
```
**Inputs:** `GimbalPitchDegree`, `FlightPitchDegree`  
**Output:** float graus

### 10. **estimated_coverage** `[EstCover]`
```
(width_m, height_m) = (altitude * sensor_width / focal_length * cos(incidence_angle), ...)
FOV fixo por câmera (M3M: 84° H, 65° V estimado)
```
**Inputs:** `AbsoluteAltitude`, `FocalLength`, `incidence_angle`, `ExifImageWidth/Height`  
**Output:** tuple (float, float) metros

### 11. **predicted_overlap** `[PredOver]`
```
max(0, min(100, (1 - geodesic_distance_previous / estimated_coverage[0]) * 100))
Sobreposição longitudinal estimada
```
**Inputs:** `geodesic_distance_previous`, `estimated_coverage.width`  
**Output:** float %

### 12. **rtk_effective_precision** `[RTKPrec]`
```
if RtkFlag == '50' and avg(RtkStdLon,Lat,Hgt) < 0.02: 'Alta'
elif avg < 0.1: 'Média' 
elif avg < 1.0: 'Baixa' 
else: 'Sem RTK'
```
**Inputs:** `RtkFlag`, `RtkStdLon`, `RtkStdLat`, `RtkStdHgt`  
**Output:** str ('Alta', 'Média', 'Baixa', 'Sem RTK')

### 13. **is_ideal_overlap** `[IdealOvl]`
```
predicted_overlap >= 60
```
**Inputs:** `predicted_overlap`  
**Output:** bool

### 14. **abrupt_change_flag** `[AbrChgF]`
```
time_since_previous > 5s OR geodesic_distance_previous > 50m
```
**Inputs:** `time_since_previous`, `geodesic_distance_previous`  
**Output:** bool

### 15. **gimbal_angular_velocity** `[GimAngV]`
```
abs(GimbalYawDegree_atual - GimbalYawDegree_ant) / time_since_previous
```
**Inputs:** `GimbalYawDegree` anterior + atual, `time_since_previous`  
**Output:** float °/s

### 16. **orthorectification_potential** `[OrtoPot]`
```
score = 0
if rtk_effective_precision == 'Alta': +30
if incidence_angle < 5: +25  
if DewarpFlag == 0: +20
if RtkDiffAge < 2: +15
if predicted_overlap > 70: +10
score = min(100, score)
```
**Inputs:** vários acima  
**Output:** int 0-100

## 📋 Próximos
1. Criar `CustomUtil.py` com essas fórmulas EXATAS
2. Integrar Manager: `manager.collect_metadata(folder) → customutil.calculate(...)`
3. Output terminal + arquivo JSON/CSV

**OK para implementar assim?** Algum ajuste nas fórmulas?
