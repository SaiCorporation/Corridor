# Mocked SMBIOS detection
def detect_model() -> str:
    # In reality, would parse DMI/SMBIOS; here we rotate through known models.
    models = ["XPS13-9300", "Latitude-7420", "Precision-5550"]
    # Simple deterministic pick so tests are stable
    return models[0]
