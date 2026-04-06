#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CustomUtil - Calcula campos derivados CUSTOM_FIELDS do Strings.py

Recebe output do Manager.collect_metadata() → adiciona 23 campos custom calculados

Dependências: 
- Strings.REQUIRED_FIELDS, Strings.CUSTOM_FIELDS
- math, datetime, numpy (haversine)
"""

import math
from datetime import datetime
from typing import Dict, List, Tuple, Optional
from Strings import Strings

class CustomUtil:
    """Calcula todos os campos CUSTOM_FIELDS para cada foto, validando sequências."""
    
    # Constantes
    MAX_DT_DIFF = 120  # segundos
    MAX_ALT_DIFF = 200  # metros
    MAX_SHUTTER_JUMP = 5000  # fotos (arrochado)
    IDEAL_OVERLAP = 60  # %
    ORTO_SCORE_WEIGHTS = {
        'rtk_high': 30,
        'incidence_low': 25,
        'dewarp': 20,
        'rtk_fresh': 15, 
        'overlap_good': 10
    }
    
    @staticmethod
    def safe_float(val: any, default: float = 0.0) -> float:
        """Converte para float seguro (strings '+123.4' → 123.4)."""
        if val is None:
            return default
        return float(str(val).replace('+', ''))
    
    @staticmethod
    def safe_int(val: any, default: int = 0) -> int:
        """Converte para int seguro."""
        if val is None:
            return default
        return int(str(val))
    
    @staticmethod
    def parse_datetime(dt_str: str) -> datetime:
        """Parse DateTimeOriginal 'YYYY:MM:DD HH:MM:SS'."""
        return datetime.strptime(dt_str, '%Y:%m:%d %H:%M:%S')
    
    @staticmethod
    def get_voo_id(data: Dict) -> str:
        """VOO_ID = drone_sn[:8] + camera_sn[:8] + YYYY-MM-DD."""
        drone_sn = data.get('DroneSerialNumber', 'UNKNOWN')
        camera_sn = data.get('CameraSerialNumber', 'UNKNOWN')
        date_str = CustomUtil.parse_datetime(data['DateTimeOriginal']).strftime('%Y-%m-%d')
        return f"{drone_sn[:8]}_{camera_sn[:8]}_{date_str}"
    
    @staticmethod
    def is_valid_sequence(curr_data: Dict, other_data: Dict, direction: str = 'prev') -> bool:
        """Valida se 2 fotos são sequência válida (mesmo voo)."""
        if other_data is None:
            return False
        
        # 1. Mesmo VOO_ID
        voo_curr = CustomUtil.get_voo_id(curr_data)
        voo_other = CustomUtil.get_voo_id(other_data)
        if voo_curr != voo_other:
            return False
        
        # 2. dt_diff
        dt_curr = CustomUtil.parse_datetime(curr_data['DateTimeOriginal'])
        dt_other = CustomUtil.parse_datetime(other_data['DateTimeOriginal'])
        dt_diff = abs((dt_curr - dt_other).total_seconds())
        if dt_diff > CustomUtil.MAX_DT_DIFF:
            return False
        
        # 3. alt_diff
        alt_curr = CustomUtil.safe_float(curr_data['AbsoluteAltitude'])
        alt_other = CustomUtil.safe_float(other_data['AbsoluteAltitude'])
        alt_diff = abs(alt_curr - alt_other)
        if alt_diff > CustomUtil.MAX_ALT_DIFF:
            return False
        
        # 4. shutter_jump (arrochado)
        shutter_curr = CustomUtil.safe_int(curr_data.get('ShutterCount'))
        shutter_other = CustomUtil.safe_int(other_data.get('ShutterCount'))
        shutter_jump = abs(shutter_curr - shutter_other) > CustomUtil.MAX_SHUTTER_JUMP
        if shutter_jump:
            return False
        
        return True
    
    @staticmethod
    def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """Distância Haversine entre 2 pontos GPS (metros)."""
        R = 6371000  # Raio Terra
        
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)
        
        a = (math.sin(delta_phi / 2) ** 2 + 
             math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c
    
    @staticmethod
    def bearing_angle(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """Azimute bearing entre 2 pontos (0=Norte)."""
        delta_lon = math.radians(lon2 - lon1)
        y = math.sin(delta_lon) * math.cos(math.radians(lat2))
        x = math.cos(math.radians(lat1)) * math.sin(math.radians(lat2)) - \
            math.sin(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.cos(delta_lon)
        bearing = math.degrees(math.atan2(y, x))
        return (bearing + 360) % 360
    
    @staticmethod
    def _calculate_sequence_fields(data: Dict, other_data: Optional[Dict], valid_seq: bool, direction: str) -> Dict:
        """Campos sequência (prev/next)."""
        if not valid_seq or other_data is None:
            prefix = f"{direction}_"
            return {
                f"{prefix}time_since": 0.0,
                f"{prefix}geodesic_distance": 0.0,
                f"{prefix}distance_3d": 0.0,
                f"{prefix}avg_velocity": 0.0,
                f"{prefix}displacement_direction": 0.0
            }
        
        dt_curr = CustomUtil.parse_datetime(data['DateTimeOriginal'])
        dt_other = CustomUtil.parse_datetime(other_data['DateTimeOriginal'])
        dt_diff = abs((dt_curr - dt_other).total_seconds())
        
        # GPS (haversine precisa lat/lon reais - usar LRFTarget se GPS None)
        lat_curr = CustomUtil.safe_float(data.get('LRFTargetLat') or data.get('GpsLatitude', 0))
        lon_curr = CustomUtil.safe_float(data.get('LRFTargetLon') or data.get('GpsLongitude', 0))
        lat_other = CustomUtil.safe_float(other_data.get('LRFTargetLat') or other_data.get('GpsLatitude', 0))
        lon_other = CustomUtil.safe_float(other_data.get('LRFTargetLon') or other_data.get('GpsLongitude', 0))
        
        geo_dist = CustomUtil.haversine(lat_curr, lon_curr, lat_other, lon_other)
        alt_curr = CustomUtil.safe_float(data['AbsoluteAltitude'])
        alt_other = CustomUtil.safe_float(other_data['AbsoluteAltitude'])
        alt_diff = abs(alt_curr - alt_other)
        dist_3d = math.sqrt(geo_dist**2 + alt_diff**2)
        
        avg_vel = dist_3d / dt_diff if dt_diff > 0 else 0.0
        dir_displ = CustomUtil.bearing_angle(lat_curr, lon_curr, lat_other, lon_other)
        
        prefix = f"{direction}_"
        return {
            f"{prefix}time_since": dt_diff,
            f"{prefix}geodesic_distance": geo_dist,
            f"{prefix}distance_3d": dist_3d,
            f"{prefix}avg_velocity": avg_vel,
            f"{prefix}displacement_direction": dir_displ
        }
    
    @staticmethod
    def _calculate_individual_fields(data: Dict) -> Dict:
        #\"\"\"Campos custom individuais derivados.\"\"\"
        shutter_count = CustomUtil.safe_int(data.get('ShutterCount', 0))
        shutter_life_pct = (shutter_count / 400000) * 100
        
        lrf_distance_m = CustomUtil.safe_float(data.get('LRFTargetDistance', 0))
        focal_length_mm = CustomUtil.safe_float(data.get('FocalLength', 12.29))
        sensor_width_mm = 7.49  # M3E/M4E sensor width (20MP 5280px)
        sensor_height_mm = 5.62  # height 3956px
        img_w_px = CustomUtil.safe_float(data.get('ExifImageWidth', 5280))
        img_h_px = CustomUtil.safe_float(data.get('ExifImageHeight', 3956))
        
        # GSD cm/pixel horizontal central - Fallback AbsoluteAltitude se LRF=0
        if lrf_distance_m == 0:
            lrf_distance_m = CustomUtil.safe_float(data.get('AbsoluteAltitude', 0)) * 0.85  # 85% até terreno
        
        pixel_pitch_mm = sensor_width_mm / img_w_px
        gsd_cm_px = (lrf_distance_m * pixel_pitch_mm / focal_length_mm * 100) if lrf_distance_m > 0 and focal_length_mm > 0 else 0
        
        # Heat index - só dividir se 2 valores
        sens_temp = CustomUtil.safe_float(data.get('SensorTemperature'))
        lens_temp = CustomUtil.safe_float(data.get('LensTemperature'))
        if sens_temp > 0 and lens_temp > 0:
            total_heat_index = (sens_temp + lens_temp) / 2
        elif sens_temp > 0:
            total_heat_index = sens_temp
        elif lens_temp > 0:
            total_heat_index = lens_temp  
        else:
            total_heat_index = 0.0
        
        return {
            'shutter_life_pct': shutter_life_pct,
            'ground_sample_distance_cm': gsd_cm_px,
            'total_heat_index': total_heat_index
        }

    @staticmethod
    def _calculate_gimbal_3d(data: Dict) -> Dict:
        """GimbalOffset e 3DSpeed."""
        gim_yaw = CustomUtil.safe_float(data['GimbalYawDegree'])
        flight_yaw = CustomUtil.safe_float(data['FlightYawDegree'])
        gimbal_offset = gim_yaw - flight_yaw - 180
        
        xspd = CustomUtil.safe_float(data['FlightXSpeed'])
        yspd = CustomUtil.safe_float(data['FlightYSpeed'])
        zspd = CustomUtil.safe_float(data['FlightZSpeed'])
        speed_3d = math.sqrt(xspd**2 + yspd**2 + zspd**2)
        
        return {
            'gimbal_offset': gimbal_offset,
            'speed_3d': speed_3d
        }
    
    @staticmethod
    def _calculate_quality_scores(data: Dict, prev_data: Optional[Dict], valid_prev: bool) -> Dict:
        """RTK precision, overlap, ortho score."""
        # RTK Precision
        rtk_flag = data.get('RtkFlag')
        rtk_stds = [
            CustomUtil.safe_float(data.get('RtkStdLon', 999)),
            CustomUtil.safe_float(data.get('RtkStdLat', 999)),
            CustomUtil.safe_float(data.get('RtkStdHgt', 999))
        ]
        avg_std = sum(rtk_stds) / 3
        
        if rtk_flag == '50' and avg_std < 0.02:
            rtk_prec = 'Alta'
        elif avg_std < 0.1:
            rtk_prec = 'Média'
        elif avg_std < 1.0:
            rtk_prec = 'Baixa'
        else:
            rtk_prec = 'Sem RTK'
        
        # Incidence angle
        gim_pitch = CustomUtil.safe_float(data['GimbalPitchDegree'])
        flight_pitch = CustomUtil.safe_float(data['FlightPitchDegree'])
        inc_angle = abs(gim_pitch + flight_pitch)
        
        # Predicted overlap (simplificado sem prev para foto única)
        pred_overlap = 0.0  # será calculado na sequência
        
        # Ortho score
        score = 0
        if rtk_prec == 'Alta': score += 30
        if inc_angle < 5: score += 25
        if data.get('DewarpFlag') == '0': score += 20
        if CustomUtil.safe_float(data.get('RtkDiffAge', 999)) < 2: score += 15
        if pred_overlap > 70: score += 10
        ortho_potential = min(100, score)
        
        # Flags
        abrupt_flag = False  # precisa sequência
        ideal_overlap = pred_overlap >= 60
        
        # Angular velocity gimbal (precisa sequência)
        gim_ang_vel = 0.0
        
        return {
            'rtk_effective_precision': rtk_prec,
            'incidence_angle': inc_angle,
            'predicted_overlap': pred_overlap,
            'is_ideal_overlap': ideal_overlap,
            'abrupt_change_flag': abrupt_flag,
            'gimbal_angular_velocity': gim_ang_vel,
            'orthorectification_potential': ortho_potential
        }
    
    @classmethod
    def calculate_all_custom_fields(cls, metadata_dict: Dict[str, Dict]) -> Dict[str, Dict]:
        """Orquestra todos cálculos custom."""
        # Ordenar por datetime
        sorted_items = sorted(metadata_dict.items(), 
                            key=lambda x: cls.parse_datetime(x[1]['DateTimeOriginal']))
        
        result = {}
        for i, (filename, data) in enumerate(sorted_items):
            prev_item = sorted_items[i-1] if i > 0 else None
            next_item = sorted_items[i+1] if i < len(sorted_items)-1 else None
            
            prev_data = prev_item[1] if prev_item else None
            next_data = next_item[1] if next_item else None
            
            # Validações sequência
            valid_prev = cls.is_valid_sequence(data, prev_data)
            valid_next = cls.is_valid_sequence(next_data, data) if next_data else False
            
            # Sequência campos
            prev_seq = cls._calculate_sequence_fields(data, prev_data, valid_prev, 'prev')
            next_seq = cls._calculate_sequence_fields(data, next_data, valid_next, 'next')
            
            # Campos individuais NOVOS
            individual = cls._calculate_individual_fields(data)
            
            # Outros
            gim_3d = cls._calculate_gimbal_3d(data)
            quality = cls._calculate_quality_scores(data, prev_data, valid_prev)
            
            # Flags validação
            validation = {
                'is_valid_sequence_prev': valid_prev,
                'is_valid_sequence_next': valid_next,
                'voo_id': cls.get_voo_id(data)
            }
            
            custom = {**individual, **gim_3d, **quality, **prev_seq, **next_seq, **validation}
            
            result[filename] = {**data, **custom}
        
        return result


if __name__ == "__main__":
    from Manager import Manager
    manager = Manager()
    raw_data = manager.collect_metadata(r"G:\np\IMAGENS")
    custom_data = CustomUtil.calculate_all_custom_fields(raw_data)
    print(f"Custom fields adicionados! Total fotos: {len(custom_data)}")
    print(list(custom_data[list(custom_data.keys())[0]].keys())[-20:])  # últimos 20 campos

