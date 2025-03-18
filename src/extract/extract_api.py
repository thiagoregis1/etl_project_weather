

class ExtractAPI:
    def __init__(self, data=None):
        self.data = data
        self.columns = self.extract_columns() if data else None

    def extract_columns(self):
        if not self.data:
            return None

        return {
            "name": self.data.get("name"),
            "lon": self.data["coord"].get("lon"),
            "lat": self.data["coord"].get("lat"),
            "weather_id": self.data["weather"][0].get("id") if self.data["weather"] else None,
            "weather_main": self.data["weather"][0].get("main") if self.data["weather"] else None,
            "weather_description": self.data["weather"][0].get("description") if self.data["weather"] else None,
            "weather_icon": self.data["weather"][0].get("icon") if self.data["weather"] else None,
            "base": self.data.get("base"),
            "temp": self.data["main"].get("temp"),
            "feels_like": self.data["main"].get("feels_like"),
            "temp_min": self.data["main"].get("temp_min"),
            "temp_max": self.data["main"].get("temp_max"),
            "pressure": self.data["main"].get("pressure"),
            "humidity": self.data["main"].get("humidity"),
            "sea_level": self.data["main"].get("sea_level"),
            "grnd_level": self.data["main"].get("grnd_level"),
            "visibility": self.data.get("visibility"),
            "wind_speed": self.data["wind"].get("speed"),
            "wind_deg": self.data["wind"].get("deg"),
            "clouds_all": self.data["clouds"].get("all"),
            "dt": self.data.get("dt"),
            "sys_type": self.data["sys"].get("type"),
            "sys_id": self.data["sys"].get("id"),
            "country": self.data["sys"].get("country"),
            "sunrise": self.data["sys"].get("sunrise"),
            "sunset": self.data["sys"].get("sunset"),
            "timezone": self.data.get("timezone"),
            "id": self.data.get("id"),
            "cod": self.data.get("cod"),
        }
