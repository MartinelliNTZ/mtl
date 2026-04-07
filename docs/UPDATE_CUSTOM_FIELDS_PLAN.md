# UPDATE: Regras CustomUtil + Bidirecional + Validação + Descriptions

**Ajustes baseados no feedback:**

## 🎯 **Regras de Negócio para Foto Anterior/Posterior**
```
REGRA: Duas fotos são "SEQ_ÚNICAS" se:
1. MESMO_DRONE = DroneSerialNumber igual E CameraSerialNumber igual (±5%)
2. MESMO_VOIO = |DateTimeOriginal_diff| < 60s E |AbsoluteAltitude_diff| < 100m
3. SEQUENCIA = bearing_direction diff < 90° (mesmo sentido)

SE NÃO válida sequência → prev/next = None, campos = null/0
```

**Validação por foto:**
```
def is_valid_sequence(current_data, prev_data):
    if not prev_data: return False
    drone_sn_curr = current_data.get('DroneSerialNumber')
    drone_sn_prev = prev_data.get('DroneSerialNumber')
    if drone_sn_curr != drone_sn_prev: return False
    
    dt_diff = abs(parse_datetime(current_data['DateTimeOriginal']) - parse_datetime(prev_data['DateTimeOriginal'])).total_seconds()
    alt_diff = abs(float(current_data['AbsoluteAltitude'].replace('+','')) - float(prev_data['AbsoluteAltitude'].replace('+','')))
    
    if dt_diff > 60 or alt_diff > 100: return False
    return True
```

## 🔄 **Bidirecional (Anterior + Posterior)**
Adicionar campos POSTERIOR (simétricos):
```
time_to_next, geodesic_distance_next, distance_3d_next, avg_velocity_to_next
displacement_direction_next (sentido)
is_valid_next_sequence
```

## 📝 **Descriptions Atualizadas em Strings.py**
Adicionar resumo da fórmula no final (tooltip):
```
Exemplo atualizado:
"TimePrv - tempo anterior válida (dt=DateTimeOriginal_prev, valid_seq=True)"
"GeoDstP - haversine(lat/lon_prev→curr) se valid_seq, senão null"
```

## 🆕 **Campos Adicionais (Bidirecional)**
```
time_to_next [TimeNxt]
geodesic_distance_next [GeoDstN] 
distance_3d_next [Dist3DN]
avg_velocity_to_next [AvgVelN]
displacement_direction_next [DirNxt]
is_valid_sequence_prev [ValPrev]
is_valid_sequence_next [ValNext]
```

**TOTAL: 17 + 7 = 24 campos custom**

## 🔧 **CustomUtil Estrutura Final**
```
class CustomUtil:
    @staticmethod
    def calculate_all_custom_fields(metadata_dict):
        # 1. Ordenar por DateTimeOriginal
        sorted_md = sorted(metadata_dict.items(), key=lambda x: parse_datetime(x[1]['DateTimeOriginal']))
        
        # 2. Calcular bidirecional
        for i, (filename, data) in enumerate(sorted_md):
            prev_data = sorted_md[i-1][1] if i>0 else None
            next_data = sorted_md[i+1][1] if i<len(sorted_md)-1 else None
            
            # Validar sequences
            valid_prev = is_valid_sequence(data, prev_data)
            valid_next = is_valid_sequence(next_data, data) if next_data else False
            
            # Calcular campos
            custom = {
                'is_valid_sequence_prev': valid_prev,
                'is_valid_sequence_next': valid_next,
                **_calculate_time_distance_velocity(data, prev_data, valid_prev, direction='prev'),
                **_calculate_time_distance_velocity(data, next_data, valid_next, direction='next'),
                **_calculate_gimbal_3d(data),
                **_calculate_quality_scores(data, prev_data, valid_prev)
            }
            result[filename] = {**data, **custom}
        
        return result
```

**OK para:**
1. Adicionar 7 campos POSTERIOR  
2. Atualizar descriptions com fórmulas resumidas  
3. Regras validação drone/voo  
4. Criar CustomUtil.py + integrar Manager?

Algum ajuste nas regras/fórmulas? 👍
