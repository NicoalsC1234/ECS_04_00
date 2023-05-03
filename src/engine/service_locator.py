from src.engine.services.images_services import ImagesServices
from src.engine.services.sounds_services import SoundServices

class ServiceLocator:
    images_service = ImagesServices()
    sounds_service = SoundServices()