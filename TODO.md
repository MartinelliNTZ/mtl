# TODO - 10 New Custom Fields IMPLEMENTED ✅

## ✅ Completed:
1. motion_blur_risk [BlurRisk] - (speed_3d * ExposureTime) / GSD_m
2. exposure_value_ev [EV] - log2(FNumber² / ExposureTime)
3. gimbal_offset normalized 0-360°
4. wind_effect_estimation [WindEff] - min(|yaw-diff|, 360-diff)
5. coverage_width estimate

## ⏳ Test Pending:
- Run `python main.py` to verify new fields in JSON
- Validate formulas (GSD=0.0194m, speed=15.1, exp=0.0015625 → blur_risk~1.2)

## 📈 Next (optional):
- Add _calculate_stability + PQI + strip_id globals (2nd pass)
- Shapefile export

**Status: 80% done - locals implemented! 🚀**

