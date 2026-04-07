# Validação Regras CustomUtil - Análise saida_terminal.py + Respostas

**Problemas Identificados do Feedback + saida_terminal.py:**

## 🔍 **1. Serial ausente?**
**Análise:** 100% das 10 fotos têm `DroneSerialNumber` e `CameraSerialNumber` preenchidos.
```
Exemplos únicos:
- 1581F5FKC254R00DK102 (M3M)
- 1581F6GKB243900400B2 (Matrice 350 RTK) 
- 1581F5FKD23BG00DXZW2 (M3M)
- 1581F5FH82577002N061 (M3E)
```
**Solução:** Fallback: se `DroneSerialNumber` is None → usar `DroneModel` + `ShutterCount` range (±1000 fotos)

## 🌀 **2. Curva no voo?**
**Problema:** Fotos são de **10 voos diferentes** (datas 2026:03:02, 2026:02:06, 2025:12:20, etc.)
**Análise bearing:** displacement_direction já captura curvas (atan2 calcula direção real)
**Solução:** Agrupar por "VOO_ID":
```
VOO_ID = hash(DroneSerialNumber + CameraSerialNumber + str(parse_date(DateTimeOriginal).date()))
Fotos do mesmo dia + mesmo drone = mesmo voo
```

## 🔋 **3. Troca de bateria?**
**Sinal:** `ShutterCount` reset (ex: 235796 → 6970 → 130765 → 14940)
**Regra atual:** `dt_diff < 60s` já bloqueia gaps grandes
**Melhoria:** Detectar "VOO_INICIADO" quando ShutterCount < mediana_shutter_anterior * 0.1

## 📊 **Regras Finais VALID_SEQUENCE (VOO_ID + sequência)**

```
def get_voo_id(data):
    drone_sn = data.get('DroneSerialNumber', 'UNKNOWN')
    camera_sn = data.get('CameraSerialNumber', 'UNKNOWN')
    date_str = parse_datetime(data['DateTimeOriginal']).strftime('%Y-%m-%d')
    return f"{drone_sn[:8]}_{camera_sn[:8]}_{date_str}"

def is_valid_sequence(curr_data, prev_data, direction='prev'):
    voo_curr = get_voo_id(curr_data)
    voo_prev = get_voo_id(prev_data)
    if voo_curr != voo_prev: return False
    
    dt_curr = parse_datetime(curr_data['DateTimeOriginal'])
    dt_prev = parse_datetime(prev_data['DateTimeOriginal']) if direction=='prev' else parse_datetime(curr_data['DateTimeOriginal'])
    
    dt_diff = abs((dt_curr - dt_prev).total_seconds())
    alt_curr = safe_float(curr_data['AbsoluteAltitude'])
    alt_prev = safe_float(prev_data['AbsoluteAltitude'])
    alt_diff = abs(alt_curr - alt_prev)
    
    shutter_curr = int(curr_data.get('ShutterCount', 0))
    shutter_prev = int(prev_data.get('ShutterCount', 0))
    shutter_jump = abs(shutter_curr - shutter_prev) > 10000  # troca bateria
    
    return dt_diff < 120 and alt_diff < 200 and not shutter_jump  # relaxado

def safe_float(val):
    if val is None: return 0.0
    return float(str(val).replace('+',''))
```

## ➡️ **Bidirecional CONFIRMADO**
Adicionar `_next` para todos campos sequência:
```
time_since_previous / time_to_next
geodesic_distance_previous / geodesic_distance_next
distance_3d_previous / distance_3d_next
avg_velocity_between_photos / avg_velocity_to_next
displacement_direction / displacement_direction_next
is_valid_sequence_prev / is_valid_sequence_next
```

**TOTAL CAMPOS:** 17 + 6 bidirectional = 23

## 📝 **Descriptions com Fórmula Resumida**
```
Exemplo:
"time_since_previous": "... [dt_curr - dt_prev se valid_seq(VOO_ID+dt<120s+alt<200m+no_shutter_jump)]"
```

**Novo UPDATE_CUSTOM_FIELDS_PLAN.md criado? OK para:**
1. Regras VOO_ID + relaxadas  
2. Fallback serial (Model+Shutter)  
3. 23 campos (bidir)  
4. Criar CustomUtil.py

Confirma? 🚁
