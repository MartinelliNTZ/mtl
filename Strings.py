class Strings:
    
    {"img1":{"file":"G:\\np\\IMAGENS\\1_CERRADO (1).JPG","GPSMapDatum":"WGS-84","Software":"DJI GO 4"},
     "img2":{"file":"G:\\np\\IMAGENS\\2_CERRADO (1).JPG","GPSMapDatum":"WGS-84","Software":"DJI GO 4"}
     }
    REQUIRED_FIELDS = {
        "file": {
            "normalized": "file",
            "core": "os",
            "attribute": "File",
            "description": "",
        },
        "path": {
            "normalized": "path",
            "core": "os",
            "attribute": "Path",
            "description": "",
        },
        "format": {
            "normalized": "format",
            "core": "os",
            "attribute": "FormatMod",
            "description": "",
        },
        "size_mb": {
            "normalized": "size_mb",
            "core": "os",
            "attribute": "SizeMB",
            "description": "",
        },
        "GPSMapDatum": {
            "normalized": "EXIF:GPSInfo:GPSMapDatum",
            "core": "EXIF",
            "attribute": "GPSDatum",
            "description": "Datum da foto",
        },
        "Model": {
            "normalized": "EXIF:Model",
            "core": "EXIF",
            "attribute": "Model",
            "description": "Modelo da Camera",
        },
        "Software": {
            "normalized": "EXIF:Software",
            "core": "EXIF",
            "attribute": "Firmware",
            "description": "Versao do Firmware",
        },
        "XResolution": {
            "normalized": "EXIF:XResolution",
            "core": "EXIF",
            "attribute": "DPIWidth",
            "description": "Largura em DPI",
        },
        "YResolution": {
            "normalized": "EXIF:YResolution",
            "core": "EXIF",
            "attribute": "DPIHeight",
            "description": "Altura em DPI",
        },
        "ShutterSpeedValue": {
            "normalized": "EXIF:ShutterSpeedValue",
            "core": "EXIF",
            "attribute": "ShutterSp",
            "description": "Velocidade do Obturador",
        },
        "DateTimeOriginal": {
            "normalized": "EXIF:DateTimeOriginal",
            "core": "EXIF",
            "attribute": "DateTime",
            "description": "Data exata da foto no fuso horario",
        },
        "ApertureValue": {
            "normalized": "EXIF:ApertureValue",
            "core": "EXIF",
            "attribute": "ApertureV",
            "description": "Abertura da lente",
        },
        "MaxApertureValue": {
            "normalized": "EXIF:MaxApertureValue",
            "core": "EXIF",
            "attribute": "MaxApertV",
            "description": "Abertura maxima da lente",
        },
        "LightSource": {
            "normalized": "EXIF:LightSource",
            "core": "EXIF",
            "attribute": "LightSour",
            "description": "Luminosidade do dia",
        },
        "FocalLength": {
            "normalized": "EXIF:FocalLength",
            "core": "EXIF",
            "attribute": "FocalLeng",
            "description": "Distancia focal real da lente em milimetros",
        },
        "ExifImageWidth": {
            "normalized": "EXIF:ExifImageWidth",
            "core": "EXIF",
            "attribute": "WidthPX",
            "description": "Largura em pixels",
        },
        "ExifImageHeight": {
            "normalized": "EXIF:ExifImageHeight",
            "core": "EXIF",
            "attribute": "HeightPX",
            "description": "Altura em pixels",
        },
        "ExposureTime": {
            "normalized": "EXIF:ExposureTime",
            "core": "EXIF",
            "attribute": "ExpTime",
            "description": "Tempo de Exposicao",
        },
        "FNumber": {
            "normalized": "EXIF:FNumber",
            "core": "EXIF",
            "attribute": "FNumber",
            "description": "Numero da Abertura",
        },
        "ExposureProgram": {
            "normalized": "EXIF:ExposureProgram",
            "core": "EXIF",
            "attribute": "ExpProg",
            "description": "Programa de exposicao definido pelo drone",
        },
        "ISOSpeedRatings": {
            "normalized": "EXIF:ISOSpeedRatings",
            "core": "EXIF",
            "attribute": "ISOSpeed",
            "description": "Sensibilidade do sensor a luz",
        },
        "ExposureMode": {
            "normalized": "EXIF:ExposureMode",
            "core": "EXIF",
            "attribute": "ExpMode",
            "description": "Modo de exposicao utilizado pela camera",
        },
        "LensSpecification": {
            "normalized": "EXIF:LensSpecification",
            "core": "EXIF",
            "attribute": "Lens",
            "description": "(FocalLengthMin, FocalLengthMax, ApertureMin, ApertureMax)",
        },
        "DigitalZoomRatio": {
            "normalized": "EXIF:DigitalZoomRatio",
            "core": "EXIF",
            "attribute": "ZoomRatio",
            "description": "Zoom digital tem sempre que ta 0",
        },
        "GpsStatus": {
            "normalized": "EXIF:GPSInfo:GPSStatus",
            "core": "xmp_bloco_1",
            "attribute": "GpsStatus",
            "description": "Se RTK ou outro formato",
        },
        "AltitudeType": {
            "normalized": "xmp_bloco_1:drone-dji:AltitudeType",
            "core": "xmp_bloco_1",
            "attribute": "Ytype",
            "description": "Se RTK ou outro formato",
        },
        "GpsLatitude": {
            "normalized": "EXIF:GPSInfo:GPSLatitude",
            "core": "xmp_bloco_1",
            "attribute": "GpsLat",
            "description": "Latitude da aeronave",
        },
        "GpsLongitude": {
            "normalized": "EXIF:GPSInfo:GPSLongitude",
            "core": "xmp_bloco_1",
            "attribute": "GPSLong",
            "description": "Longitude da aeronave",
        },
        "AbsoluteAltitude": {
            "normalized": "xmp_bloco_1:drone-dji:AbsoluteAltitude",
            "core": "xmp_bloco_1",
            "attribute": "AbsY",
            "description": "Altitude absoluta da aeronave",
        },
        "RelativeAltitude": {
            "normalized": "xmp_bloco_1:drone-dji:RelativeAltitude",
            "core": "xmp_bloco_1",
            "attribute": "RelativeY",
            "description": "Altitude Relativa do ponto de decolagem",
        },
        "GimbalRollDegree": {
            "normalized": "xmp_bloco_1:drone-dji:GimbalRollDegree",
            "core": "xmp_bloco_1",
            "attribute": "GimbRoll",
            "description": "Rolagem do Gimbal(180 normal)(sim com acabeça)",
        },
        "GimbalYawDegree": {
            "normalized": "xmp_bloco_1:drone-dji:GimbalYawDegree",
            "core": "xmp_bloco_1",
            "attribute": "GimbYaw",
            "description": "Direcao do Gimbal",
        },
        "GimbalPitchDegree": {
            "normalized": "xmp_bloco_1:drone-dji:GimbalPitchDegree",
            "core": "xmp_bloco_1",
            "attribute": "GimbPitch",
            "description": "Inclinacao do Gimbal verticamente",
        },
        "FlightRollDegree": {
            "normalized": "xmp_bloco_1:drone-dji:FlightRollDegree",
            "core": "xmp_bloco_1",
            "attribute": "DroneRoll",
            "description": "Rolagem da aeronave",
        },
        "FlightYawDegree": {
            "normalized": "xmp_bloco_1:drone-dji:FlightYawDegree",
            "core": "xmp_bloco_1",
            "attribute": "DroneYaw",
            "description": "Direcao da aeronave",
        },
        "FlightPitchDegree": {
            "normalized": "xmp_bloco_1:drone-dji:FlightPitchDegree",
            "core": "xmp_bloco_1",
            "attribute": "DronePitc",
            "description": "Inclinacao da aeronave",
        },
        "FlightXSpeed": {
            "normalized": "xmp_bloco_1:drone-dji:FlightXSpeed",
            "core": "xmp_bloco_1",
            "attribute": "XSpeed",
            "description": "Velocidade de voo X",
        },
        "FlightYSpeed": {
            "normalized": "xmp_bloco_1:drone-dji:FlightYSpeed",
            "core": "xmp_bloco_1",
            "attribute": "YSpeed",
            "description": "Velocidade de voo Y",
        },
        "FlightZSpeed": {
            "normalized": "xmp_bloco_1:drone-dji:FlightZSpeed",
            "core": "xmp_bloco_1",
            "attribute": "ZSpeed",
            "description": "Velocidade de voo Z",
        },
        "RtkFlag": {
            "normalized": "xmp_bloco_1:drone-dji:RtkFlag",
            "core": "xmp_bloco_1",
            "attribute": "RtkFlag",
            "description": "Qualidade do sinal do drone",
        },
        "RtkStdLon": {
            "normalized": "xmp_bloco_1:drone-dji:RtkStdLon",
            "core": "xmp_bloco_1",
            "attribute": "RtkStdLon",
            "description": "Desvio Padrao do RTK Longitude",
        },
        "RtkStdLat": {
            "normalized": "xmp_bloco_1:drone-dji:RtkStdLat",
            "core": "xmp_bloco_1",
            "attribute": "RtkStdLat",
            "description": "Desvio Padrao do RTK Latitude",
        },
        "RtkStdHgt": {
            "normalized": "xmp_bloco_1:drone-dji:RtkStdHgt",
            "core": "xmp_bloco_1",
            "attribute": "RtkStdHgt",
            "description": "Desvio Padrao do RTK Altitude",
        },
        "RtkDiffAge": {
            "normalized": "xmp_bloco_1:drone-dji:RtkDiffAge",
            "core": "xmp_bloco_1",
            "attribute": "RtkDifAge",
            "description": "Tempo da Ultima correcao RTK",
        },
        "DewarpFlag": {
            "normalized": "xmp_bloco_1:drone-dji:DewarpFlag",
            "core": "xmp_bloco_1",
            "attribute": "Dewarp",
            "description": "Dewarp habilitado =0; desabilitado = nada",
        },
        "UTCAtExposure": {
            "normalized": "xmp_bloco_1:drone-dji:UTCAtExposure",
            "core": "xmp_bloco_1",
            "attribute": "UTCTime",
            "description": "Data e hora no GPS Time",
        },
        "ShutterCount": {
            "normalized": "xmp_bloco_1:drone-dji:ShutterCount",
            "core": "xmp_bloco_1",
            "attribute": "ShotCount",
            "description": "Numero Total de Fotos tiradas com a camera",
        },
        "FocusDistance": {
            "normalized": "xmp_bloco_1:drone-dji:FocusDistance",
            "core": "xmp_bloco_1",
            "attribute": "FocusDist",
            "description": "Distancia de foco",
        },
        "CameraSerialNumber": {
            "normalized": "xmp_bloco_1:drone-dji:CameraSerialNumber",
            "core": "xmp_bloco_1",
            "attribute": "CameraID",
            "description": "Numero Serial da Camera",
        },
        "DroneModel": {
            "normalized": "xmp_bloco_1:drone-dji:DroneModel",
            "core": "xmp_bloco_1",
            "attribute": "DronModel",
            "description": "Modelo do Drone",
        },
        "DroneSerialNumber": {
            "normalized": "xmp_bloco_1:drone-dji:DroneSerialNumber",
            "core": "xmp_bloco_1",
            "attribute": "DroneID",
            "description": "Numero Serial do Drone",
        },
        "CaptureUUID": {
            "normalized": "xmp_bloco_1:drone-dji:CaptureUUID",
            "core": "xmp_bloco_1",
            "attribute": "CaptureID",
            "description": "ID da captura para unir fotos Multespectral em drones M3M",
        },
        "PictureQuality": {
            "normalized": "xmp_bloco_1:drone-dji:PictureQuality",
            "core": "xmp_bloco_1",
            "attribute": "ImgQualit",
            "description": "Nivel de compressao da imagem",
        },
        "segmentos_total": {
            "normalized": "JPEG:segmentos_total",
            "core": "xmp_bloco_1",
            "attribute": "Segments",
            "description": "Numero de segmentos do JPG",
        },
        "SensorTemperature": {
            "normalized": "xmp_bloco_1:drone-dji:SensorTemperature",
            "core": "xmp_bloco_1",
            "attribute": "SensTemp",
            "description": "Temperatura do sensor",
        },
        "LRFStatus": {
            "normalized": "xmp_bloco_1:drone-dji:LRFStatus",
            "core": "xmp_bloco_1",
            "attribute": "LRFStatus",
            "description": "Status do Laser Range Finder",
        },
        "LRFTargetDistance": {
            "normalized": "xmp_bloco_1:drone-dji:LRFTargetDistance",
            "core": "xmp_bloco_1",
            "attribute": "LRFDist",
            "description": "Distancia do LRF(Laser Range Finder) ate o ponto central da foto no solo",
        },
        "LRFTargetLon": {
            "normalized": "xmp_bloco_1:drone-dji:LRFTargetLon",
            "core": "xmp_bloco_1",
            "attribute": "LRFLong",
            "description": "Longitude medida pelo LRF(Laser Range Finder)",
        },
        "LRFTargetLat": {
            "normalized": "xmp_bloco_1:drone-dji:LRFTargetLat",
            "core": "xmp_bloco_1",
            "attribute": "LRFLati",
            "description": "Latitude medida pelo LRF(Laser Range Finder)",
        },
        "LRFTargetAlt": {
            "normalized": "xmp_bloco_1:drone-dji:LRFTargetAlt",
            "core": "xmp_bloco_1",
            "attribute": "LRFY",
            "description": "Altitude Relativa do ponto de decolagem LRF(Laser Range Finder)",
        },
        "LRFTargetAbsAlt": {
            "normalized": "xmp_bloco_1:drone-dji:LRFTargetAbsAlt",
            "core": "xmp_bloco_1",
            "attribute": "LrfAbsAlt",
            "description": "Altitude Absoluta do ponto de decolagem LRF(Laser Range Finder)",
        },
        "WhiteBalanceCCT": {
            "normalized": "xmp_bloco_1:drone-dji:WhiteBalanceCCT",
            "core": "xmp_bloco_1",
            "attribute": "WhiteBlc",
            "description": "E um valor numerico que indica a cor da luz no ambiente onde a foto foi tirada, medida em Kelvin (K)",
        },
        "SensorFPS": {
            "normalized": "xmp_bloco_1:drone-dji:SensorFPS",
            "core": "xmp_bloco_1",
            "attribute": "SensorFPS",
            "description": "Taxa de quadros (frames por segundo)",
        },
        "RecommendedExposureIndex": {
            "normalized": "EXIF:RecommendedExposureIndex",
            "core": "xmp_bloco_1",
            "attribute": "REI",
            "description": "Indice de Exposicao Recomendado - REI",
        },
        "LensPosition": {
            "normalized": "xmp_bloco_1:drone-dji:LensPosition",
            "core": "xmp_bloco_1",
            "attribute": "LensPosit",
            "description": "Posicao da Lente",
        },
        "LensTemperature": {
            "normalized": "xmp_bloco_1:drone-dji:LensTemperature",
            "core": "xmp_bloco_1",
            "attribute": "LensTemp",
            "description": "Temperatura da Lente",
        },
    }
    
    
    DECIMAL_PLACES = 2
    
    CUSTOM_FIELDS = {
        "GimbalOffset": {
            "normalized": "xmp_bloco_1:drone-dji:GimbalOffset",
            "core": "custom",
            "attribute": "GimOffset",
            "description": "Deslocamento angular mínimo do gimbal em relação à aeronave em graus (GimbalYawDegree - FlightYawDegree - 180, normalizado para menor ângulo). Valores: 0-180°. Valor referência: <1°. [GimOffset]"
        },
        "3DSpeed": {
            "normalized": "Custom:3DSpeed",
            "core": "custom",
            "attribute": "3DSpeed",
            "description": "Velocidade total 3D da aeronave em m/s, calculada como sqrt(FlightXSpeed² + FlightYSpeed² + FlightZSpeed²). Valores: 0-50 m/s. Valor referência: <10 m/s para voos estáveis. [3DSpeed]"
        },
        "time_since_previous": {
            "normalized": "Custom:time_since_previous",
            "core": "custom",
            "attribute": "TimePrv",
            "description": "Tempo em segundos desde a foto anterior. Valores: 0-120 s. Valor referência: 2-5 s para cadência ideal. [TimePrv]"
        },
        "geodesic_distance_previous": {
            "normalized": "Custom:geodesic_distance_previous",
            "core": "custom",
            "attribute": "GeoDstP",
            "description": "Distância horizontal em metros entre posições GPS consecutivas (fórmula Haversine). Valores: 0-100 m. Valor referência: 20-50 m para sobreposição adequada. [GeoDstP]"
        },
        "distance_3d_previous": {
            "normalized": "Custom:distance_3d_previous",
            "core": "custom",
            "attribute": "Dist3DP",
            "description": "Distância 3D em metros entre posições consecutivas (horizontal + altitude). Valores: 0-100 m. Valor referência: 20-50 m. [Dist3DP]"
        },
        "avg_velocity_between_photos": {
            "normalized": "Custom:avg_velocity_between_photos",
            "core": "custom",
            "attribute": "AvgVelB",
            "description": "Velocidade média em m/s entre fotos consecutivas. Valores: 0-20 m/s. Valor referência: 5-10 m/s. [AvgVelB]"
        },
        "linear_velocity_instant": {
            "normalized": "Custom:linear_velocity_instant",
            "core": "custom",
            "attribute": "LinVelI",
            "description": "Velocidade instantânea 3D em m/s. Valores: 0-50 m/s. Valor referência: <10 m/s. [LinVelI]"
        },
        "displacement_direction": {
            "normalized": "Custom:displacement_direction",
            "core": "custom",
            "attribute": "DirDispl",
            "description": "Azimute do deslocamento em graus (0=Norte). Valores: 0-360°. Valor referência: varia por missão. [DirDispl]"
        },
        "incidence_angle": {
            "normalized": "Custom:incidence_angle",
            "core": "custom",
            "attribute": "IncAngle",
            "description": "Ângulo de incidência em graus (ângulo entre câmera e vertical). Valores: 0-180°. Valor referência: <5° para nadir. [IncAngle]"
        },
        "estimated_coverage": {
            "normalized": "Custom:estimated_coverage",
            "core": "custom",
            "attribute": "EstCover",
            "description": "Tupla (largura, altura) em metros da cobertura estimada no solo. Valores: (0-200, 0-150) m. Valor referência: depende altitude. [EstCover]"
        },
        "predicted_overlap": {
            "normalized": "Custom:predicted_overlap",
            "core": "custom",
            "attribute": "PredOver",
            "description": "Percentual de sobreposição longitudinal com foto anterior. Valores: 0-100%. Valor referência: >60%. [PredOver]"
        },
        "rtk_effective_precision": {
            "normalized": "Custom:rtk_effective_precision",
            "core": "custom",
            "attribute": "RTKPrec",
            "description": "Classificação textual da precisão RTK. Valores: Alta, Média, Baixa, Sem RTK. Valor referência: Alta. [RTKPrec]"
        },
        "is_ideal_overlap": {
            "normalized": "Custom:is_ideal_overlap",
            "core": "custom",
            "attribute": "IdealOvl",
            "description": "Booleano indicando se sobreposição >=60%. Valores: True/False. Valor referência: True. [IdealOvl]"
        },
        "abrupt_change_flag": {
            "normalized": "Custom:abrupt_change_flag",
            "core": "custom",
            "attribute": "AbrChgF",
            "description": "Flag de mudança brusca (tempo ou distância >2x mediana). Valores: True/False. Valor referência: False. [AbrChgF]"
        },
        "gimbal_angular_velocity": {
            "normalized": "Custom:gimbal_angular_velocity",
            "core": "custom",
            "attribute": "GimAngV",
            "description": "Variação angular do gimbal em °/s. Valores: 0-100 °/s. Valor referência: <1 °/s. [GimAngV]"
        },
        "orthorectification_potential": {
            "normalized": "Custom:orthorectification_potential",
            "core": "custom",
            "attribute": "OrtoPot",
            "description": "Score de potencial para ortorretificação (0-100). Valores: 0-100. Valor referência: >80. [OrtoPot]"
        },
        "shutter_life_pct": {
            "normalized": "Custom:shutter_life_pct",
            "core": "custom",
            "attribute": "ShutPct",
            "description": "% de vida útil do obturador. Valores: 0-100%. Valor referência: <50%. [ShutPct]"
        },
        "ground_sample_distance_cm": {
            "normalized": "Custom:ground_sample_distance_cm",
            "core": "custom",
            "attribute": "GsdCmPx",
            "description": "GSD em cm/pixel. Valores: 0-10 cm. Valor referência: <2 cm. [GsdCmPx]"
        },
        "total_heat_index": {
            "normalized": "Custom:total_heat_index",
            "core": "custom", 
            "attribute": "HeatIdx",
            "description": "Índice térmico médio em °C. Valores: 20-60 °C. Valor referência: <40 °C. [HeatIdx]"
        },
        "speed_3d_kmh": {
            "normalized": "Custom:speed_3d_kmh",
            "core": "custom",
            "attribute": "SpdKmH",
            "description": "Velocidade 3D do drone em km/h. Valores: 0-180 km/h. Valor referência: <36 km/h. [SpdKmH]"
        },
        "yaw_alignment_error": {
            "normalized": "Custom:yaw_alignment_error",
            "core": "custom",
            "attribute": "YawErr",
            "description": "Erro de alinhamento yaw em graus. Valores: 0-180°. Valor referência: <5°. [YawErr]"
        },
        "motion_blur_risk": {
            "normalized": "Custom:motion_blur_risk",
            "core": "custom",
            "attribute": "BlurRisk",
            "description": "Risco de motion blur em pixels. Valores: 0-5. Valor referência: <0.5. [BlurRisk]"
        },
        "exposure_value_ev": {
            "normalized": "Custom:exposure_value_ev",
            "core": "custom",
            "attribute": "EV",
            "description": "Valor de exposição EV. Valores: 8-16. Valor referência: 12-14. [EV]"
        },
        "light_source_classification": {
            "normalized": "Custom:light_source_classification",
            "core": "custom",
            "attribute": "LSrcClass",
            "description": "Classificação textual da fonte de luz EXIF. Valores: Daylight, Fluorescent, etc. Valor referência: Daylight. [LSrcClass]"
        },
        "light_consistency": {
            "normalized": "Custom:light_consistency",
            "core": "custom",
            "attribute": "LightCons",
            "description": "Consistência entre LightSource e CCT. Valores: Consistent, Inconsistent, Unknown. Valor referência: Consistent. [LightCons]"
        },
        "vertical_stability": {
            "normalized": "Custom:vertical_stability",
            "core": "custom",
            "attribute": "VertStb",
            "description": "Variação vertical em metros. Valores: 0-10 m. Valor referência: <1 m. [VertStb]"
        },
        "trajectory_smoothness": {
            "normalized": "Custom:trajectory_smoothness",
            "core": "custom",
            "attribute": "TrajSmt",
            "description": "Diferença angular de direção em graus. Valores: 0-180°. Valor referência: <10°. [TrajSmt]"
        },
        "speed_variation_index": {
            "normalized": "Custom:speed_variation_index",
            "core": "custom",
            "attribute": "SpdVar",
            "description": "Índice de variação de velocidade (coeficiente de variação). Valores: 0-1. Valor referência: <0.1. [SpdVar]"
        },
        "rtk_stability_score": {
            "normalized": "Custom:rtk_stability_score",
            "core": "custom",
            "attribute": "RtkStab",
            "description": "Score de estabilidade RTK (0-100). Valores: 0-100. Valor referência: >90. [RtkStab]"
        },
        "capture_efficiency": {
            "normalized": "Custom:capture_efficiency",
            "core": "custom",
            "attribute": "CapEff",
            "description": "Eficiência de captura (distância/cobertura). Valores: 0-1. Valor referência: 0.5-0.8. [CapEff]"
        },
        "photogrammetry_quality_index": {
            "normalized": "Custom:photogrammetry_quality_index", 
            "core": "custom",
            "attribute": "PQI",
            "description": "Índice de qualidade fotogramétrica (0-100). Valores: 0-100. Valor referência: >80. [PQI]"
        },
        "strip_id": {
            "normalized": "Custom:strip_id",
            "core": "custom",
            "attribute": "StripID",
            "description": "ID da faixa de voo. Valores: 1+. Valor referência: incremental. [StripID]"
        }
    }
    
    LIGHT_SOURCE_VALUES = {
        0: {
            "value": "Unknown",
            "description": "Fonte de luz desconhecida ou não especificada. Este valor é frequentemente usado quando o dado não foi registrado ou é inválido."
        },
        1: {
            "value": "Daylight",
            "description": "Luz do dia, referente à iluminação solar natural. Corresponde ao balanço de branco para condições diurnas, com temperatura de cor por volta de 5200K-6500K."
        },
        2: {
            "value": "Fluorescent",
            "description": "Iluminação fluorescente, típica de lâmpadas de luz do dia. Apresenta uma temperatura de cor variando geralmente entre 3000K e 6500K, dependendo do tipo da lâmpada."
        },
        3: {
            "value": "Tungsten",
            "description": "Iluminação de tungstênio (lâmpada incandescente), com tom amarelado característico. A temperatura de cor normalmente fica na faixa dos 2800K a 3200K."
        },
        4: {
            "value": "Flash",
            "description": "Iluminação fornecida pelo flash da câmera. Este valor é registrado quando o flash é disparado e atua como fonte de luz principal ou de preenchimento."
        },
        9: {
            "value": "Fine Weather",
            "description": "Tempo claro, condição de luz do dia sem nuvens. Representa uma iluminação de alta intensidade e com temperatura de cor bem definida."
        },
        10: {
            "value": "Cloudy Weather",
            "description": "Tempo nublado, onde a luz do sol é difusa devido à cobertura de nuvens. Geralmente resulta em uma temperatura de cor mais alta, por volta de 6500K-7500K."
        },
        11: {
            "value": "Shade",
            "description": "Área de sombra, onde a iluminação solar é bloqueada por obstáculos. A luz refletida do céu tende a ser mais azulada, com temperatura de cor superior a 7000K."
        },
        12: {
            "value": "Daylight Fluorescent",
            "description": "Luz fluorescente do tipo Daylight, que emula a cor da luz do dia. Apresenta uma temperatura de cor típica entre 5700K e 7100K, indicada para ambientes internos."
        },
        13: {
            "value": "Day White Fluorescent",
            "description": "Luz fluorescente branca diurna, com uma tonalidade neutra. A temperatura de cor dessa fonte varia de 4600K a 5400K."
        },
        14: {
            "value": "Cool White Fluorescent",
            "description": "Luz fluorescente branca fria, com uma aparência mais azulada. Este tipo de iluminação opera com uma temperatura de cor na faixa de 3800K a 4500K."
        },
        15: {
            "value": "White Fluorescent",
            "description": "Luz fluorescente branca, oferecendo um equilíbrio entre tons quentes e frios. Sua temperatura de cor geralmente está entre 3250K e 3800K."
        },
        16: {
            "value": "Warm White Fluorescent",
            "description": "Luz fluorescente branca quente, com tonalidade mais amarelada. É comum em lâmpadas do tipo WW, operando com temperatura de cor de 2600K a 3250K."
        },
        17: {
            "value": "Standard Light A",
            "description": "Luz padrão do tipo A, que representa uma fonte de luz incandescente. É utilizada como referência para simular iluminação residencial comum."
        },
        18: {
            "value": "Standard Light B",
            "description": "Luz padrão do tipo B, usada para representar a luz solar direta. Faz parte das referências padronizadas para avaliação de reprodução de cores."
        },
        19: {
            "value": "Standard Light C",
            "description": "Luz padrão do tipo C, que simula a luz do dia média. É outra referência importante em estudos de temperatura de cor e fidelidade tonal."
        },
        20: {
            "value": "D55",
            "description": "Iluminante D55, com temperatura de cor de 5500 Kelvin. É utilizado como padrão na indústria gráfica e fotográfica para condições de luz do dia."
        },
        21: {
            "value": "D65",
            "description": "Iluminante D65, com temperatura de cor de 6500 Kelvin. Representa a luz do dia média na Europa e é o padrão mais comum para monitores e softwares de edição."
        },
        22: {
            "value": "D75",
            "description": "Iluminante D75, com temperatura de cor de 7500 Kelvin. Simula uma luz do dia com maior componente azul, típica de céus muito claros."
        },
        23: {
            "value": "D50",
            "description": "Iluminante D50, com temperatura de cor de 5000 Kelvin. É um padrão amplamente utilizado nas artes gráficas e na indústria de impressão."
        },
        24: {
            "value": "ISO Studio Tungsten",
            "description": "Iluminação de tungstênio para estúdio, conforme padrão ISO. Utilizada em ambientes profissionais para obter uma luz contínua e de alta intensidade."
        },
        255: {
            "value": "Other Light Source",
            "description": "Outra fonte de luz não listada nas categorias padrão do EXIF. Este valor é utilizado para indicar uma condição de iluminação fora do comum."
        }
    }
# DERIVED_INDIVIDUAL_FIELDS MOVED TO CUSTOM_FIELDS
# DERIVED_INDIVIDUAL_FIELDS = { ... }

"""
### Lista 2 – Informações do conjunto geral de dados

- **tempo_total_sequencia**: Duração total (segundos) desde a primeira até a última imagem da sequência (diferença entre DateTimeOriginal da última e da primeira).
- **integral_velocidade**: Distância total percorrida (metros) pelo drone durante toda a missão, obtida pela soma de `distancia_3d_anterior` para todas as imagens consecutivas.
- **taxa_de_obturacao**: Frequência média de captura (fotos por segundo) ao longo da sequência, calculada como (número de imagens) / tempo_total_sequencia.
- **sentido_de_voo**: Direção dominante do voo (ex.: “Norte”, “Sul”, “Nordeste”, etc.) determinada pela média dos azimutes de deslocamento (`direcao_deslocamento`).
- **altitude_relativa_media**: Média da `RelativeAltitude` (ou `AbsoluteAltitude` caso a relativa não exista) para todas as imagens, representando a altura média de voo.
- **variacao_rtk_entre_fotos**: Diferença média (ou máxima) dos desvios padrão RTK (`RtkStdLon`, `RtkStdLat`, `RtkStdHgt`) entre imagens consecutivas, indicando estabilidade da correção.
- **distribuicao_sobreposicao**: Estatísticas (mínimo, máximo, média, mediana, desvio padrão) da `sobreposicao_prevista` ao longo do conjunto, para avaliar a uniformidade da cobertura.
- **perfil_de_velocidade**: Estatísticas descritivas das velocidades (`velocidade_media_entre_fotos` e `velocidade_linear_instantanea`) – média, desvio, máximo – caracterizando o tipo de voo.
- **mapa_de_trajetoria**: Lista ordenada de coordenadas (latitude, longitude, altitude) de cada imagem, permitindo visualização do percurso completo em um mapa.
- **identificacao_de_passagens**: Detecção automática de padrões de ida e volta (linhas de voo), baseada na alternância da `direcao_deslocamento` (variação próxima a 180°).
- **falhas_ou_manobras**: Lista ou contagem de imagens onde `flag_mudanca_brusca` foi verdadeira, indicando possíveis pausas, mudanças abruptas ou falhas de comunicação.
- **percentual_de_imagens_adequadas**: Proporção de imagens com `potencial_de_ortoretificacao` acima de um limiar (ex.: > 80), útil para avaliar a qualidade geral do conjunto.
- **estimativa_de_area_coberta**: Área total aproximada (km² ou ha) varrida pelo conjunto, calculada pela união das `cobertura_estimada` de cada imagem, considerando sobreposição.
- **consistencia_de_metadados**: Percentual de imagens que possuem todos os campos críticos (GPS, atitude, RTK, etc.) preenchidos, indicando completude dos dados.
- **calibracao_do_conjunto**: Identificação se houve variação sistemática em parâmetros como `CalibratedFocalLength` ou `DewarpData` entre imagens, indicando possíveis mudanças de configuração durante o voo.
"""
    
"""
    ### 3. Novos campos derivados (informação calculada, não dados brutos)

Estes campos são computados a partir dos metadados existentes, considerando a sequência ordenada de imagens (por `DateTimeOriginal`). Eles transformam dados isolados em informação contextual.

- **tempo_desde_anterior** – intervalo em segundos entre a foto atual e a foto anterior (`DateTimeOriginal` atual – anterior). Útil para avaliar frequência de captura e sincronia.
- **distancia_geodesica_anterior** – distância em metros entre a posição GPS atual e a anterior, calculada pela fórmula de Haversine usando `GPSLatitude`, `GPSLongitude` e as altitudes (`AbsoluteAltitude` ou `GPSAltitude`). Indica o deslocamento entre pontos.
- **distancia_3d_anterior** – distância tridimensional entre a posição atual e a anterior, combinando a distância horizontal (haversine) com a diferença de altitude (`AbsoluteAltitude`). Mais realista para voos.
- **velocidade_linear_instantanea** – módulo da velocidade vetorial fornecida pelos campos `FlightXSpeed`, `FlightYSpeed`, `FlightZSpeed` (se presentes): `sqrt(XSpeed² + YSpeed² + ZSpeed²)` em m/s. Representa a velocidade total do drone no momento da captura.
- **velocidade_media_entre_fotos** – velocidade média (m/s) entre a foto anterior e a atual, calculada como `distancia_3d_anterior / tempo_desde_anterior`. Permite detectar variações de velocidade entre tomadas.
- **direcao_deslocamento** – azimute (graus) do deslocamento entre duas imagens consecutivas, derivado das coordenadas GPS. Útil para verificar se a trajetória segue um padrão (ex.: voo em linha reta).
- **angulo_de_incidencia** – ângulo entre o eixo óptico da câmera e a vertical do terreno, combinando `GimbalPitchDegree` e a inclinação do drone (`FlightPitchDegree`). Importante para análises fotogramétricas.
- **cobertura_estimada** – largura (m) e altura (m) da área capturada no solo, calculada a partir da altitude (`AbsoluteAltitude`), ângulo de gimbal, campo de visão da câmera (derivado do modelo) e formato do sensor. Permite avaliar sobreposição de imagens.
- **sobreposicao_prevista** – percentual de sobreposição longitudinal com a imagem anterior, baseada na distância percorrida e na cobertura estimada. Essencial para qualidade de ortomosaico.
- **tempo_desde_inicio_voo** – tempo decorrido desde a primeira imagem da sequência (ou desde o início do voo, se houver registro). Ajuda a sincronizar eventos.
- **precisao_rtk_efetiva** – classificação da precisão baseada nos campos `RtkFlag`, `RtkStdLon`, `RtkStdLat`, `RtkStdHgt` e `RtkDiffAge`. Exemplo: “Alta (cm)”, “Média (dm)”, “Baixa (m)”, “Sem RTK”.
- **variacao_rtk_entre_fotos** – diferença nos valores de `RtkStdLon` (ou similares) entre imagens consecutivas, indicando se a qualidade da correção se manteve estável.
- **altitude_relativa_media** – média da `RelativeAltitude` (se disponível) em uma janela de imagens, para estimar altura de voo em relação ao ponto de decolagem.
- **taxa_de_obturacao** – número de fotos por segundo no conjunto (frequência média), útil para identificar modo burst ou intervalo programado.
- **sentido_de_voo** – direção geral do voo (ex.: “Norte”, “Sul”, etc.) baseada na média dos azimutes de deslocamento.
- **integral_velocidade** – distância total percorrida pelo drone durante a missão (soma das `distancia_3d_anterior`), em metros.
- **tempo_total_sequencia** – duração total desde a primeira até a última imagem (segundos).
- **flag_mudanca_brusca** – indicador booleano que alerta quando `tempo_desde_anterior` > 2× média ou `distancia_geodesica_anterior` > 2× mediana, sinalizando possíveis falhas ou manobras não programadas.
- **e_sobreposicao_ideal** – booleano baseado na `sobreposicao_prevista` comparada com um limiar (ex.: > 60% para longitudinal), útil para controle de qualidade.
- **velocidade_angular_gimbal** – derivada da variação de `GimbalYawDegree` entre imagens consecutivas (graus/s), para verificar se o gimbal estava estável ou em movimento.
- **potencial_de_ortoretificacao** – score (0–100) que combina precisão RTK, ângulo de gimbal, distância focal calibrada (`CalibratedFocalLength`) e presença de dados de dewarp (`DewarpFlag`), indicando se a imagem é adequada para processamento fotogramétrico de alta precisão.
    """
    
